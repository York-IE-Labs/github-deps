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

   ```json
   {
     "organization": "your_organization",
     "repos": ["repo1", "repo2"]
   }
   ```

   > NOTE: Be sure the repos you want to list dependencies for are public or you have access to them and they have the [dependency graph enabled](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph)

2. Run the script

   ```bash
   # run the script
   python script.py
   ```

3. View the output

   View the output in `deps.md` as a markdown formatted table.

   **Sample output for this repository:**
   | Package | Github Link | Version | Stellar Menu Repos |
   |-----|-----|-----|-----|
   | certifi | [certifi/python-certifi](https://github.com/certifi/python-certifi) | `= 2024.2.2` | `github-deps` |
   | charset-normalizer | [Ousret/charset_normalizer](https://github.com/Ousret/charset_normalizer) | `= 3.3.2` | `github-deps` |
   | diskcache | [Baughn/python-diskcache](https://github.com/Baughn/python-diskcache) | `= 5.6.3` | `github-deps` |
   | idna | [kjd/idna](https://github.com/kjd/idna) | `= 3.6` | `github-deps` |
   | python-dotenv | [theskumar/python-dotenv](https://github.com/theskumar/python-dotenv) | `= 1.0.1` | `github-deps` |
   | pyyaml | [yaml/pyyaml](https://github.com/yaml/pyyaml) | `= 6.0.1` | `github-deps` |
   | requests | [psf/requests](https://github.com/psf/requests) | `= 2.31.0` | `github-deps` |
   | tomark | [codazoda/tomark](https://github.com/codazoda/tomark) | `= 0.1.4` | `github-deps` |
   | urllib3 | [urllib3/urllib3](https://github.com/urllib3/urllib3) | `= 2.2.1` | `github-deps` |
   | xkcd2347 | [edsu/xkcd2347](https://github.com/edsu/xkcd2347) | `= 0.0.4` | `github-deps` |
