for($i = 0; $i -lt 5000; $i++){
    git add .
    git commit -m 'auto commit'
    git push
    Start-Sleep 60
}