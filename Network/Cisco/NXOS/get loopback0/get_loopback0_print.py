import csv
import getpass
import time
import os
from netmiko import ConnectHandler


# Read the device file
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


# Run show command on target device
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


# Extract the information of vrf and ip address from the input data
def get_vrf_ip_address(data):
    # Initiate default value for vrf as 'default' and ip_address as ''
    vrf = 'default'
    ip_address = ''

    for line in data.strip().splitlines():
        # line contains vrf information will have format of 'vrf member vrf_name'
        if 'vrf' in line:
            vrf = line.strip().split(' ')[2]
        # line contains ip address information will have format of 'ip address ip_address'
        if 'ip address' in line:
            ip_address = line.strip().split(' ')[2]

    return vrf, ip_address


def main():

    # Load and Read the devices from the text file
    device_file = 'devices.txt'

    devices = read_device_file(device_file)

    # Enter credentials to access the devices
    acc_user = input('username:')
    acc_password = getpass.getpass()

    # show commands to run
    command = 'show run int loopback0'

    # Print column headers
    print(f"{'Hostname':<20} {'Loopback0':<30} {'VRF':<10}")

    # Loop through the device list
    for device in devices:
        ip = device['IP']
        name = device['Name']
        username = acc_user
        password = acc_password

        # Get the "show run int loopback0" output
        output = get_show_command(ip, username, password, command)

        # Check if the connection to target devices is successful or not
        if 'Failed' in output:
            print(f"{name:<20} {'Failed to connect':<30} {'Failed to connect':<10}")
        else:
            vrf, ip_address = get_vrf_ip_address(output)
            print(f"{name:<20} {ip_address:<30} {vrf:<10}")

        time.sleep(1)


if __name__ == '__main__':
    main()
