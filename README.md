# Manage Librem Battery

## Introduction
Manage Librem Battery is a utility designed for Librem 5 smartphones to help users optimize battery life by controlling charging behavior. This tool allows the battery charge to toggle on and off based on predefined thresholds to extend battery health and efficiency.

## Getting Started

### Prerequisites
Before installing the Manage Librem Battery service, ensure you have `git` installed on your device to pull the latest version of the script.

### Installation
Follow these steps to install and set up the Manage Librem Battery service on your Librem 5:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/alivellani/manage_librem_battery.git
   cd manage_librem_battery
   ```

2. **Install the service:**
   Copy the service and script files into the appropriate system directories.
   ```bash
   sudo cp manage_librem_battery.service /etc/systemd/system/manage_librem_battery.service
   sudo cp manage_librem_battery.py /usr/bin/manage_librem_battery.py
   ```

3. **Reload systemd:**
   Inform systemd that a new service file exists.
   ```bash
   sudo systemctl daemon-reload
   ```

4. **Enable the service:**
   Enable the service to start at boot.
   ```bash
   sudo systemctl enable manage_librem_battery.service
   ```

5. **Start the service:**
   Start the service immediately.
   ```bash
   sudo systemctl start manage_librem_battery.service
   ```

## Usage
Once installed, the Manage Librem Battery service will automatically monitor your device's battery level and adjust the charging state based on the set thresholds. The service runs in the background without needing further interaction.

## Contributing
Contributions to the Manage Librem Battery project are welcome. Please feel free to fork the repository, make improvements, and submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
This software comes with no warranty. You are responsible for reviewing the code and ensuring it meets your needs. The author is not responsible for any damage that may occur due to the use of this utility.
```
