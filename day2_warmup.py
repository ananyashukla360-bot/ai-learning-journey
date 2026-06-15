#hungry for more so lets go
import json

person = {"name": "Alex", "age": 25, "skills": ["python", "sql"]}

# Python dict -> JSON string
json_string = json.dumps(person)

# {"name": "Alex", "age": 25, "skills": ["python", "sql"]}

# JSON string -> Python dict
back_to_dict = json.loads(json_string)



people = [
    {"name": "Alex", "age": 25, "skills": ["python", "sql"]},
    {"name": "Sam", "age": 30, "skills": ["python", "react"]},
    {"name": "Jordan", "age": 22, "skills": ["java", "sql"]}
]
print(json.dumps(people, indent=2))

with open("data.json", "w") as f:
    json.dump(people,f,indent =2 )

with open("data.json", "r") as f:
    data = json.load(f)



import requests

def get_github_user_summary(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    data = response.json()
    return {
        "name": data.get("name"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "following": data.get("following"),
    }

usernames = ["octocat", "torvalds", "mojombo"]
for username in usernames:
    summary = get_github_user_summary(username)
    print(f"Summary for {username}:")
    print(summary)
    print()








