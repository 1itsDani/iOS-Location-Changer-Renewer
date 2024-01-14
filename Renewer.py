import os
import sys
import subprocess
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )


def welcome_message():
    print("Hello, welcome to Modifier made by Dani version 0.1 (Date 2024, Jan)")


def display_menu():
    print("\n1. Start")
    print("2. Quit program")


def delete_registry_key():
    try:
        # Create a .reg file content
        reg_content = "Windows Registry Editor Version 5.00\n\n[-HKEY_CURRENT_USER\Software\Siacgltiyg\SiaData\MFTimes]"

        # Save the .reg file
        reg_file_path = os.path.join(os.getcwd(), "remover.reg")
        with open(reg_file_path, "w") as reg_file:
            reg_file.write(reg_content)

        # Run the reg file to delete the registry key
        subprocess.run(["regedit", "/s", reg_file_path], check=True)

        print("Successfully deleted. You have now 2 new times.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to delete registry key. Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up the temporary .reg file
        os.remove(reg_file_path)


def main():
    welcome_message()

    if not is_admin():
        print("Program needs to run as an administrator. Restarting...")
        run_as_admin()
        sys.exit()

    while True:
        display_menu()
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            delete_registry_key()
        elif choice == "2":
            print("Quitting program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
