echo 'Uninstalling MKDocs and dependencies'

py -m pip uninstall -y -r requirements.txt

echo 'Uninstalling Python'

.\python-3.10.1-amd64.exe /uninstall /quiet | Out-Default

# Alternative method to start the uninstallation
# Start-Process .\python-3.10.1-amd64.exe -NoNewWindow -Wait -ArgumentList /uninstall,/quiet
