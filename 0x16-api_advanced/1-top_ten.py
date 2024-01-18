#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        if response.status_code == 404:
            print("None")
            return

        results = response.json().get("data")
        posts = results.get("children")
        
        for post in posts:
            title = post.get("data").get("title")
            print(title)

    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")

if __name__ == "__main__":
    subreddit_name = input("Enter the subreddit name: ")
    top_ten(subreddit_name)

