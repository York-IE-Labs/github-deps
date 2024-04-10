# github-deps

List all dependencies of a GitHub repository, outputs to markdown file

## Getting Started

Pull the repository and install the dependencies:

```bash
# setup virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# create .env file with GITHUB_API_KEY
echo "GITHUB_API_KEY=your_github_api_key" > .env
```

## Usage

1. Update `config.json` with the organization and list of repos you want to list dependencies for.

   ````json
   {
   "organization": "your_organization",
   "repos": [
      "repo1",
      "repo2"
   ]
   }
   ```

   ````

2. Run the script

   ```bash
   # run the script
   python script.py
   ```

3. View the output

   View the output in `deps.md` as a markdown formatted table.
