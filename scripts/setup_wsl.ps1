<#
.SYNOPSIS
Installs and configs WSL2 environment for Docker operations.

.DESCRIPTION
This script prepares the Windows host to manage the Docker/WSL2 security boundary 
required by the local agentic architecture. 
#>

Write-Host "Verifying WSL is installed..." -ForegroundColor Green

$wslStatus = wsl --status 2>&1
if ($wslStatus -match "is not recognized" -or $wslStatus -match "no installed distributions") {
    Write-Host "WSL 2 is not installed or configured. Installing..." -ForegroundColor Yellow
    wsl --install -d Ubuntu
    Write-Host "Please restart your computer and re-run this script." -ForegroundColor Red
    exit
} else {
    Write-Host "WSL is installed. Ensuring version 2..." -ForegroundColor Green
    wsl --set-default-version 2
}

Write-Host "Docker Desktop should be set to use the WSL 2 based engine." -ForegroundColor Cyan
Write-Host "Initialization script completed." -ForegroundColor Green
