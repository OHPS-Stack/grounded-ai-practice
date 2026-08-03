# Builds a slimmed copy of the repo for the Claude surfaces that take a folder
# -- Cowork and Design.
#
# Not for Projects: that reads a branch on GitHub rather than a local folder,
# so its size limit is fixed by deselecting assets/ and drafts/ in its own file
# picker, which also keeps it syncing. The Docs set below is the same content
# you would upload if you ever wanted a Project knowledge base maintained by
# hand instead.
#
# Why this exists. Two separate problems, one answer:
#
#   1. Size. The repo is ~6.7 MB, but 6.3 MB of that is binary output --
#      252 files under assets/ (mostly PNG exports) and the two files in
#      drafts/ (a .docx and its self-check PDF render). The material that
#      actually functions as context is the ~530 KB of markdown. Handing a
#      surface the whole repo spends its entire budget on files it cannot
#      reason about.
#
#   2. Exposure. internal/ and the .claude-memory junction both sit inside
#      C:\dev\grounded-ai-practice. Cowork processes work on Anthropic's
#      servers rather than locally by default, so granting it the repo root
#      would send exactly the material the public/internal split exists to
#      keep out of circulation. .gitignore and the pre-commit hook do not
#      help -- they guard commits, not file access. See CLAUDE.md,
#      "Choosing the right Claude surface".
#
# So the destination is deliberately OUTSIDE the repo, and the script refuses
# to write anywhere inside it. Regenerate by re-running rather than editing
# the copy by hand: the share folder is disposable output, never a second
# source of truth. Anything worth keeping goes back into the repo.
#
# Note this copies the working tree, not a commit -- unlike a Project's GitHub
# sync, it does include uncommitted work. That is usually what you want when
# handing current drafts to Cowork, and worth remembering when the two
# surfaces disagree about what the project says.
#
# Usage:
#   powershell -File tools/make_share_folder.ps1                <- no arguments: opens the window
#   powershell -File tools/make_share_folder.ps1 -Mode Docs     <- scripted use, exactly as before
#   powershell -File tools/make_share_folder.ps1 -Mode All -Destination D:\gap-share
#
#   Bare invocation used to run a Docs build; since 2026-08-03 it opens the
#   window instead, per the GUI rule in CLAUDE.md. Scripted runs pass -Mode.
#
#   -Mode Docs    the six root markdown files, tools/, exports/.
#                 For Cowork and for a Projects file selection.
#   -Mode Design  logo SVGs, icon SVGs, the creative brief and project_brief.md
#                 for the palette and visual-identity decisions. Skips
#                 assets/logo/png (3.2 MB of raster exports of the same marks).
#   -Mode All     both sets.
#   -Gui          open the window explicitly.
#   -GuiSelfTest  internal: scripted window check used by the repo's
#                 verification -- renders the window offscreen to a PNG in the
#                 given folder and runs a Docs build into it, without showing
#                 anything.
#
# Safety: the destination is wiped and rebuilt on every run, so it will only
# write to a folder it created -- one carrying the .gap-share-folder marker it
# drops -- or to a path that does not exist yet. Pointing it at a folder with
# your own files in it aborts rather than deleting them; -Force overrides that
# and should be used only when you are certain what is in there. After copying,
# it re-scans the destination for internal/ and .claude-memory and deletes the
# whole output if either appears, on the principle that a share folder which
# might contain private material is worth less than no share folder at all.
#
# Requirements: PowerShell only. No Word, no Python, no Inkscape. The window
# uses WinForms, which is built into Windows PowerShell.

param(
    [ValidateSet('Docs', 'Design', 'All')][string]$Mode = 'Docs',
    [string]$Destination = 'C:\dev\gap-share',
    [switch]$Force,
    [switch]$Gui,
    [string]$GuiSelfTest
)

$ErrorActionPreference = "Stop"

$repo = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$marker = ".gap-share-folder"

# GAP palette (project_brief.md, "Visual identity") -- window colours only.
$GapPalette = @{
    Ink   = '#27221E'
    Ember = '#F15E4B'
    Paper = '#F9F9F9'
    Mist  = '#EFEEED'
    Stone = '#6E6E6E'
}

# Embedded GAP logo (base64 PNG). Filled by tools/embed_logo.py from
# assets/logo/png -- regenerate there if the brand assets change; never
# hand-edit. A copy of this script keeps its branding without the repo.
$LOGO_WORDMARK_PNG = @'
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
uBUYOi4zX/8fsVsipdQVSM0AAAAASUVORK5CYII=
'@

$LOGO_SYMBOL_64_PNG = @'
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
SUVORK5CYII=
'@

$LOGO_SYMBOL_32_PNG = @'
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAEPElEQVR42sVXXWhcRRT+zszdZN24
mt0N3ULRQGqapEkT8TFWfWrtQ9EK0ofG/vjzJEKLFdI00eqjRYSC1YjQgoINBQVLGwIWJFqE0L5o
V+2LGrCVQtIYKW524905PuydOzN77zZNTPQ+3Mt+d+5833znzDmzxMz4Py8PAFpbWzMJ8t8mou1S
yKwQlJZCgISAFAQiCj8welnf/wJj0UzJ1TfOuiKYz8CRq9d+PuUBgMTix0rRTikIDAZz9UlgILjX
zmD9bAK4qUaXTRuPAbsAVAUoxY8QqqRgBiig1z/Naq3J4rB4B8KRNkZWCFjhfhLGYmZYQtiMvnuL
DRoRoklsAQCF8SUzuCoEgZBlWryUA8FTGEOMpf2PbsW2bTuC6dgIYVgYhxhrtC7GFgYzLhTA1mrB
2Pn0Lpw4OYqh4WOQQjqkZtxSBDWYJmF2IuUFTzIkhGPDQ1CVCgb2HUBXdw9eO/gKZmdnVmSx3rdu
ynCIi2hoGeXFMkaGBvHm60expbcPY599gZ7e3mVabFbLVlJxgCk7B0wSWrMAODv2KV7aPwApJU5/
Mob+rY/dtcWGWGO1icxODpATVyuhbty4jrm5W0gkErg3nXYsdQg4DqvngBHjmT1QjX/4BQEdXV0Y
/egUmjNZDB4+hInxC7X1OLKqmvJQBzOXAABSiuzcYjC2P7kDZ85+DiEl9u3ZjfEL55ZncQxmVs+u
AKVLTeDjnoG9OHFyFNPT09j9zFMofP/dyixml9je8oqVtQ3ZNB0GkF+/HhPj5zFyZBALpWK1GwYz
JpNJbOl7GNLzIo1gfn4ePxYKiBjPke7h1gF2CzDefec4BAkIISDIDd3hwaMY2Lu/bn9/8cBzuPT1
JNzS4IphmJIfFiK2e46u/8xgIiehJsbPI5vNOWcETVAsLuCnwg8BSQypLUa5Akz3CUgDDZHSeXlq
Cpenppa2uA7GNZtB5wBV2WqIg3MBhR9H+m19i+sQG4ydHHC3yp2IGbFJdmdSA3DcmRDh0SMwwhEC
UJAcy7HYeRs599ZUwvBjfRTT6w8zdiUWR8U4QvQuICLKt2TARBoDgYoE+KBqPpJpFQCxFRoKJ6PQ
4jgsmFVvKFZoSDSWtQNCV6C2to147/0P0dvXl/oP/hKktRHeulzz31JKfDV5CR0tGfDFc8Dt+bWl
z7T8Qs8+v9Hr7oaYuQmkUk3Fjs7OVOmD4/CvfLvmyxdtHfelAHjl8kMEzKJcKjX4vg+/tR1/Tl6M
S91VvRpKJaSCENC6XPMCETUePPQqhoZH4P9xC/7c7NpaQOKbZFv748TMyLdkrxKhRxChfdOm3zo3
b/79nsakkp5QnvBU2JFWMwPT6cLIG2+9TMyMDflcf6XCZ0jQg4IIQhAIwZNEsH14taNy+tfrN18g
/feciOSGfO4JKDwACEiPKoKoQkSV6EHq312KVCVZUl9em5m5/Q8rDQfdDkx5PQAAAABJRU5ErkJg
gg==
'@

function Invoke-ShareFolder {
    # The whole build, shared by the command line and the window.
    param(
        [string]$Mode,
        [string]$Destination,
        [switch]$Force,
        [scriptblock]$Log = { param($m) Write-Output $m }
    )

    # --- Guard 1: destination must sit outside the repo -----------------
    # Otherwise the whole point is defeated -- a share folder inside the
    # repo is adjacent to internal/ again, and would also get picked up by
    # the next `git add -A`.
    $destFull = [System.IO.Path]::GetFullPath($Destination)
    if ($destFull.TrimEnd('\') -ieq $repo.TrimEnd('\') -or $destFull.StartsWith($repo.TrimEnd('\') + '\', [StringComparison]::OrdinalIgnoreCase)) {
        throw "Destination '$destFull' is inside the repo. The share folder must live outside $repo -- that separation is the reason it exists. Try -Destination C:\dev\gap-share."
    }

    # --- Guard 2: never delete files this script did not put there ------
    if (Test-Path $destFull) {
        $existing = @(Get-ChildItem $destFull -Force)
        $isOurs = Test-Path (Join-Path $destFull $marker)
        if ($existing.Count -gt 0 -and -not $isOurs -and -not $Force) {
            throw "'$destFull' already exists, is not empty, and has no $marker file, so this script did not create it. Refusing to wipe it. Pick an empty or non-existent path, or pass -Force if you are certain its contents are disposable."
        }
        Get-ChildItem $destFull -Force | Remove-Item -Recurse -Force
    }
    else {
        New-Item -ItemType Directory -Path $destFull | Out-Null
    }

    # --- What each mode copies ------------------------------------------
    # Each entry is a source path relative to the repo root, an optional
    # filename filter, and the subfolder it lands in (empty = root).
    $sets = @{
        Docs   = @(
            @{ From = "."; Filter = "*.md"; To = ""; Recurse = $false },
            @{ From = "tools"; Filter = "*"; To = "tools"; Recurse = $false },
            @{ From = "exports"; Filter = "*"; To = "exports"; Recurse = $false }
        )
        Design = @(
            @{ From = "assets\logo"; Filter = "*.svg"; To = "assets\logo"; Recurse = $false },
            @{ From = "assets\logo"; Filter = "creative_brief.md"; To = "assets\logo"; Recurse = $false },
            @{ From = "assets\icons\svg"; Filter = "*.svg"; To = "assets\icons\svg"; Recurse = $false },
            @{ From = "assets\icons"; Filter = "README.md"; To = "assets\icons"; Recurse = $false },
            @{ From = "."; Filter = "project_brief.md"; To = ""; Recurse = $false }
        )
    }

    $plan = switch ($Mode) {
        'Docs' { $sets.Docs }
        'Design' { $sets.Design }
        'All' { $sets.Docs + $sets.Design }
    }

    $copied = 0
    $bytes = 0

    foreach ($item in $plan) {
        $src = Join-Path $repo $item.From
        if (-not (Test-Path $src)) {
            & $Log "warning: skipping '$($item.From)' -- not found in the repo. If it was renamed, update the copy sets in this script."
            continue
        }

        $targetDir = if ($item.To) { Join-Path $destFull $item.To } else { $destFull }
        if (-not (Test-Path $targetDir)) { New-Item -ItemType Directory -Path $targetDir -Force | Out-Null }

        foreach ($file in Get-ChildItem $src -File -Filter $item.Filter) {
            $dest = Join-Path $targetDir $file.Name
            if (Test-Path $dest) { continue }   # -Mode All overlaps on project_brief.md
            Copy-Item $file.FullName $dest
            $copied++
            $bytes += $file.Length
        }
    }

    # --- Guard 3: post-copy audit ---------------------------------------
    # The copy sets above are explicit allow-lists, so nothing private
    # should be reachable. This checks anyway, because the cost of being
    # wrong is the one thing the public/internal split exists to prevent.
    $leaked = @(Get-ChildItem $destFull -Recurse -Force | Where-Object {
            $_.FullName -imatch '[\\/](internal|\.claude-memory)([\\/]|$)'
        })
    if ($leaked.Count -gt 0) {
        Get-ChildItem $destFull -Force | Remove-Item -Recurse -Force
        throw "Private material reached the share folder ($($leaked.Count) path(s) matching internal/ or .claude-memory). The output has been deleted. Do not use this script again until the copy sets are fixed."
    }

    Set-Content -Path (Join-Path $destFull $marker) -Encoding utf8 -Value @"
Generated by tools/make_share_folder.ps1 from $repo
Mode: $Mode
Built: $(Get-Date -Format 'yyyy-MM-dd HH:mm')

Disposable output, not a source of truth. Re-run the script to refresh it;
anything worth keeping belongs back in the repo. Safe to hand to Cowork or
Design -- the repo root is not, because internal/ sits inside it.
"@

    [pscustomobject]@{ Mode = $Mode; Destination = $destFull; Copied = $copied; Bytes = $bytes }
}

function Show-ShareFolderGui {
    # The window: a thin layer over Invoke-ShareFolder, exposing the two
    # decisions a person makes -- what to copy, where to build it.
    param([string]$SelfTestFolder)

    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    [System.Windows.Forms.Application]::EnableVisualStyles()

    $ink = [System.Drawing.ColorTranslator]::FromHtml($GapPalette.Ink)
    $ember = [System.Drawing.ColorTranslator]::FromHtml($GapPalette.Ember)
    $paper = [System.Drawing.ColorTranslator]::FromHtml($GapPalette.Paper)
    $mist = [System.Drawing.ColorTranslator]::FromHtml($GapPalette.Mist)
    $stone = [System.Drawing.ColorTranslator]::FromHtml($GapPalette.Stone)
    $white = [System.Drawing.Color]::White

    $form = New-Object System.Windows.Forms.Form
    $form.Text = 'Build a share folder'
    $form.StartPosition = 'CenterScreen'
    $form.BackColor = $paper
    $form.ForeColor = $ink
    $form.Font = New-Object System.Drawing.Font('Segoe UI', 9)
    $form.ClientSize = New-Object System.Drawing.Size(620, 560)
    $form.MinimumSize = $form.Size

    $script:LogoStreams = @()  # Image.FromStream needs its stream kept alive
    function ConvertFrom-LogoB64([string]$B64) {
        $bytes = [Convert]::FromBase64String(($B64 -replace '\s', ''))
        $ms = New-Object System.IO.MemoryStream(, $bytes)
        $script:LogoStreams += $ms
        [System.Drawing.Image]::FromStream($ms)
    }

    try {
        $pb = New-Object System.Windows.Forms.PictureBox
        $pb.Image = ConvertFrom-LogoB64 $LOGO_WORDMARK_PNG
        $pb.SizeMode = 'Zoom'
        $pb.Location = New-Object System.Drawing.Point(12, 12)
        $pb.Size = New-Object System.Drawing.Size(180, 64)
        $form.Controls.Add($pb)
        $symbol = ConvertFrom-LogoB64 $LOGO_SYMBOL_64_PNG
        $form.Icon = [System.Drawing.Icon]::FromHandle(([System.Drawing.Bitmap]$symbol).GetHicon())
    }
    catch {
        # blobs absent or corrupted: text header instead, same layout
        $fallback = New-Object System.Windows.Forms.Label
        $fallback.Text = 'Grounded AI Practice'
        $fallback.Font = New-Object System.Drawing.Font('Segoe UI', 13, [System.Drawing.FontStyle]::Bold)
        $fallback.Location = New-Object System.Drawing.Point(12, 24)
        $fallback.AutoSize = $true
        $form.Controls.Add($fallback)
    }

    $bold = New-Object System.Drawing.Font('Segoe UI', 10, [System.Drawing.FontStyle]::Bold)
    function Add-Label([string]$Text, [int]$X, [int]$Y, $Font, $Colour) {
        $l = New-Object System.Windows.Forms.Label
        $l.Text = $Text
        $l.Location = New-Object System.Drawing.Point($X, $Y)
        $l.AutoSize = $true
        if ($Font) { $l.Font = $Font }
        if ($Colour) { $l.ForeColor = $Colour }
        $form.Controls.Add($l)
        $l
    }

    [void](Add-Label '1.  What to copy' 12 92 $bold $ink)
    $script:RDocs = New-Object System.Windows.Forms.RadioButton
    $script:RDocs.Text = 'Docs - the markdown, tools and exports (for Cowork, or a Projects selection)'
    $script:RDocs.Location = New-Object System.Drawing.Point(16, 116)
    $script:RDocs.AutoSize = $true
    $script:RDocs.Checked = $true
    $script:RDesign = New-Object System.Windows.Forms.RadioButton
    $script:RDesign.Text = 'Design - logo and icon SVGs plus the creative brief (for Design)'
    $script:RDesign.Location = New-Object System.Drawing.Point(16, 140)
    $script:RDesign.AutoSize = $true
    $script:RAll = New-Object System.Windows.Forms.RadioButton
    $script:RAll.Text = 'All - both sets'
    $script:RAll.Location = New-Object System.Drawing.Point(16, 164)
    $script:RAll.AutoSize = $true
    $form.Controls.AddRange(@($script:RDocs, $script:RDesign, $script:RAll))

    [void](Add-Label '2.  Where to build it' 12 200 $bold $ink)
    $script:GuiDest = New-Object System.Windows.Forms.TextBox
    $script:GuiDest.Text = 'C:\dev\gap-share'
    $script:GuiDest.Location = New-Object System.Drawing.Point(16, 224)
    $script:GuiDest.Size = New-Object System.Drawing.Size(460, 23)
    $script:GuiDest.BackColor = $white
    $script:GuiDest.ForeColor = $ink
    $form.Controls.Add($script:GuiDest)
    $browse = New-Object System.Windows.Forms.Button
    $browse.Text = 'Browse...'
    $browse.Location = New-Object System.Drawing.Point(484, 223)
    $browse.Size = New-Object System.Drawing.Size(90, 25)
    $browse.BackColor = $mist
    $browse.FlatStyle = 'Flat'
    $browse.FlatAppearance.BorderColor = $stone
    $browse.Add_Click({
            $dlg = New-Object System.Windows.Forms.FolderBrowserDialog
            $dlg.Description = 'Choose where to build the share folder (outside the repo)'
            if ($dlg.ShowDialog() -eq 'OK') { $script:GuiDest.Text = $dlg.SelectedPath }
        })
    $form.Controls.Add($browse)
    [void](Add-Label 'Must be outside the repo. Wiped and rebuilt on every run - disposable output, never a source of truth.' 16 252 $null $stone)

    $script:BuildBtn = New-Object System.Windows.Forms.Button
    $script:BuildBtn.Text = 'Build'
    $script:BuildBtn.Location = New-Object System.Drawing.Point(12, 282)
    $script:BuildBtn.Size = New-Object System.Drawing.Size(120, 32)
    $script:BuildBtn.BackColor = $ember
    $script:BuildBtn.ForeColor = $white
    $script:BuildBtn.FlatStyle = 'Flat'
    $script:BuildBtn.FlatAppearance.BorderSize = 0
    $script:BuildBtn.Font = $bold
    $form.Controls.Add($script:BuildBtn)

    $script:GuiLog = New-Object System.Windows.Forms.TextBox
    $script:GuiLog.Multiline = $true
    $script:GuiLog.ReadOnly = $true
    $script:GuiLog.ScrollBars = 'Vertical'
    $script:GuiLog.Font = New-Object System.Drawing.Font('Consolas', 9)
    $script:GuiLog.BackColor = $white
    $script:GuiLog.ForeColor = $ink
    $script:GuiLog.Location = New-Object System.Drawing.Point(12, 326)
    $script:GuiLog.Size = New-Object System.Drawing.Size(596, 222)
    $script:GuiLog.Anchor = 'Top,Bottom,Left,Right'
    $form.Controls.Add($script:GuiLog)

    $script:SelfTestMode = [bool]$SelfTestFolder
    $doBuild = {
        $script:GuiLog.Clear()
        $mode = if ($script:RAll.Checked) { 'All' } elseif ($script:RDesign.Checked) { 'Design' } else { 'Docs' }
        $script:BuildBtn.Enabled = $false
        [System.Windows.Forms.Application]::DoEvents()
        try {
            $r = Invoke-ShareFolder -Mode $mode -Destination $script:GuiDest.Text -Log { param($m) $script:GuiLog.AppendText("$m`r`n") }
            $script:GuiLog.AppendText("Mode:    $($r.Mode)`r`n")
            $script:GuiLog.AppendText(("Copied:  {0} files, {1:N2} MB`r`n" -f $r.Copied, ($r.Bytes / 1MB)))
            $script:GuiLog.AppendText("Built:   $($r.Destination)`r`n`r`n")
            $script:GuiLog.AppendText("Safe to hand to Cowork or Design. Re-run to refresh; anything worth keeping belongs back in the repo.`r`n")
            if (-not $script:SelfTestMode) { Start-Process explorer.exe $r.Destination }
        }
        catch {
            $script:GuiLog.AppendText("STOPPED: $($_.Exception.Message)`r`n")
        }
        finally {
            $script:BuildBtn.Enabled = $true
        }
    }
    $script:BuildBtn.Add_Click($doBuild)

    if ($SelfTestFolder) {
        # Scripted self-check: show for a moment (DrawToBitmap only paints
        # child controls once the window has been shown), screenshot, build
        # into the test folder, print the log.
        $form.Show()
        [System.Windows.Forms.Application]::DoEvents()
        Start-Sleep -Milliseconds 250
        [System.Windows.Forms.Application]::DoEvents()
        $bmp = New-Object System.Drawing.Bitmap($form.Width, $form.Height)
        $form.DrawToBitmap($bmp, (New-Object System.Drawing.Rectangle(0, 0, $form.Width, $form.Height)))
        $bmp.Save((Join-Path $SelfTestFolder 'share_gui.png'), [System.Drawing.Imaging.ImageFormat]::Png)
        $script:GuiDest.Text = Join-Path $SelfTestFolder 'share_gui_out'
        & $doBuild
        Write-Output $script:GuiLog.Text
        $form.Dispose()
        return
    }

    [void]$form.ShowDialog()
    $form.Dispose()
}

if ($GuiSelfTest) {
    Show-ShareFolderGui -SelfTestFolder $GuiSelfTest
    return
}
if ($Gui -or $PSBoundParameters.Count -eq 0) {
    Show-ShareFolderGui
    return
}

$result = Invoke-ShareFolder -Mode $Mode -Destination $Destination -Force:$Force

Write-Output ""
Write-Output "  Mode:        $($result.Mode)"
Write-Output "  Destination: $($result.Destination)"
Write-Output "  Copied:      $($result.Copied) files, $('{0:N2}' -f ($result.Bytes / 1MB)) MB"
Write-Output ""
