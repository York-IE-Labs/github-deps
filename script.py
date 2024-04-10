import xkcd2347
import json
from tomark import Tomark
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get GitHub API key
GITHUB_API_KEY = os.getenv('GITHUB_API_KEY')

# Exit if no key is found
if GITHUB_API_KEY is None:
   print("No GitHub API key found. Please add it to your .env file")
   exit()

# Create requests session
client = requests.Session()
client.headers.update({'Accept': 'application/vnd.github+json', 'Authorization': f'Bearer {GITHUB_API_KEY}', 'X-GitHub-Api-Version': '2022-11-28'})


# Create GitHub object
gh = xkcd2347.GitHub(key=GITHUB_API_KEY)

# Load config file
f = open('config.json')
data = json.load(f)

# Get config values
REPOS = data['repos']
ORGANIZATION = data['organization']
FETCH_METRICS = data['fetchMetrics']
dependencies = []
dependencyMap = {}

# Get dependencies for each repo
print(f"Getting dependencies for {len(REPOS)} repos of {ORGANIZATION}")
for repo in REPOS:
   print(f"Getting dependencies for {repo}...")
   for dep in gh.get_dependencies(ORGANIZATION, repo):
      # Get the nameWithOwner of the repo if it exists
      nameWithOwner = "No git repo found"
      repository = dep.get('repository', None)
      if repository is not None:
         nameWithOwner = repository.get('nameWithOwner', None)
      
      # Add to map if not already there
      if nameWithOwner not in dependencyMap:
         dependencyMap[nameWithOwner] = {
               'package': dep['packageName'],
               'github': f'[{nameWithOwner}](https://github.com/{nameWithOwner})',
               'nameWithOwner': nameWithOwner,
               'version': dep['requirements'],
               'repos': []
            }
      
      # If not already added to repos
      if repo not in dependencyMap[nameWithOwner]['repos']:
         # Add repo to list
         dependencyMap[nameWithOwner]['repos'].append(repo)

# Create a list of dependencies
for key in dependencyMap:
   # Turn `repos` into a string. surround the repo names with backticks
   repos = dependencyMap[key]['repos']
   reposStr = ', '.join([f'`{r}`' for r in repos])

   dependency = {
         'Package': dependencyMap[key]['package'],
         'Github Link': dependencyMap[key]['github'],
         'Version': f"`{dependencyMap[key]['version']}`",
         'Org Repos': reposStr
      }

   if nameWithOwner == "No git repo found" or not FETCH_METRICS:
      # Add to list
      dependencies.append(dependency)
      continue
   
   try:
      # Get the repo details via HTTP request
      response = client.get(f"https://api.github.com/repos/{dependencyMap[key]['nameWithOwner']}")

      # Get created_at, updated_at, pushed_at, stargazers_count, and open_issues_count and add them to 'repo'
      repoDetails = response.json()
      dependency['Last Push'] = repoDetails.get('pushed_at', '-')[0:10]
      dependency['Stars'] = repoDetails.get('stargazers_count', '-')
      dependency['Open Issues'] = repoDetails.get('open_issues_count', '-')
   except:
      print(f"Error getting repo details for {nameWithOwner}")
   
   # Add to list
   dependencies.append(dependency)

# Sort dependencies by package name
sortedDeps = sorted(dependencies, key=lambda d: d['Package'])

# Create markdown table
markdown = Tomark.table(sortedDeps)

# Write markdown to file
f = open("deps.md", "w")
f.write(markdown)
f.close()