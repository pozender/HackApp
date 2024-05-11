from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import subprocess as subprocess
import re

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"frame0")


def is_valid_ip(ip):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip) is not None

def Nmap_vulners(ip):

    # implémentation de l'utilisation de la commande de nmap Vulners
    # exemple : nmap -sV --script nmap-vulners/ -p 22 89.0.142.86
    if entry_1.get() != None:
        ip=entry_1.get()
        if is_valid_ip(ip):
            messagebox.showwarning("L'adresse IP est valide.")
            
            subprocess.run(["ping" , ip , "-c" , "3"], check=True)
            subprocess.run(["nmap", "-sV", "--script", "nmap-vulners", "-p", "22", ip , ">" , "nmap-vulners.txt"])
            messagebox.showwarning(" Le résultat des tests a été ecrit dans le fichier : nmap-vulners.txt")
            
        else:
            messagebox.showwarning("L'adresse IP n'est pas valide,  merci dans renseigner une de valide.")
            
    

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("NMAP")
window.geometry("900x800")
window.configure(bg = "#CECECE")


canvas = Canvas(
    window,
    bg = "#CECECE",
    height = 800,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    380.0,
    32.0,
    anchor="nw",
    text="NMAP",
    fill="#000000",
    font=("RobotoRoman Bold", 48 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    239.5,
    177.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=111.0,
    y=161.0,
    width=257.0,
    height=31.0
)

canvas.create_text(
    105.0,
    124.0,
    anchor="nw",
    text="@IP_ADDRESS",
    fill="#000000",
    font=("RobotoRoman Bold", 24 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    693.5,
    179.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=565.0,
    y=163.0,
    width=257.0,
    height=31.0
)

canvas.create_text(
    559.0,
    126.0,
    anchor="nw",
    text="PORT",
    fill="#000000",
    font=("RobotoRoman Bold", 24 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=114.0,
    y=594.0,
    width=120.0,
    height=43.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=303.0,
    y=594.0,
    width=120.0,
    height=43.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Nmap_vulners(entry_1.get()),
    relief="flat"
)
button_3.place(
    x=493.0,
    y=594.0,
    width=120.0,
    height=43.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=682.0,
    y=594.0,
    width=120.0,
    height=43.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=359.0,
    y=374.0,
    width=183.0,
    height=53.0
)

canvas.create_text(
    246.0,
    285.0,
    anchor="nw",
    text="/home/user/",
    fill="#000000",
    font=("RobotoRoman Bold", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
