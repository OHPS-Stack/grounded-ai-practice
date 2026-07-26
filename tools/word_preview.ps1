# Renders a .docx through the real Microsoft Word engine (via COM automation)
# so Claude can visually self-check formatting the same way Word would show it,
# instead of relying on LibreOffice's approximate rendering.
#
# Usage: powershell -File tools/word_preview.ps1 -Path "path\to\file.docx"
#
# Safety: New-Object -ComObject Word.Application is assumed to spawn a fresh,
# separate Word process, but that isn't guaranteed by Word's COM registration.
# This script verifies a *new* WINWORD.exe PID actually appeared before doing
# anything; if it doesn't (i.e. we'd be attaching to a Word window you already
# had open), it aborts instead of risking Quit()-ing your own session and
# losing unsaved work. Only the PID we confirmed spawning is ever touched.

param(
    [Parameter(Mandatory = $true)][string]$Path,
    [string]$OutPath
)

$ErrorActionPreference = "Stop"

$Path = (Resolve-Path $Path).Path
if (-not $OutPath) {
    $OutPath = [System.IO.Path]::ChangeExtension($Path, "pdf")
}

$before = @(Get-Process WINWORD -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Id)

$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0

$after = @(Get-Process WINWORD -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Id)
$newPid = @($after | Where-Object { $before -notcontains $_ }) | Select-Object -First 1

if (-not $newPid) {
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
    throw "Word.Application attached to an already-running WINWORD.exe instead of starting a new one -- refusing to automate it in case it's a window you have open with unsaved work. Close your own Word windows and re-run, or investigate why COM didn't spawn a separate instance."
}

try {
    $doc = $word.Documents.Open($Path, $false, $true)   # ReadOnly = $true
    $doc.ExportAsFixedFormat($OutPath, 17)               # 17 = wdExportFormatPDF
    $doc.Close(0)                                        # 0 = wdDoNotSaveChanges
    $word.Quit()
}
catch {
    throw "Word automation failed on '$Path': $_"
}
finally {
    [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
    # Quit() returns before the process necessarily finishes unloading, so
    # poll for a few seconds of normal teardown before treating it as hung --
    # force-killing a process still mid-shutdown is itself an unclean exit,
    # which risks causing the exact crash-recovery slowdown this guards against.
    $stillRunning = $null
    for ($i = 0; $i -lt 10; $i++) {
        $stillRunning = Get-Process -Id $newPid -ErrorAction SilentlyContinue
        if (-not $stillRunning) { break }
        Start-Sleep -Milliseconds 500
    }
    if ($stillRunning) {
        Stop-Process -Id $newPid -Force
        Write-Warning "Word (PID $newPid) had not exited 5s after Quit() and was force-stopped. This can leave crash-recovery state that slows the next run's startup."
    }
}

Write-Output $OutPath
