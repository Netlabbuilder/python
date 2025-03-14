import urllib3
import requests
import json
from requests.auth import HTTPBasicAuth
from dnac_config import DNAC_IP, DNAC_PORT, DNAC_USER, DNAC_PASSWORD

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_auth_token():
    """
    Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    """
    # Token Endpoint URL
    url = 'https://' + DNAC_IP + '/dna/system/api/v1/auth/token'
    # Make the POST Request to get the Token
    resp = requests.post(url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD), verify=False)
    # Retrieve the Token from the returned JSON data
    token = resp.json()['Token']
    # Create a return statement to send the token back for later use
    return token


def get_device_count(token):
    """
    Building out function to retrieve the number of devices. Using requests.get to make a call to the device count Endpoint
    """
    # Device_Count Endpoint URL
    url = 'https://' + DNAC_IP + '/dna/intent/api/v1/network-device/count'
    # Header data for GET Request
    hdr = {'x-auth-token': token,
           'content-type': 'application/json'}
    # Make the Get Request to get the number of devices
    resp = requests.get(url, headers=hdr, verify=False)

    if resp.status_code != 200:
        return resp.text
    else:
        return resp.json()


def get_device_list(token):
    """
    Building out function to retrieve list of devices. Using requests.get to make a call to the network device Endpoint
    """
    # Network-Device Endpoint URL
    url = 'https://' + DNAC_IP + '/dna/intent/api/v1/network-device'
    # Header data for GET Request
    hdr = {'x-auth-token': token,
           'content-type': 'application/json'}
    # Make the Get Request to get network-device list
    resp = requests.get(url, headers=hdr, verify=False)

    if resp.status_code != 200:
        return resp.text
    else:
        return resp.json()


if __name__ == '__main__':

    # Get Token by calling get_auth_token()
    token = get_auth_token()

    # Get Device List by calling get_auth_token()
    device_count_result = get_device_count(token)

    print(f'Output from from device_count API call: {device_count_result}')

    if 'response' in device_count_result:
        print(f"Total number of devices: {device_count_result['response']}")
    else:
        print(f"This API cannot get the device list from DNAC due to this error: {device_count_result}")

    # Get Device List by calling get_auth_token()
    device_list_result = get_device_list(token)

    if 'response' in device_list_result:
        print((json.dumps(device_list_result['response'], indent=2)))
    else:
        print(f"This API cannot get the device list from DNAC due to this error: {device_list_result}")
