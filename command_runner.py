import subprocess
import socket
import os
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from threading import Thread
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Developer information (stylish header using ASCII art-like text)
developer_info = f"""
{Fore.CYAN}---------------------------------------------------
{Fore.MAGENTA} LARAVEL DEVELOPMENT SERVER MANAGER
{Fore.CYAN}---------------------------------------------------
{Fore.WHITE}Developed by: {Fore.GREEN}Adi Hasan Rifat
{Fore.WHITE}Contact: {Fore.GREEN}adihasan@example.com
---------------------------------------------------
"""

# Function to clear the terminal
def clear_terminal():
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For macOS and Linux
        _ = os.system('clear')

# Function to get the local IP address
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't need to actually connect
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception as e:
        local_ip = "127.0.0.1"  # Fallback to localhost if unable to get local IP
    finally:
        s.close()
    return local_ip

# Step 1: Ensure Laravel dependencies are installed
def install_laravel_dependencies():
    print(f"{Fore.YELLOW}Installing Laravel dependencies using composer...")

    # Command to install dependencies using composer
    command = "composer install"

    # Execute the command using subprocess
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"{Fore.GREEN}Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Error installing dependencies: {e}")

# Function to update Laravel dependencies if the user confirms
def update_laravel_dependencies():
    choice = input(f"{Fore.CYAN}Do you want to update Laravel dependencies? (Y/N): ").strip().lower()
    if choice == "y":
        print(f"{Fore.YELLOW}Updating Laravel dependencies using composer...")
        command = "composer update"
        try:
            subprocess.run(command, shell=True, check=True)
            print(f"{Fore.GREEN}Dependencies updated successfully.")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}Error updating dependencies: {e}")
    else:
        print(f"{Fore.YELLOW}Skipping Laravel dependency update.")

# Function to run the Laravel development server
def run_laravel_server(host_ip, log_text):
    print(f"Running Laravel server on {host_ip}...")

    # Command to run Laravel with the specific host (IP) and port 8000
    command = f"php artisan serve --host {host_ip} --port 8000"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Continuously read logs and insert them into the log_text widget
    while True:
        output = process.stdout.readline()
        if output:
            log_text.insert(tk.END, output)
            log_text.yview(tk.END)  # Auto scroll to the end
        else:
            break

# GUI for Laravel logs
def open_gui(host_ip):
    # Create the GUI window
    window = tk.Tk()
    window.title(f"Laravel Server Logs - {host_ip}")

    # Create a ScrolledText widget for displaying logs
    log_text = ScrolledText(window, width=100, height=30)
    log_text.pack()

    # Run Laravel server in a separate thread, but keep the GUI on the main thread
    Thread(target=run_laravel_server, args=(host_ip, log_text)).start()

    # Start the tkinter main loop
    window.mainloop()

# Display the option menu
def display_menu():
    clear_terminal()
    print(developer_info)
    print(f"{Fore.MAGENTA}Please select an option:")
    print(f"{Fore.YELLOW}1. {Fore.WHITE}Run development server at local computer (127.0.0.1)")
    print(f"{Fore.YELLOW}2. {Fore.WHITE}Run development server at local IP (e.g., 192.168.x.x)")
    print(f"{Fore.YELLOW}3. {Fore.WHITE}Exit")

def main():
    while True:
        display_menu()
        choice = input(f"{Fore.CYAN}Enter your choice (1-3): ")

        if choice == "1":
            # Step 1: Ask if the user wants to update dependencies
            update_laravel_dependencies()
            # Step 2: Run server on localhost (127.0.0.1)
            open_gui("127.0.0.1")
            break
        elif choice == "2":
            # Step 1: Ask if the user wants to update dependencies
            update_laravel_dependencies()
            # Step 2: Run server on local IP
            local_ip = get_local_ip()
            open_gui(local_ip)
            break
        elif choice == "3":
            print(f"{Fore.GREEN}Exiting...")
            break
        else:
            print(f"{Fore.RED}Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
