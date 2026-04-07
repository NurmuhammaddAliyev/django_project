$projectRoot = "D:\TEST"
$manageDir = Join-Path $projectRoot "config"
$pythonExe = Join-Path $projectRoot ".venv\Scripts\python.exe"

Set-Location $manageDir
& $pythonExe "manage.py" "runserver"
