import xkcd2347
import json
from tomark import Tomark
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get GitHub API key
GITHUB_API_KEY = os.getenv('GITHUB_API_KEY')

# Exit if no key is found
if GITHUB_API_KEY is None:
   print("No GitHub API key found. Please add it to your .env file")
   exit()

# Create GitHub object
gh = xkcd2347.GitHub(key=GITHUB_API_KEY)

# Load config file
f = open('config.json')
data = json.load(f)

# Get config values
REPOS = data['repos']
ORGANIZATION = data['organization']
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
               'version': dep['requirements'],
               'repos': []
            }
      
      # If not already added to repos
      if repo not in dependencyMap[nameWithOwner]['repos']:
         dependencyMap[nameWithOwner]['repos'].append(repo)

# Create a list of dependencies
for key in dependencyMap:
   # Turn `repos` into a string. surround the repo names with backticks
   repos = dependencyMap[key]['repos']
   reposStr = ', '.join([f'`{r}`' for r in repos])

   # Add to list
   dependencies.append({
         'Package': dependencyMap[key]['package'],
         'Github Link': dependencyMap[key]['github'],
         'Version': f"`{dependencyMap[key]['version']}`",
         'Stellar Menu Repos': reposStr
      })

# Sort dependencies by package name
sortedDeps = sorted(dependencies, key=lambda d: d['Package'])

# Create markdown table
markdown = Tomark.table(sortedDeps)

# Write markdown to file
f = open("deps.md", "w")
f.write(markdown)
f.close()