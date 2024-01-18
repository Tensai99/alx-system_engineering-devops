#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        if response.status_code == 404:
            return 0

        results = response.json().get("data")
        return results.get("subscribers")

    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return 0

if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name: ")
    subscribers = number_of_subscribers(subreddit_name)
    print(f"The subreddit {subreddit_name} has {subscribers} subscribers.")

