import os
import sys
import requests

GITHUB_USER = "lilscorfy"

def check_following(username):
    url = f"https://api.github.com/users/{username}/following"
    headers = {"Accept": "application/vnd.github.v3+json"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            following = [user["login"] for user in response.json()]
            return GITHUB_USER in following
        else:
            print(f"Error: {response.json().get('message', 'Unknown error')}")
            return False
    except requests.RequestException:
        print("Failed to connect to GitHub. Please check your internet connection.")
        return False

def main():
    print("\n\033[1;32mWelcome to WEBDEV Installer!\033[0m")
    username = input("Enter your GitHub username: ").strip()

    if username.lower() == GITHUB_USER.lower():
        print("\033[1;32mYou are the owner. Skipping verification...\033[0m")
    elif not check_following(username):
        print(f"\033[1;31mYou are not following @{GITHUB_USER} on GitHub. Please follow and try again.\033[0m")
        sys.exit(1)
    
    print("\033[1;32mVerification complete! Installing WEBDEV...\033[0m")
    
    # Install dependencies
    os.system("pip install -r requirements.txt")

    print("\033[1;32mInstallation successful! Run 'python webdev.py' to start WEBDEV.\033[0m")

if __name__ == "__main__":
    main()
