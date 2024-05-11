import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PackageInstaller import PackageInstaller  

def install_packages(os_var, kernel_var, windows_version_var):
    installer = PackageInstaller()  

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
                packages = {
                    "aircrack-ng": "https://example.com/aircrack-ng-installer.exe",
                    "nmap": "https://example.com/nmap-installer.exe",
                    
                }
            elif windows_version == "Windows 11":
                packages = {
                    "aircrack-ng": "https://example.com/aircrack-ng-installer.exe",
                    "nmap": "https://example.com/nmap-installer.exe",
                    
                }
            else:
                messagebox.showwarning("Invalid Windows Version", "Invalid Windows version selected.")
                return
    else:  
        packages = ["aircrack-ng", "nmap", "hydra", "hashcat", "john", "metasploit", "netcat"]

    
    if messagebox.askyesno("Confirm Installation", "Do you want to install the required packages?"):
        installer.download_windows(packages)  
        messagebox.showinfo("Installation Complete", "Package installation completed.")
    else:
        messagebox.showinfo("Installation Cancelled", "Package installation cancelled.")
