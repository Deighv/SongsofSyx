[string]$rootPathForFiles = 
[string[]]$listOfFilesToRename = Get-ChildItem -Path $rootPathForFiles -Filter '*.save' | Select-Object -ExpandProperty FullName
$listOfFilesToRename | ForEach-Object {
    [string]$newName = Split-Path -Path $_ -Leaf 
    
    $newName = $newName -replace '^(\w+)-([0-9a-fA-F]+)-(\w+)-0-([0-9a-fA-F]+)[(.save)]', '$2'    
    Write-Verbose $newName -Verbose
    $newName = $newName.Replace('.save', '')
    $newName = $newName.Replace('save', '') #I know I know
    $newName = [System.Convert]::ToInt32($newName,16)
    Write-Verbose $newName -Verbose
    Rename-Item -Path $_ -NewName $newName".save"
}
