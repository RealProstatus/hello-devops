#!/usr/bin/env python3

import requests


def make_request(url):
    print(f"\nОтправляем запрос на {url}")

    try:
        response = requests.get(url, timeout = 5)
        status_code = response.status_code

        if 100 <= status_code < 400:
            print(f"Response {status_code}: {response.text}")
        elif 400 <= status_code < 600:
            raise Exception(f"Error {status_code}: {response.text}")
        else:
            print(f"Unexpected status code: {status_code}")
    except Exception as e:
        print(f"Exception occurred: {e}")


if __name__ == "__main__":

    urls = [
        "https://httpstat.us/200",
        "https://httpstat.us/201",
        "https://httpstat.us/301",
        "https://httpstat.us/404",
        "https://httpstat.us/500"
    ]

    for url in urls:
        make_request(url)

