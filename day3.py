from dotenv import load_dotenv
import os
import requests
import json

usernames_str = os.getenv("GITHUB_USERNAMES")
usernames = usernames_str.split(",")


load_dotenv()
def get_github_user_summary(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        return {
            "name": data.get("name"),
            "public_repos": data.get("public_repos"),
            "followers": data.get("followers"),
            "following": data.get("following"),
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {username}: {e}")
        return None
    

all_summaries = []
for username in usernames:
    summary = get_github_user_summary(username)
    if summary:
        all_summaries.append(summary)
        print(f"{summary['name']} has {summary['public_repos']} public repos, {summary['followers']} followers, and is following {summary['following']} people.")

with open("github_summaries.json", "w") as f:
    json.dump(all_summaries, f, indent=2)

print("All summaries have been saved to github_summaries.json")