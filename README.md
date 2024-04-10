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
     "repos": ["repo1", "repo2"],
     "fetchMetrics": true
   }
   ```

   > NOTE: `fetchMetrics` is optional and defaults to `false`. If set to `true`, the script will fetch additional metrics like last push, stars, and open issues for each dependency. This may take longer to run, and requires additional API calls.

   > NOTE: Be sure the repos you want to list dependencies for are public or you have access to them and they have the [dependency graph enabled](https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-graph)

2. Run the script

   ```bash
   # run the script
   python script.py
   ```

3. View the output

   View the output in `deps.md` as a markdown formatted table.

   **Sample output for this repository:**
   | Package | Github Link | Version | Org Repos | Last Push | Stars | Open Issues |
   |-----|-----|-----|-----|-----|-----|-----|
   | certifi | [certifi/python-certifi](https://github.com/certifi/python-certifi) | `= 2024.2.2` | `github-deps` | 2024-04-01 | 758 | 4 |
   | charset-normalizer | [Ousret/charset_normalizer](https://github.com/Ousret/charset_normalizer) | `= 3.3.2` | `github-deps` | 2024-04-08 | 514 | 8 |
   | diskcache | [Baughn/python-diskcache](https://github.com/Baughn/python-diskcache) | `= 5.6.3` | `github-deps` | 2023-04-17 | 0 | 1 |
   | idna | [kjd/idna](https://github.com/kjd/idna) | `= 3.6` | `github-deps` | 2024-04-02 | 234 | 5 |
   | python-dotenv | [theskumar/python-dotenv](https://github.com/theskumar/python-dotenv) | `= 1.0.1` | `github-deps` | 2024-04-08 | 7048 | 57 |
   | pyyaml | [yaml/pyyaml](https://github.com/yaml/pyyaml) | `= 6.0.1` | `github-deps` | 2024-03-19 | 2416 | 282 |
   | requests | [psf/requests](https://github.com/psf/requests) | `= 2.31.0` | `github-deps` | 2024-04-08 | 51288 | 273 |
   | tomark | [codazoda/tomark](https://github.com/codazoda/tomark) | `= 0.1.4` | `github-deps` | 2023-08-24 | 15 | 1 |
   | urllib3 | [urllib3/urllib3](https://github.com/urllib3/urllib3) | `= 2.2.1` | `github-deps` | 2024-04-07 | 3657 | 139 |
   | xkcd2347 | [edsu/xkcd2347](https://github.com/edsu/xkcd2347) | `= 0.0.4` | `github-deps` | 2021-06-17 | 13 | 2 |
