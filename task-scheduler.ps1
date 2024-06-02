param([string]$TaskName , [string]$time ,[string]$fileNameToExecute )

  
$filePathToExecute = $pwd.Path + '\' + $fileNameToExecute

$action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-File  $filePathToExecute" 
$trigger = New-ScheduledTaskTrigger -once -At $time
$taskFound=$false
$tasks = Get-ScheduledTask 
foreach ($task in $tasks) {
    if ($task.TaskName -eq $TaskName) {
        $taskFound=$true
    } 
}
if(!$taskFound){
    Register-ScheduledTask -Action $action -Trigger $trigger -TaskName  $TaskName
}
