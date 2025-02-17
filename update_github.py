import subprocess
import logging
import os
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def run_command(command, check=True, capture_output=False):
    """
    Run a shell command and return the result.
    Provides error handling and logging for subprocesses.
    """
    try:
        logging.info(f"Running command: {' '.join(command)}")
        result = subprocess.run(command, check=check, capture_output=capture_output, text=True)
        if capture_output:
            return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Command '{' '.join(command)}' failed with error: {e}")
        sys.exit(1)  # Exit the script if a command fails


def check_git_directory():
    """
    Check if the current directory is a Git repository.
    """
    if not os.path.exists(".git"):
        logging.error("This directory is not a Git repository.")
        sys.exit(1)


def stage_changes():
    """
    Stage all changes in the repository.
    """
    run_command(["git", "add", "."])
    logging.info("Staged all changes.")


def commit_changes():
    """
    Commit changes if there are staged changes.
    """
    # Check if there are staged changes
    status_result = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if status_result.returncode == 0:
        logging.info("No changes to commit.")
    else:
        # Commit the staged changes
        run_command(["git", "commit", "-m", "Automated commit"])
        logging.info("Committed changes with message 'Automated commit'.")


def push_changes():
    """
    Force push committed changes to the remote repository.
    This will override remote changes with local changes.
    """
    try:
        run_command(["git", "push", "--force"])
        logging.info("Force push executed successfully!")
    except subprocess.CalledProcessError:
        logging.error("Force push failed. Please check your repository permissions or remote configuration.")
        sys.exit(1)


def handle_unstaged_changes():
    """
    Automatically detect and handle unstaged changes.
    Always stages and commits the changes (no user input required).
    """
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if result.stdout:
        logging.info("Unstaged changes detected. Automatically staging and committing them.")
        stage_changes()  # Stage all changes
        commit_changes()  # Commit those changes
    else:
        logging.info("No unstaged changes found. Proceeding.")


def main():
    """
    Automates the Git workflow: staging, committing, and force pushing local changes.
    """
    try:
        # Ensure the script is run in a Git repository
        check_git_directory()

        # Handle unstaged changes automatically
        handle_unstaged_changes()

        # Force push changes to the remote repository (local changes always win)
        push_changes()

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
