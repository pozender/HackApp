from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import subprocess as subprocess
import re

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"frame0")


def test_valid_ip(ip):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip) is not None

def Nmap_port(ip):
    port = entry_2.get()
    test_port = port.split("-")
    intervalle_start = int(test_port[0])
    intervalle_end = int(test_port[1])
    ip = entry_1.get()  
    if ip != None and port != None and intervalle_start > 0 and intervalle_end < 65536  and test_valid_ip(ip):   
        print("pas fait")
        subprocess.run(["nmap", "-pV", port, ip , ">" , "nmap-port.txt"])        
    else:
        messagebox.showinfo("Error", "The IP address or the Port are not valid, please enter a valid one.")          
def Nmap_os(ip):
    if ip != None and test_valid_ip(ip):
        
        subprocess.run(["nmap", "-V", "-O", ip , ">" , "nmap-os.txt"])
    else:
        messagebox.showinfo("Error", "The IP address is not valid, please enter a valid one.")      

def Nmap_vulners(ip):
    port_char = entry_2.get()
    port = int(port_char)
    ip=entry_1.get()
    if ip != None:
        if port == None:
            if test_valid_ip(ip):
                messagebox.showinfo("Validation", "The IP address is valid.")
                subprocess.run(["ping" , ip , "-c" , "3"], check=True)
                subprocess.run(["nmap", "-sV", "--script", "nmap-vulners", ip , ">" , "nmap-vulners.txt"])
                messagebox.showinfo("Finish", "The test results were written to the file: nmap-vulners.txt")

            else:
                messagebox.showinfo("Error", "The IP address is not valid, please enter a valid one.")

        else :
            if port > 1 :
                if port < 65535 :
                    if test_valid_ip(ip):
                        messagebox.showinfo("Validation", "The IP address and Port are validated." )

                        subprocess.run(["ping" , ip , "-c" , "3"], check=True)
                        subprocess.run(["nmap", "-sV", "--script", "nmap-vulners", "-p", str(port), ip , ">" , "nmap-vulners.txt"])
                        messagebox.showinfo("Finish", "The test results were written to the file: nmap-vulners.txt")


                    else:
                        messagebox.showinfo("Error", "The IP address is not valid, please enter a valid one.")
                        
                else :
                    messagebox.showinfo("Error", "The port must be between 1 and 65535.")
            else:
                messagebox.showinfo("Error", "The port must be between 1 and 65535.")



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def close_window(nom_fichier):
    window.destroy()
    subprocess.run(["python3", nom_fichier])

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
    command=lambda: Nmap_port(entry_1.get()),
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
    command=lambda: Nmap_os(entry_1.get()),
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

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: close_window("modules/GUI_Accueil.py"),
    relief="flat"
)
button_6.place(
    x=802.0,
    y=32.0,
    width=62.0,
    height=55.0
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
