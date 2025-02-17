import os
import subprocess
import shutil

# Set GIT_SSH_COMMAND to use your SSH key
os.environ['GIT_SSH_COMMAND'] = 'ssh -i /Users/mattalevy/PycharmProjects/snow-plots/id_ed25519'

def update_remote_url():
    try:
        # Update the remote URL to SSH format
        subprocess.run(
            ["git", "remote", "set-url", "origin", "git@github.com:matt0164/matt0164.github.io.git"],
            check=True
        )
        print("Git remote URL updated to SSH format.")
    except subprocess.CalledProcessError as e:
        print(f"Error updating remote URL: {e}")
        raise


def copy_html_file():
    source_file = '/Users/mattalevy/PycharmProjects/snow-plots/html/index.html'
    destination_file = '/Users/mattalevy/PycharmProjects/matt0164.github.io/index.html'
    try:
        shutil.copy(source_file, destination_file)
        print(f"Copied {source_file} to {destination_file}")
    except Exception as e:
        print(f"Error copying file: {e}")
        raise


def commit_to_github():
    # First update the remote URL to ensure SSH is being used
    update_remote_url()

    # Then, copy the HTML file before updating git
    copy_html_file()

    try:
        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)

        # Commit the changes
        subprocess.run(["git", "commit", "-m", "Automated commit"], check=True)

        # Push the changes
        subprocess.run(["git", "push"], check=True)

        print("Changes successfully committed and pushed to GitHub!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    commit_to_github()
