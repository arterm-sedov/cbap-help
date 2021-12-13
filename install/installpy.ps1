echo 'Downloading Python'

# Source URL
$SiteAdress = "https://www.python.org/downloads/"
$HttpContent = Invoke-WebRequest -URI $SiteAdress
$HttpContent.Links | Where-Object {$_.href -like "*amd64.exe"} | %{$url = $_.href} 

# Destation file
$dest = ".\python_latest.exe"

echo $url 
echo "to" 
echo $dest

Invoke-WebRequest -Uri $url -OutFile ($dest)

echo 'Installing Python'

& $dest /quiet PrependPath=1 Include_pip=1 Include_exe=1 Include_test=0 | Out-Default

# Alternative method to start the installation
# Start-Process .\python_latest.exe -NoNewWindow -Wait -ArgumentList /quiet,PrependPath=1,Include_pip=1,Include_exe=1,Include_test=0