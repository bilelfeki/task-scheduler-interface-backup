
# PowerShell Task Scheduler with Pygubu

This Python project provides a graphical interface for scheduling PowerShell scripts as tasks. It leverages the Pygubu GUI builder to create an easy-to-use interface for scheduling tasks with specified names, execution times, and script paths.


## Demo

Here’s a demo of the Task Scheduler in action:

![Task Scheduler Demo](https://github.com/bilelfeki/task-scheduler-interface-backup/blob/master/demo/demo-schedular.gif)

## Features

- Schedule PowerShell scripts using a simple graphical interface.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Tkinter (for GUI)
- Pygubu (`pip install pygubu`)
- PowerShell (installed on Windows by default)

4. Fill in the following fields in the GUI:
   - **Task Name**: The name of the scheduled task.
   - **Time**: The time to run the PowerShell script (format: HH:MM AM/PM).
   - **Script Location**: Path to the PowerShell script file.

5. Click the **Schedule** button to schedule the task.

## Example

- Task Name: `BackupScript`
- Time: `8:05 AM`
- Script Location: `C:\Scripts\backup.ps1`

## Main UI Components

- **Task Name**: Text input for the task name.
- **Time**: Text input for setting the execution time.
- **Script Location**: File chooser to select the PowerShell script.
- **Schedule Button**: Button to schedule the task.

## License

This project is licensed under the MIT License.
