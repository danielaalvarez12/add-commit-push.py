import subprocess
import sys

def run_command(command):
    """Print the command, execute it, and print the output."""
    print(f"\nRunning command: {' '.join(command)}")
    result = subprocess.run(command, check=True, text=True, capture_output=True)
    print(result.stdout)
    return result

def main():
    # Initialize variables
    commit_message = ""
    force = False

    # Process command-line arguments
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "-m" and i + 1 < len(sys.argv):
            commit_message = sys.argv[i + 1]
        elif sys.argv[i] == "-f":
            force = True

    # Show git status
    print("git status:")
    run_command(["git", "status"])

    # Prepare commands
    add_command = ["git", "add", "."]
    commit_command = ["git", "commit", "-m", commit_message or "Update"]
    push_command = ["git", "push"]

    # Display queued commands
    print("\nQueued commands:")
    print(f"1. {' '.join(add_command)}")
    print(f"2. {' '.join(commit_command)}")
    print(f"3. {' '.join(push_command)}")

    # Ask for user confirmation unless forced
    if not force:
        confirm = input("\nDo you want to execute these commands? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Operation canceled.")
            sys.exit(0)

    # Execute commands
    run_command(add_command)
    run_command(commit_command)
    run_command(push_command)

    print("All commands executed successfully.")

if __name__ == "__main__":
    main()
