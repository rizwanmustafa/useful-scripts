import os
import colorama
import requests

GITHUB_USERNAME = "rizwanmustafa"

"""

Ideas for the script:
- We would have different packs that we could install. Each pack would consist of common tools required for a language


Things this script will do:
- Update the system using pacman
- Install paru if not already installed

- Install python
- Install nvm
- Modify the .zshrc to recognize nvm
- Install the latest lts version of nodejs using nvm


"""


def update_system():
    print(make_stylish_heading("Updating System", colorama.Style.BRIGHT))
    execute_command("sudo pacman -Syyu --noconfirm")


def install_prerequisites():
    print(make_stylish_heading("Installing prerequisites", colorama.Style.BRIGHT))
    execute_command("sudo pacman -S git")


def clone_git_repos():
    print(make_stylish_heading("Cloning Git Repos", colorama.Style.BRIGHT))
    if input("Do you want to clone all repos [y/N]? ").lower() != "y":
        print()
        return

    clone_path = os.path.expanduser(input("Enter clone path: "))

    try:
        repos = requests.get(f"https://api.github.com/users/{GITHUB_USERNAME}/repos").json()
    except Exception as e:
        print(f"{colorama.Fore.RED}There was an error while making a GET request to Github API: ")
        print(e, colorama.Style.RESET_ALL)
        return

    for i in repos:
        execute_command(f"cd {clone_path}; git clone https://github.com/{GITHUB_USERNAME}/{i.get('name')}")


def install_vscode():
    print(make_stylish_heading("Installing Visual Studio Code", colorama.Style.BRIGHT))
    execute_command("cd /tmp; git clone https://aur.archlinux.org/visual-studio-code-bin.git vs_code; cd vs_code; makepkg -si")


def install_python():
    print(make_stylish_heading("Installing Python", colorama.Style.BRIGHT))
    execute_command("sudo pacman -S python3 --noconfirm")


def install_node_pack():
    print(make_stylish_heading("Installing NVM and Node LTS", colorama.Style.BRIGHT))

    execute_command("curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash")
    execute_command("echo 'export NVM_DIR=\"$HOME/.nvm\"; [ -s \"$NVM_DIR/nvm.sh\" ] && \. \"$NVM_DIR/nvm.sh\"; nvm install --lts' | bash")


def make_stylish_heading(heading: str, color_code: str = "", padding: int = 75) -> str:
    heading = heading.center(padding)
    style = "#" * (len(heading) + 4)

    heading = "# " + color_code + heading + colorama.Style.RESET_ALL + " #"

    return f"{style}\n{heading}\n{style}"


def execute_command(cmd: str) -> int:
    ret_code = os.system(cmd)

    print()
    if ret_code == 0:
        print(f"{colorama.Fore.GREEN}Command executed sucessfully!{colorama.Style.RESET_ALL}")
    else:
        print(f"Command failed with code: {ret_code}")
    print()

    return ret_code


colorama.init()
if __name__ == "__main__":
    print(f"{colorama.Fore.YELLOW}Setting up Development Environment...{colorama.Style.RESET_ALL}")

    update_system()
    install_prerequisites()

    install_python()
    install_node_pack()
    install_vscode()

    clone_git_repos()

    print(f"{colorama.Fore.GREEN}Setup finished!{colorama.Style.RESET_ALL}")
