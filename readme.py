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


def directory_tree(path, make_links=False):
    """Generate a directory tree structure, optionally as Markdown links."""
    tree = []
    for root, dirs, files in os.walk(path):
        # Skip hidden directories and files
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        files[:] = [f for f in files if not f.startswith(".")]
        level = root.replace(path, "").count(os.sep)

        # Skip root level files and hidden files
        if level == 0:
            continue

        indent = " " * 4 * level
        subdir = os.path.basename(root)
        # Format directory as link if required
        if make_links:
            subdir_path = os.path.relpath(root, path)
            subdir = f"[{subdir}]({subdir_path}/)"
        tree.append(f"{indent}{subdir}/")

        # Add files
        for file in files:
            file_indent = " " * 4 * (level + 1)
            if make_links:
                file_path = os.path.relpath(os.path.join(root, file), path)
                file = f"[{file}]({file_path})"
            tree.append(f"{file_indent}{file}")

    return "\n".join(tree)


def generate_readme(
    path,
    include_dir_tree,
    include_links,
    include_nix,
    markdown_prefix_file,
    username=None,
    repo_name=None,
):
    existing_content = ""
    if markdown_prefix_file:
        try:
            with open(markdown_prefix_file, "r") as f:
                existing_content = f.read()
        except FileNotFoundError:
            print(f"{markdown_prefix_file} not found, creating new file.")

    readme_content = existing_content

    if username and repo_name:
        readme_content += f"\n\n## Repository Information\n**User:** {username}\n**Repository:** {repo_name}\n"

    if include_dir_tree:
        dir_tree = directory_tree(path)
        readme_content += "\n\n`Directory Tree`\n\n```bash\n" + dir_tree + "\n```\n"

    if include_links:
        dir_tree_links = directory_tree(path, make_links=True)
        readme_content += (
            "\n\n`Directory Tree`\n\n```bash\n" + dir_tree_links + "\n```\n"
        )

    if include_nix:
        flake_show_output = run_command("nix flake show . --all-systems")
        readme_content += (
            "## Nix Flake Show\n\n```nix\n" + flake_show_output + "\n```\n"
        )

    return readme_content


def main():
    parser = argparse.ArgumentParser(description="Generate README.md content.")
    parser.add_argument(
        "--dir-tree", help="Include directory tree structure", action="store_true"
    )
    parser.add_argument("--header", help="Path to the header markdown file", type=str)
    parser.add_argument(
        "--nix", help="Include nix flake show output", action="store_true"
    )
    parser.add_argument("--username", help="GitHub username", type=str)
    parser.add_argument("--repo-name", help="GitHub repository name", type=str)
    parser.add_argument(
        "--links",
        help="Turn directory tree into Markdown links",
        action="store_true",
    )

    args = parser.parse_args()

    readme_content = generate_readme(
        ".",
        args.dir_tree,
        args.links,
        args.nix,
        args.header,
        args.username,
        args.repo_name,
    )
    with open("README.md", "w") as f:
        f.write(readme_content)


if __name__ == "__main__":
    main()
