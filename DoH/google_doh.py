import requests
import json
import urllib3


urllib3.disable_warnings()

proxies = {
    "http": "http://127.0.0.1:9000",
    "https": "http://127.0.0.1:9000",
}


def google_doh(hostname, dns_type):

    # Use the correct DoH URL for Google's DNS resolver
    doh = f'https://8.8.8.8/resolve?name={hostname}&type={dns_type}'

    try:
        # Make the request
        response = requests.get(doh, verify=False, proxies=proxies)

        # Check if the response was successful
        if response.status_code == 200:
            # Print the JSON response
            print(json.dumps(response.json(), indent=1))
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.Timeout:
        print("The request timed out")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")


def main():

    # hostname = "ip-ranges.amazonaws.com"
    hostname = "microsoft.com"
    query_type = "A"
    google_doh(hostname, query_type)


if __name__ == '__main__':
    main()
