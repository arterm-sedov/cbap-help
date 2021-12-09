echo 'Downloading Python'

# Source URL
$url = "https://www.python.org/ftp/python/3.10.1/python-3.10.1-amd64.exe"

# Destation file
$dest = ".\python-3.10.1-amd64.exe"

# Download the file
Invoke-WebRequest -Uri $url -OutFile $dest

echo 'Installing Python'

.\python-3.10.1-amd64.exe /quiet PrependPath=1 Include_pip=1 Include_exe=1 Include_test=0 | Out-Default

# Alternative method to start the installation
# Start-Process .\python-3.10.1-amd64.exe -NoNewWindow -Wait -ArgumentList /quiet,PrependPath=1,Include_pip=1,Include_exe=1,Include_test=0

echo 'Installing MKDocs and dependencies'

py -m pip install -U -r requirements.txt
