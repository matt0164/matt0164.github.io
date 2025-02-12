import subprocess


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
