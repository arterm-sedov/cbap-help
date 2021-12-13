echo 'Uninstalling Python'

.\python_latest.exe /uninstall /quiet | Out-Default

# Alternative method to start the uninstallation
# Start-Process .\python_latest.exe -NoNewWindow -Wait -ArgumentList /uninstall,/quiet
