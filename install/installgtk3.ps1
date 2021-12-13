# GTK3 is needed to output PDF files from MkDocs. It is not needed to build Web Help.
# You might need to set PATH variable to the installation folder for correct operation.

echo 'Downloading GTK3'

# Source URL
$SiteAdress = "https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases"
$HttpContent = Invoke-WebRequest -URI $SiteAdress
$HttpContent.Links | Where-Object {$_.href -like "*win64.exe"} | %{$url = "https://github.com" + $_.href} 

# Destation file
$dest = ".\gtk3_latest.exe"

echo $url 
echo "to" 
echo $dest

Invoke-WebRequest -Uri $url -OutFile ($dest)

echo 'Installing GTK3'

& $dest
