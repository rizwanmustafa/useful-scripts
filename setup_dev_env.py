import os
import colorama

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

    ret_code = os.system("sudo pacman -Syyu --noconfirm")
    if ret_code == 0:
        print(f"{colorama.Fore.GREEN}Command executed sucessfully!{colorama.Style.RESET_ALL}")
    else:
        print(f"Command failed with code: {ret_code}")
    print()


def install_python():
    print(make_stylish_heading("Installing Python", colorama.Style.BRIGHT))

    ret_code = os.system("sudo pacman -S python3 --noconfirm")
    if ret_code == 0:
        print(f"{colorama.Fore.GREEN}Command executed sucessfully!{colorama.Style.RESET_ALL}")
    else:
        print(f"Command failed with code: {ret_code}")


def install_node_pack():
    print(make_stylish_heading("Installing NVM and Node LTS", colorama.Style.BRIGHT))

    ret_code = os.system("curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash")
    if ret_code == 0:
        print(f"{colorama.Fore.GREEN}Command executed sucessfully!{colorama.Style.RESET_ALL}")
    else:
        print(f"Command failed with code: {ret_code}")
    print()

    ret_code = os.system("echo 'export NVM_DIR=\"$HOME/.nvm\"; [ -s \"$NVM_DIR/nvm.sh\" ] && \. \"$NVM_DIR/nvm.sh\"; nvm install --lts' | bash")
    if ret_code == 0:
        print(f"{colorama.Fore.GREEN}Command executed sucessfully!{colorama.Style.RESET_ALL}")
    else:
        print(f"Command failed with code: {ret_code}")

def make_stylish_heading(heading: str, color_code: str = "") -> str:
    style = "#" * (len(heading) + 4)

    heading = "# " + color_code + heading + colorama.Style.RESET_ALL + " #"

    return f"{style}\n{heading}\n{style}"


if __name__ == "__main__":
    colorama.init()
    # update_system()
    # install_python()
    install_node_pack()
