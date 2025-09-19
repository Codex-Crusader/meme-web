# Daily Meme Website

A fully automated meme website that fetches and displays fresh memes daily using GitHub Actions.

---

## Features

- **Daily Meme Updates**: Automatically fetches 5 new memes every day
- **Responsive UI**: Clean, modern interface that works on mobile and desktop
- **Interactive Gallery**: Memes display in a horizontally scrollable gallery
- **Lightbox View**: Click/tap any meme to open an enlarged view with navigation
- **GitHub Pages Integration**: Automatically publishes to GitHub Pages
- **Completely Automated**: Set it and forget it - runs on a schedule

---

## How It Works

The project follows a simple automated workflow:

1. **Fetch Memes**: `fetch_meme.py` retrieves 5 unique memes from the meme API
2. **Generate Site**: `generate_site.py` builds a responsive HTML page with the memes
3. **Publish**: The GitHub Actions workflow deploys the site to GitHub Pages
4. **Schedule**: This process repeats daily at 6:00 UTC

---

## Installation

### Prerequisites
- Python 3.11 or higher
- Git

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/meme-web.git
   cd meme-web
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Local Development

To test locally:

1. Fetch today's memes:
   ```bash
   python fetch_meme.py
   ```

2. Generate the website:
   ```bash
   python generate_site.py
   ```

3. Open `site/index.html` in your browser to view the result
---
### Manual Deployment

You can manually trigger the GitHub Actions workflow to publish the site:

1. Go to your repository on GitHub
2. Navigate to the Actions tab
3. Select "Daily Meme Publish"
4. Click "Run workflow"
---
## Automated Deployment

The project is configured to automatically run every day at 6:00 UTC using GitHub Actions:

1. The workflow is defined in `.github/workflows/daily.yml`
2. It runs the fetch and generate scripts
3. It publishes the result to the `gh-pages` branch
4. GitHub Pages serves the content from this branch

---

## Step-by-Step Automation Guide

Follow these steps to set up complete automation for your meme website:

### 1. Fork or Clone the Repository

Start by forking this repository to your GitHub account or clone and push to a new repository.

### 2. Enable GitHub Actions

1. Go to your repository on GitHub
2. Click on the "Actions" tab
3. If prompted, click "I understand my workflows, go ahead and enable them"

### 3. Set Up GitHub Pages

1. Go to your repository's "Settings" tab
2. In the left sidebar, click on "Pages"
3. Under "Source", select "Deploy from a branch"
4. Under "Branch", select "gh-pages" and "/ (root)"
5. Click "Save"

### 4. Configure Repository Settings (Optional)

For better security and automation:

1. Go to "Settings" → "Actions" → "General"
2. Under "Workflow permissions":
   - Select "Read and write permissions"
   - Check "Allow GitHub Actions to create and approve pull requests"
3. Click "Save"

### 5. Trigger Your First Deployment

1. Go to the "Actions" tab
2. Click on the "Daily Meme Publish" workflow
3. Click "Run workflow" → "Run workflow"
4. Wait for the workflow to complete (typically 1-2 minutes)

### 6. Verify Your Deployment

1. Go back to "Settings" → "Pages"
2. You should see a message like "Your site is published at https://yourusername.github.io/repo-name/"
3. Click on the link to view your deployed meme website

### 7. Verify Scheduled Runs

1. The site will automatically update daily at 6:00 UTC
2. You can check the "Actions" tab to see the history of workflow runs
3. Each successful run will update your website with fresh memes

---

## Local Testing Guide

To run and test this project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/meme-web.git
cd meme-web
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Fetch Today's Memes

```bash
python fetch_meme.py
```

This will:
- Create a `memes` directory if it doesn't exist
- Fetch 5 unique memes from the API
- Save them as a JSON file named with today's date (e.g., `memes/2023-11-22.json`)

### 5. Generate the Website

```bash
python generate_site.py
```

This will:
- Create a `site` directory if it doesn't exist
- Generate an `index.html` file with today's memes

### 6. View the Website Locally

Open the generated HTML file in your browser:

```bash
# On Windows
start site\index.html

# On macOS
open site/index.html

# On Linux
xdg-open site/index.html
```

Alternatively, you can navigate to the `site` directory and open `index.html` manually in your browser.

### 7. Testing the Full Workflow (Optional)

To test the entire workflow including publishing (without actually pushing to GitHub):

```bash
# Set environment variables (Windows)
set GIT_REMOTE=origin
set GIT_BRANCH=test-branch
set COMMITTER_NAME=Test User
set COMMITTER_EMAIL=test@example.com

# Set environment variables (macOS/Linux)
export GIT_REMOTE=origin
export GIT_BRANCH=test-branch
export COMMITTER_NAME="Test User"
export COMMITTER_EMAIL=test@example.com

# Run the publish script with the dry-run flag
python publish.py --dry-run
```

### Troubleshooting

- **API Rate Limits**: The meme API may have rate limits. If you see errors, wait a few minutes and try again.
- **Missing Images**: Some memes might fail to load due to their source being removed or temporary network issues.
- **Permissions Issues**: Make sure you have write permissions for the project directory.
- **Python Version**: This project requires Python 3.11+. Check your version with `python --version`.

---

## Troubleshooting

- **Workflow failing?** Check that your `requirements.txt` contains all dependencies.
- **Pages not updating?** Make sure GitHub Pages is configured to deploy from the `gh-pages` branch.
- **API rate limits?** The meme API has rate limits - check workflow logs for details.

---

## Project Structure

- `fetch_meme.py` - Fetches memes from the API and saves as JSON
- `generate_site.py` - Creates the HTML site from the fetched memes
- `publish.py` - Alternative manual publishing script
- `.github/workflows/daily.yml` - GitHub Actions workflow definition
- `memes/` - Directory where daily meme data is stored
- `site/` - Output directory for the generated website
- `requirements.txt` - Python dependencies

---

## Configuration

You can modify these settings:

- In `fetch_meme.py`:
  - `MEME_COUNT`: Number of memes to fetch each day (default: 5)
  
- In `.github/workflows/daily.yml`:
  - `cron`: Schedule timing (default: "0 6 * * *" - 6:00 UTC daily)

---

## Security Note

The GitHub workflow uses the `GITHUB_TOKEN` which is automatically provided by GitHub Actions - no additional secrets need to be configured.

**Dependency Security**: This project uses requests ≥2.32.0 to address CVE-2024-35195 (Always-Incorrect Control Flow Implementation vulnerability).

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

---

## License

This project is open source and available under the MIT License.

---

Made with love, Fork me on GitHub
Thank you for reading.

