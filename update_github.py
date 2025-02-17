#!/usr/bin/env python3

"""
Script Name: update_git_website.py

Description:
This script automates the process of updating a GitHub repository for a website.
It performs the following steps:
1. Updates the remote URL of the GitHub repository to use the SSH protocol.
2. Copies an updated HTML file (index.html) from a source directory to the target GitHub repository directory.
3. Stages any new changes in the repository.
4. Commits the changes with a pre-defined commit message, if there are any changes.
5. Pushes the committed changes to the remote repository on GitHub.

Additional Features:
- Logs all operations and errors to a 'logs/commit.log' file in the script's directory.
- Skips the commit step gracefully if there are no changes to commit.
- Handles errors during the Git operations and logs them appropriately.

Usage:
- Ensure you have an SSH key configured for GitHub and update the `GIT_SSH_COMMAND` environment variable if needed.
- Make sure the source file path and destination repository path are correct.

Author: [Your Name]
Date: [Date]

"""

import os
import subprocess
import shutil
import logging
from datetime import datetime

# Create logs directory if it does not exist
LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "commit.log")

# Configure logging to both file and console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

# Set GIT_SSH_COMMAND to use your SSH key
os.environ['GIT_SSH_COMMAND'] = 'ssh -i ~/.ssh/id_ed25519'


def update_remote_url():
    try:
        # Update the remote URL to SSH format
        subprocess.run(
            ["git", "remote", "set-url", "origin", "git@github.com:matt0164/matt0164.github.io.git"],
            check=True
        )
        logging.info("Git remote URL updated to SSH format.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error updating remote URL: {e}")
        raise


def copy_html_file():
    source_file = '/Users/mattalevy/PycharmProjects/snow-plots/html/index.html'
    destination_file = '/Users/mattalevy/PycharmProjects/matt0164.github.io/index.html'
    try:
        shutil.copy(source_file, destination_file)
        logging.info(f"Copied {source_file} to {destination_file}")
    except Exception as e:
        logging.error(f"Error copying file: {e}")
        raise


def commit_to_github():
    # First update the remote URL to ensure SSH is being used
    update_remote_url()

    # Then, copy the HTML file before updating git
    copy_html_file()

    try:
        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)
        logging.info("Staged all changes.")

        # Check if there are any staged changes before committing
        # git diff --cached --quiet returns exit code 1 if there are changes
        status_result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            check=False
        )
        if status_result.returncode == 0:
            # No changes to commit
            logging.info("No changes to commit.")
        else:
            # Commit the changes
            subprocess.run(["git", "commit", "-m", "Automated commit"], check=True)
            logging.info("Changes committed with message 'Automated commit'.")

        # Push the changes
        subprocess.run(["git", "push"], check=True)
        logging.info("Changes successfully pushed to GitHub!")
    except subprocess.CalledProcessError as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    commit_to_github()
