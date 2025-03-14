import csv
import getpass
import time
import os
from netmiko import ConnectHandler


# Create a function to parse the text file
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


# Create a connection function
def get_show_command(ip, username, password, command):
    # Device details for Netmiko
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

    # Load the text file
    device_file = 'devices.txt'

    # Read the devices from the text file
    devices = read_device_file(device_file)

    acc_user = input('username:')
    acc_password = getpass.getpass()

    # A prefix to be checked (replace 'prefix' with an actual prefix - could be A.B.C.D or A.B.C.D/LEN)
    prefix = 'prefix'
    
    # In case of route lookup in a specific VRF, replace 'vrf_name' with an actual vrf name. For example, if vrf name is 'production', then the value of vrf_option variable is 'vrf production' 
    # In case of route lookup in the default global VRF, replace 'vrf vrf_name' with ''.
    vrf_option = 'vrf vrf_name'

    # show commands to run
    command = f'show ip route {prefix} {vrf_option}'

    # Loop through the device list
    for device in devices:
        ip = device['IP']
        name = device['Name']
        username = acc_user
        password = acc_password

        # Print the IP address of each device
        print(f"Device: {ip} - {name}")

        # Get the "show" output
        output = get_show_command(ip, username, password, command)

        # Write output to a new text file named after the device IP
        folder_path = ("results")
        file_name = f"{name}.txt"

        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'w') as file:
            file.write(output)

        time.sleep(1)

    print("Script completed. Output saved in text files for each device.")


if __name__ == '__main__':
    main()
