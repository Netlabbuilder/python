import csv
import getpass
import time
import os
from netmiko import ConnectHandler


# Function to parse the "devices.txt" file
def read_device_file(file):
    devices = []
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            devices.append({
                'IP': row['IP'],
                'Name': row['Name']
            })
    return devices


# Function to connect and run a command on a target device
def get_show_command(ip, username, password, command):
  
    # Device details
    device = {
        'device_type': 'cisco_nxos',
        'host': ip,
        'username': username,
        'password': password,
    }

    # Connect and run the command
    try:
        with ConnectHandler(**device) as net_connect:
            output = net_connect.send_command(command)
            return output
    except Exception as e:
        return f"Failed to connect to {ip}: {str(e)}"


def main():

    # Load the 'devices.txt' file
    device_file = 'devices.txt'

    # Read the devices from the 'devices.txt' file
    devices = read_device_file(device_file)

    # Ask user to provide login credentials
    acc_user = input('username:')
    acc_password = getpass.getpass()

    # A show command to run
    command = 'show run'

    # Loop through the device list
    for device in devices:
        ip = device['IP']
        name = device['Name']
        username = acc_user
        password = acc_password

        # Print the IP address of each device
        print(f"Device: {ip} - {name}")

        # Get the output of show command
        output = get_show_command(ip, username, password, command)

        # Create a new folder with folder name is the show command. For example, show command is "show run", then the folder name is "show run"
        # Create a new text file named after the device Name. For example, if the device name is device_A, then new file is "device_A.txt" 
        folder_path = 'results'
        file_name = f"{name}.txt"

        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'w') as file:
            file.write(output)

        time.sleep(1)

    print("Script completed. Output saved in text files under \" {folder_path} \" for each device.")


if __name__ == '__main__':
    main()
