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
    google_resolver = f'https://8.8.8.8/resolve?name={hostname}&type={dns_type}'

    try:
        # Make the request
        response = requests.get(google_resolver, verify=False, proxies=proxies)

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

    hostname = "microsoft.com"
    # Use query_type of "AAAA" for IPv6
    query_type = "A"
    google_doh(hostname, query_type)


if __name__ == '__main__':
    main()
