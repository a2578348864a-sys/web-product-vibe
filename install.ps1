param(
  [ValidateSet('codex','claude','dsh','all')]
  [string]$HostType = 'all',
  [string]$ProjectRoot = (Get-Location).Path
)

$ErrorActionPreference = 'Stop'
$PackageRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'

function Install-Skill($Source, $Destination) {
  if (-not (Test-Path $Source)) {
    throw "Source skill not found: $Source"
  }

  New-Item -ItemType Directory -Force -Path (Split-Path -Parent $Destination) | Out-Null

  if (Test-Path $Destination) {
    $Backup = "$Destination.backup-$Timestamp"
    Move-Item -Path $Destination -Destination $Backup
    Write-Host "Backed up: $Backup"
  }

  Copy-Item -Recurse -Force $Source $Destination
  Write-Host "Installed: $Destination"
}

$SkillSource = Join-Path $PackageRoot 'skill\web-product-vibe'
$AgentsDestination = Join-Path $ProjectRoot '.agents\skills\web-product-vibe'
$ClaudeDestination = Join-Path $ProjectRoot '.claude\skills\web-product-vibe'

if ($HostType -eq 'codex' -or $HostType -eq 'dsh') {
  Install-Skill $SkillSource $AgentsDestination
}
elseif ($HostType -eq 'claude') {
  Install-Skill $SkillSource $ClaudeDestination
}
elseif ($HostType -eq 'all') {
  Install-Skill $SkillSource $AgentsDestination
  Install-Skill $SkillSource $ClaudeDestination
}
