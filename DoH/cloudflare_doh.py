import requests
import json
import urllib3


urllib3.disable_warnings()

proxies = {
    "http": "http://127.0.0.1:9000",
    "https": "http://127.0.0.1:9000",
}


def cloudflare_doh(hostname,query_type):

    # Use the correct DoH URL for Cloudflare's DNS resolver
    cloudflare_resolver = f'https://1.1.1.1/dns-query?name={hostname}&type={query_type}'

    headers = {
        "accept": "application/dns-json"
    }

    try:
        # Make the request
        response = requests.get(cloudflare_resolver, verify=False, proxies=proxies, headers=headers)

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
    # use query_type of "A" for IPv4
    query_type = "AAAA"
    cloudflare_doh(hostname, query_type)

if __name__ == '__main__':
    main()
