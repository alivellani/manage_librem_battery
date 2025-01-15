# # s/usr/bin/manage_pinephone_bat.py
# # sudo cp Documents/codes/manage_pinephone_bat/manage_pinephone_bat.py /usr/bin/manage_pinephone_bat.py

# changes for pusim


import time
from datetime import datetime
import os

#todo update this 

internal = "max170xx_battery"
external = "NA"
log_dir = "/home/purism/Documents/codes/manage_pinephone_bat/logs"

def read_battery_capacity(battery_type):
    try:
        with open(f'/sys/class/power_supply/{battery_type}/capacity', 'r') as file:
            capacity = file.read().strip()
            print(capacity)
        return int(capacity)
    except:
        return 'NA'

def read_battery_behaviour(battery_type):
    try:
        with open(f'/sys/class/power_supply/{battery_type}/status', 'r') as file:
            behaviour = file.read().strip()
        return behaviour
    except:
        return 'NA'

#todo this will need to be led state
import os

def set_charge_behaviour(value, battery_type):
    """
    Enable or disable charging behavior based on the given value.
    - Write `1` to disable charging.
    - Write `0` to enable charging.
    Only writes if the current state is different.

    Args:
        value (int): `1` to disable, `0` to enable.
        battery_type (str): Description of the battery type.
    """
    path = "/sys/class/leds/chg_en/brightness"

    try:
        # Read the current state
        with open(path, 'r') as file:
            current_value = file.read().strip()
        
        print(f"Current charging behaviour: {current_value}")

        # Only write if the desired value is different from the current value
        if current_value != str(value):
            with open(path, 'w') as file:
                file.write(f"{value}\n")
            print(f"Charging behaviour for {battery_type} changed to {value} successfully.")
        else:
            print(f"No change needed: Charging behaviour for {battery_type} is already {value}.")
    except PermissionError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"Failed to set charging behaviour for {battery_type}: {e}")




def inhibit_charge(battery_type):
    set_charge_behaviour("1", battery_type)

def enable_auto_charge(battery_type):
    set_charge_behaviour("0", battery_type)

def is_batt_at_threshold(int_bat_perc,  int_bat_beh, ext_bat_beh=None ):
    if int_bat_perc > 90:
        inhibit_charge(internal)
        print("set inhibiting charger internal")
    if int_bat_perc < 60:
        enable_auto_charge(internal)
        #print("setting auto charge intenral")

def log_battery_status(int_bat_perc, int_bat_beh, int_charger_con):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = (f"{timestamp} Behaviour internal: {int_bat_beh}, "
                 f"Battery internal: {int_bat_perc}%, "
                 f"int_charger: {int_charger_con}, \n" )
    
    log_file = os.path.join(log_dir, datetime.now().strftime('%Y-%m-%d') + ".log")
    with open(log_file, 'a') as file:
        file.write(log_entry)


def is_charger_connected(battery_type):
    try: 
        with open(f'/sys/class/power_supply/{battery_type}/charge_type', 'r') as file:
            charger = file.read().strip()
        return charger
    except:
        return 'NA'

if __name__ == "__main__":
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    #enable_auto_charge(external)
    #inhibit_charge(internal)

    while True:
        int_bat_perc = read_battery_capacity(internal)
        print(f"int_bat_perc {int_bat_perc}")
        #ext_bat_perc = read_battery_capacity(external)
        int_bat_beh = read_battery_behaviour(internal)
        
        #ext_bat_beh = read_battery_behaviour(external)
        int_charger_con = is_charger_connected(internal)
        print(f"int_charger_con {int_charger_con}")
        #ext_charger_con = is_charger_connected(external)
        log_battery_status(int_bat_perc, int_bat_beh, int_charger_con)
        is_batt_at_threshold(int_bat_perc, int_bat_beh)
        time.sleep(600)
