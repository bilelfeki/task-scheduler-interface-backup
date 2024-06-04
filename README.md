## Backup System using GitHub Repositories

This backup system is designed to automate the process of backing up GitHub private repositories by comparing commits between a working repository and a dedicated backup repository. The system is implemented using PowerShell scripting and leverages GitLog for extracting and comparing commit logs.

### How it Works

1. **Commit Comparison**: The system checks all commits in the working repository and compares them with the commits in the backup repository.
2. **Update or Notification**: If the last commit in the backup repository matches the latest commit in the working repository, the backup repository is updated. Otherwise, a notification is sent to the user.
3. **Notification**: Notifications are sent using Windows libraries to inform the user of any updates or discrepancies between the repositories.


### Dependencies

- PowerShell
- GitLog
- Windows libraries for notifications
- Tkinter
- pygubu

### Usage

- This backup system is suitable for individuals or teams working with GitHub private repositories who want an automated backup solution.
- Customize the script according to specific repository setups or notification preferences.
