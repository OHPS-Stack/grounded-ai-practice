# Opens a .docx in real Microsoft Word, saves it, and closes it — to verify
# the document survives a Word save/round-trip without errors or silent
# downgrading. Complements tools/word_preview.ps1, which only checks how a
# document RENDERS; this checks whether it can actually be EDITED AND SAVED.
#
# Motivating bug (2026-07-28): a document rendered perfectly but Word refused
# to save it, reporting "You can't put drawing objects into a text box,
# callout, comment, footnote or endnote." Root cause was a missing
# compatibilityMode declaration in settings.xml, which made Word treat the
# file as Word 2007-era and downgrade its DrawingML shape groups to legacy
# VML on save. Rendering checks could never have caught that.
#
# Usage: powershell -File tools/word_roundtrip_test.ps1 -Path "path\to\file.docx"
#
# Safety: same approach as word_preview.ps1 — verifies a NEW WINWORD.exe
# process actually spawned before automating anything, so an existing Word
# session with unsaved work is never touched. ALWAYS run this against a
# throwaway copy: it saves the file in place.

param(
    [Parameter(Mandatory = $true)][string]$Path
)

$ErrorActionPreference = "Stop"
$Path = (Resolve-Path $Path).Path

$before = @(Get-Process WINWORD -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Id)

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

$after = @(Get-Process WINWORD -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Id)
$newPid = @($after | Where-Object { $before -notcontains $_ }) | Select-Object -First 1

if (-not $newPid) {
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
    throw "Word.Application attached to an already-running WINWORD.exe instead of starting a new one -- refusing to automate it in case it's a window you have open with unsaved work."
}

$result = "UNKNOWN"
try {
    $doc = $word.Documents.Open($Path, $false, $false)   # ReadOnly = false
    try {
        $doc.Save()
        $result = "SAVE OK"
    }
    catch {
        $result = "SAVE FAILED: $($_.Exception.Message)"
    }
    $doc.Close(0)
    $word.Quit()
}
catch {
    $result = "OPEN FAILED: $($_.Exception.Message)"
    try { $word.Quit() } catch {}
}
finally {
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
    $stillRunning = $null
    for ($i = 0; $i -lt 10; $i++) {
        $stillRunning = Get-Process -Id $newPid -ErrorAction SilentlyContinue
        if (-not $stillRunning) { break }
        Start-Sleep -Milliseconds 500
    }
    if ($stillRunning) {
        Stop-Process -Id $newPid -Force
        Write-Warning "Word (PID $newPid) had not exited 5s after Quit() and was force-stopped."
    }
}

Write-Output $result
