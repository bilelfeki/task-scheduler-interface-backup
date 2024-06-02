$fileConfig= ".\task-config.txt"
$schedular = ".\task-scheduler.ps1"
$lines = Get-Content -Path $fileConfig

foreach ($line in $lines) {
    $parts = $line -split ",", 3
    echo $parts
    $taskName = $parts[0].Trim()
    $time = $parts[1].Trim()
    $path = $parts[2].Trim()
    powershell -File $schedular -TaskName  $taskName -time $time -fileNameToExecute $path
}