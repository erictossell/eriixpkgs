import subprocess
import os
import re
import argparse


def strip_ansi_sequences(text):
    """Remove ANSI escape sequences from a string."""
    ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
    return ansi_escape.sub("", text)


def run_command(command):
    """Run a shell command and return its output."""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return strip_ansi_sequences(result.stdout)


def directory_tree(path):
    """Generate a directory tree structure, ignoring hidden folders and listing only folder names."""
    tree = []
    for root, dirs, files in os.walk(path):
        # Skip hidden directories
        dirs[:] = sorted([d for d in dirs if not d.startswith(".")])
        level = root.replace(path, "").count(os.sep)
        if level == 0 or not root.split(os.sep)[-1].startswith("."):
            indent = " " * 4 * level
            tree.append(f"{indent}{os.path.basename(root)}/")
    return "\n".join(tree)


def generate_readme(
    username, repo_name, path, include_dir_tree, markdown_prefix_file="docs/readme.md"
):
    existing_content = ""
    try:
        with open(markdown_prefix_file, "r") as f:
            existing_content = f.read()
    except FileNotFoundError:
        print(f"{markdown_prefix_file} not found, creating new file.")

    flake_show_output = run_command(f"nix flake show . --all-systems")
    readme_content = existing_content

    if include_dir_tree:
        dir_tree = directory_tree(path)
        readme_content += "\n\n`Directory Tree`\n\n```bash\n" + dir_tree + "\n```\n"

    readme_content += "\n\n`nix flake show`\n\n```nix\n" + flake_show_output + "\n```"
    return readme_content


def main():
    parser = argparse.ArgumentParser(description="Generate README.md content.")
    parser.add_argument(
        "--dir-tree", help="Include directory tree structure", action="store_true"
    )
    # Add more arguments here as needed

    args = parser.parse_args()

    readme_content = generate_readme("erictossell", "eriixpkgs", ".", args.dir_tree)
    with open("README.md", "w") as f:
        f.write(readme_content)


if __name__ == "__main__":
    main()
