# manage_librem_battery

sudo systemctl daemon-reload
sudo systemctl enable manage_librem_battery.service


sudo systemctl start manage_librem_battery


sudo cp manage_librem_battery.py /usr/bin/manage_librem_battery.py
sudo cp manage_librem_battery.service /etc/systemd/system/manage_librem_battery.service