import tkinter as tk
from tkinter import messagebox
import subprocess

def install_packages(os_var, kernel_var, windows_version_var):
    if os_var == "Linux":
        if kernel_var == "":
            messagebox.showwarning("Kernel Not Selected", "Please select a kernel.")
            return
        else:
            kernel_type = kernel_var
            if kernel_type == "Fedora":
                packages = ["aircrack-ng", "nmap", "hydra", "hashcat", "john", "metasploit", "net-tools"]
            elif kernel_type == "Debian":
                packages = ["aircrack-ng", "nmap", "hydra", "hashcat", "john", "metasploit", "net-tools"]
            elif kernel_type == "Arch":
                packages = ["aircrack-ng", "nmap", "hydra", "hashcat", "john", "metasploit", "net-tools"]
            else:
                messagebox.showwarning("Invalid Kernel", "Invalid kernel type selected.")
                return
    elif os_var == "Windows":
        if windows_version_var == "":
            messagebox.showwarning("Windows Version Not Selected", "Please select a Windows version.")
            return
        else:
            windows_version = windows_version_var
            if windows_version == "Windows 10":
                packages = ["aircrack-ng", "nmap", "hydra", "hashcat", "john", "metasploit", "netcat"]
            elif windows_version == "Windows 11":
                packages = ["aircrack-ng", "nmap", "hydra", "hashcat", "john", "metasploit", "netcat"]
            else:
                messagebox.showwarning("Invalid Windows Version", "Invalid Windows version selected.")
                return
    else:  # macOS
        packages = ["aircrack-ng", "nmap", "hydra", "hashcat", "john", "metasploit", "netcat"]

    total_packages = len(packages)
    progress_step = 100 / total_packages
    progress_value = 0

    progress_window = tk.Toplevel()
    progress_window.title("Installation Progress")

    progress_label = tk.Label(progress_window, text="Installing packages:")
    progress_label.pack()

    progress_bar = tk.Tk.Progressbar(progress_window, length=200, mode="determinate")
    progress_bar.pack()

    for package in packages:
        progress_label.config(text=f"Installing {package}...")
        progress_value += progress_step
        progress_bar["value"] = progress_value
        progress_window.update()

        try:
            subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
        except subprocess.CalledProcessError:
            messagebox.showerror("Installation Error", f"Failed to install {package}.")
            break

    messagebox.showinfo("Installation Complete", "Package installation completed.")
    progress_window.destroy()


# Main script (exemple d'utilisation)
os_var = "Linux"  # Remplacer par le choix du système d'exploitation
kernel_var = "Fedora"  # Remplacer par le choix du noyau pour Linux
windows_version_var = ""  # Remplacer par le choix de la version de Windows

install_packages(os_var, kernel_var, windows_version_var)
