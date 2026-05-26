import os
import requests
from colorama import Fore, Style, init
from pyfiglet import Figlet

# Initialize colorama
init(autoreset=True)

# Display ASCII Banner
fig = Figlet(font='slant')
print(Fore.GREEN + fig.renderText("JAYDEN969"))

# Disclaimer and Support Info
print(Fore.YELLOW + "=" * 60)
print(Fore.GREEN + "Disclaimer: This tool and all repositories are provided for")
print(Fore.GREEN + "educational purposes only. Use them at your own risk.")
print(Fore.YELLOW + "=" * 60)
print(Fore.CYAN + "TOOLS KIT - 2026 \n")

# ==========================
# GITHUB USERS
# ==========================
GITHUB_USERS = {
    "1": "Jayden-969",
}

print(Fore.YELLOW + "\nSelect GitHub User:\n")

for key, user in GITHUB_USERS.items():
    print(
        Fore.CYAN +
        f"[{key}] " +
        Fore.WHITE +
        user
    )

choice_user = input(
    Fore.YELLOW +
    "\nSelect option: "
).strip()

if choice_user not in GITHUB_USERS:
    print(Fore.RED + "Invalid option")
    exit()

GITHUB_USER = GITHUB_USERS[choice_user]

print(
    Fore.GREEN +
    f"\n[+] Selected: {GITHUB_USER}\n"
)

# ==========================
# FETCH REPOSITORIES
# ==========================
url = (
    f"https://api.github.com/users/"
    f"{GITHUB_USER}/repos"
)

response = requests.get(
    url,
    timeout=15
)

if response.status_code != 200:
    print(Fore.RED + "Error fetching repository list. Please check your internet connection or username.")
    exit()

repos = response.json()

if not repos:
    print(Fore.RED + "No public repositories found for this user.")
    exit()

# Display all available repositories
print(Fore.YELLOW + "\nAvailable Repositories:\n")
for idx, repo in enumerate(repos, 1):
    print(Fore.LIGHTYELLOW_EX + f"[{idx}] {repo['name']}")
    desc = repo['description'] if repo['description'] else "No description available"
    print(Fore.GREEN + f"     ↳ {desc}\n")

# User Selection
print(Fore.YELLOW + "Options:")
print(Fore.CYAN + "  - Enter repo numbers separated by commas (e.g., 1,3,5)")
print(Fore.CYAN + "  - Enter 'all' to clone all repositories\n")

choice = input(Fore.LIGHTYELLOW_EX + "Enter your choice: ").strip().lower()

# Determine repos to clone
to_clone = []

if choice == "all":
    to_clone = [repo["clone_url"] for repo in repos]
else:
    try:
        indexes = [int(x.strip()) for x in choice.split(",")]
        for i in indexes:
            if 1 <= i <= len(repos):
                to_clone.append(repos[i - 1]["clone_url"])
            else:
                print(Fore.RED + f"Invalid index: {i}")
    except ValueError:
        print(Fore.RED + "Invalid input format. Please enter numbers or 'all'.")
        exit()

# Clone selected repos
if not to_clone:
    print(Fore.RED + "No repositories selected for cloning.")
    exit()

print(Fore.YELLOW + "\nStarting cloning process...\n")

for repo_url in to_clone:
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    print(Fore.GREEN + f"Cloning {repo_name} ...")
    os.system(f"git clone {repo_url}")

print(Fore.CYAN + "\nAll selected repositories have been cloned successfully!")
print(Fore.YELLOW + "Thank you for using Jayden969 Toolkit 1.0 🚀")
