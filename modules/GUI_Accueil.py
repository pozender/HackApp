
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import subprocess as subprocess
import src.webbrowser as webbrowser

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"frame0_acc")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def close_window(nom_fichier):
    window.destroy()
    subprocess.run(["python3", nom_fichier])
window = Tk()

window.geometry("900x800")
window.configure(bg = "#CECECE")
window.title("DarkSpear")

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
    261.0,
    27.0,
    anchor="nw",
    text="DarkSpear Pentest",
    fill="#000000",
    font=("RobotoRoman Bold", 48 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new("https://github.com/pozender/HackApp"),
    relief="flat"
)
button_1.place(
    x=63.0,
    y=604.0,
    width=249.0,
    height=72.0
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
    x=589.0,
    y=604.0,
    width=249.0,
    height=72.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=129.0,
    y=173.0,
    width=183.0,
    height=53.0
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
    x=129.0,
    y=260.0,
    width=183.0,
    height=53.0
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
    y=173.0,
    width=183.0,
    height=53.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=359.0,
    y=260.0,
    width=183.0,
    height=53.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: close_window("modules/GUI_Nmap_interface.py"),
    relief="flat"
)
button_7.place(
    x=359.0,
    y=347.0,
    width=183.0,
    height=53.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=589.0,
    y=173.0,
    width=183.0,
    height=53.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=589.0,
    y=260.0,
    width=183.0,
    height=53.0
)
window.resizable(False, False)
window.mainloop()
