import os
import subprocess

# Set GIT_SSH_COMMAND to use your SSH key
os.environ['GIT_SSH_COMMAND'] = 'ssh -i /Users/mattalevy/.ssh/id_ed25519'

# Run your git commands
result = subprocess.run(['git', 'push'], capture_output=True, text=True)
print(result.stdout, result.stderr)

def commit_to_github():
    try:
        # Add all changes
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
