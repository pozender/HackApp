import tkinter as tk
from tkinter import messagebox
import subprocess

def check_packages():
    # if os_var.get() == "Linux":
    #     if kernel_var.get() == "":
    #         messagebox.showwarning("Kernel Not Selected", "Please select a kernel.")
    #         return
    #     else:
    #         kernel_type = kernel_var.get()
    #         required_packages = ["aircrack-ng", "nmap", "hydra", "hashcat", "john", "metasploit", "nettercap"]
    # # elif os_var.get() == "Windows":
    # #     if windows_version_var.get() == "":
    # #         messagebox.showwarning("Windows Version Not Selected", "Please select a Windows version.")
    # #         return
    # #     else:
    # #         kernel_type = windows_version_var.get()
    # #         required_packages = ["aircrack-ng", "nmap", "hydra", "hashcat", "john", "metasploit", "nettercap"]
    # # else:  # macOS
    # #     kernel_type = "macOS"
    # #     required_packages = ["aircrack-ng", "nmap", "hydra", "hashcat", "john", "metasploit", "nettercap"]
   
    required_packages = ["aircrack-ng", "git", "hydra", "hashcat", "john", "metasploit", "nettercap" ,"nmap"]
    missing_packages = []
    for package in required_packages:
        try:
            if os_var.get() == "Windows":
                subprocess.check_output(["where", package])
            else:
                subprocess.check_output(["which", package])
        except subprocess.CalledProcessError:
            missing_packages.append(package)
    
    if missing_packages:
        messagebox.showwarning("Packages Missing", f"The following packages are missing: {', '.join(missing_packages)}")
        install_packages(missing_packages)
    else:
        messagebox.showinfo("Packages Installed", "All required packages are installed.")

def select_os():
    # if os_var.get() == "Windows":
    #     windows_frame.pack()
    #     kernel_frame.pack_forget()
    if os_var.get() == "Linux":
        kernel_frame.pack()
        windows_frame.pack_forget()
    # else:  # macOS
    #     kernel_frame.pack_forget()
    #     windows_frame.pack_forget()

def select_kernel():
    messagebox.showinfo("Kernel Type", f"Selected kernel: {kernel_var.get()}")

def install_packages(requirements_packages):
    for package in requirements_packages:
        subprocess.run(["sudo", "apt", "install", "-y", package ], check=True)
        if subprocess.run(["sudo", "apt", "install", "-y", package ], check=True) == True:
            print(f"Package {package} installed successfully.")
        else:
            print(f"Failed to install package {package}.")
        if package == "metasploit-framework":
            subprocess.run(["sudo" , "apt" , "install" , ""])
        if package == "nmap":
            if "/usr/share/nmap/scripts" == None:
                subprocess.run(["cd" , "/usr/share/nmap/scripts"])
                subprocess.run(["git", "clone", "https://github.com/vulnersCom/nmap-vulners.git"])
                # exemple use : nmap -sV --script nmap-vulners/ -p 22 89.0.142.86  -> analyse des vulnérabilitées de SSH ou tout autre truc sur le port 22
            else :
                messagebox.showinfo("Nmap Scripts", "Nmap scripts already installed. PLease delete what is in /usr/share/nmap/scripts if this is not the nmap scripts and try again.")
# def select_windows_version():
#     messagebox.showinfo("Windows Version", f"Selected Windows version: {windows_version_var.get()}")

# GUI
root = tk.Tk()
root.title("OS Selection")
root.geometry("400x300")  # Taille de la fenêtre principale

os_label = tk.Label(root, text="Select Operating System:")
os_label.pack()

os_var = tk.StringVar()
os_var.set("Linux")  # Default selection
os_options = ["Linux"] # rajouter macOS et windows dans ce tableau pour permettre le multi-plateforme
for os_type in os_options:
    os_radio = tk.Radiobutton(root, text=os_type, variable=os_var, value=os_type, command=select_os)
    os_radio.pack()

kernel_frame = tk.Frame(root)
kernel_frame.pack()

kernel_label = tk.Label(kernel_frame, text="Select Kernel Type:")
kernel_label.pack()

kernel_var = tk.StringVar()
kernel_var.set("")  # Default selection
kernel_options = ["Fedora", "Debian", "Arch"]
for kernel in kernel_options:
    kernel_radio = tk.Radiobutton(kernel_frame, text=kernel, variable=kernel_var, value=kernel)
    kernel_radio.pack()

windows_frame = tk.Frame(root)

# windows_label = tk.Label(windows_frame, text="Select Windows Version:")
# windows_label.pack()

# windows_version_var = tk.StringVar()
# windows_version_var.set("")  # Default selection
# windows_version_options = ["Windows 10", "Windows 11"]
# for windows_version in windows_version_options:
#     windows_version_radio = tk.Radiobutton(windows_frame, text=windows_version, variable=windows_version_var, value=windows_version)
#     windows_version_radio.pack()

check_button = tk.Button(root, text="Check Packages", command=check_packages)
check_button.pack()

root.mainloop()
