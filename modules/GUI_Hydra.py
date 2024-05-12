
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from subprocess import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"frame0_hydra")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Hydra BruteForce")
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
    386.0,
    35.0,
    anchor="nw",
    text="Hydra",
    fill="#000000",
    font=("RobotoRoman Bold", 48 * -1)
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
    x=359.0,
    y=663.0,
    width=183.0,
    height=53.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    218.5,
    191.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=90.0,
    y=175.0,
    width=257.0,
    height=31.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    682.5,
    191.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=554.0,
    y=175.0,
    width=257.0,
    height=31.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    218.5,
    333.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=90.0,
    y=317.0,
    width=257.0,
    height=31.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    682.5,
    333.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=554.0,
    y=317.0,
    width=257.0,
    height=31.0
)

canvas.create_text(
    84.0,
    138.0,
    anchor="nw",
    text="@IP",
    fill="#000000",
    font=("RobotoRoman Bold", 24 * -1)
)

canvas.create_text(
    176.0,
    416.0,
    anchor="nw",
    text="Username alone “-l”",
    fill="#000000",
    font=("RobotoRoman Bold", 20 * -1)
)

canvas.create_text(
    175.0,
    472.0,
    anchor="nw",
    text="Password alone “-p”",
    fill="#000000",
    font=("RobotoRoman Bold", 20 * -1)
)

canvas.create_text(
    586.0,
    416.0,
    anchor="nw",
    text="Username Dictionary “-L”",
    fill="#000000",
    font=("RobotoRoman Bold", 20 * -1)
)

canvas.create_text(
    590.0,
    477.0,
    anchor="nw",
    text="Password Dictionary “-P”",
    fill="#000000",
    font=("RobotoRoman Bold", 20 * -1)
)

canvas.create_text(
    548.0,
    138.0,
    anchor="nw",
    text="username",
    fill="#000000",
    font=("RobotoRoman Bold", 24 * -1)
)

canvas.create_text(
    78.0,
    274.0,
    anchor="nw",
    text="password",
    fill="#000000",
    font=("RobotoRoman Bold", 24 * -1)
)

canvas.create_text(
    542.0,
    274.0,
    anchor="nw",
    text="output file",
    fill="#000000",
    font=("RobotoRoman Bold", 24 * -1)
)

canvas.create_rectangle(
    135.0,
    417.0,
    157.0,
    439.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    546.0,
    417.0,
    568.0,
    439.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    135.0,
    473.0,
    157.0,
    495.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    546.0,
    478.0,
    568.0,
    500.0,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
