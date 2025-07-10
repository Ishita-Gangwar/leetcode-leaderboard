import requests
import json

usernames = ["leetcode_user1", "leetcode_user2"]  # Replace with actual usernames

def get_user_data(username):
    url = f"https://leetcode-stats-api.herokuapp.com/{username}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return {
            "username": username,
            "totalSolved": data.get("totalSolved", 0),
            "easySolved": data.get("easySolved", 0),
            "mediumSolved": data.get("mediumSolved", 0),
            "hardSolved": data.get("hardSolved", 0),
            "contestRating": data.get("contestRating", 0)
        }
    else:
        return {"username": username, "error": "User not found"}

all_data = [get_user_data(user) for user in usernames]

with open("leaderboard.json", "w") as f:
    json.dump(all_data, f, indent=4)

print("Leaderboard updated successfully.")
