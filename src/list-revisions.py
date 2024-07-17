# Uses the GitHub API to list all the revisions of langchain-al/langchain and its components.

REQUEST_HEADERS = { "Accept" : "application/vnd.github+json",  "X-GitHub-Api-Version" : "2022-11-28"}
GITHUB_API_URL = "https://api.github.com/repos/langchain-ai/langchain/releases"
PARAMS = { "per_page" : 100 }

import json
import requests

def get_revisions():
    response = requests.get(GITHUB_API_URL, headers=REQUEST_HEADERS, params=PARAMS)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
revisions = get_revisions()

latest_releases = {}

if revisions:
    for revision in revisions:
      entry = revision["tag_name"]            # e.g. "langchain==0.1.0"
      package, version = entry.split("==")
      if package not in latest_releases:
          latest_releases[package] = version
    for package in sorted(latest_releases.keys()):
        print(f"{package}: {latest_releases[package]}")
else:
    print("Failed to get revisions")


