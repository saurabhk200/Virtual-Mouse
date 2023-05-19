import io
import os
import subprocess
import sys
import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Air Click")
root.geometry("600x500")
# root.configure(background="#7FFFD4")
# def change_bg_color():
#     r, g, b = root.winfo_rgb(root["bg"])
#     r = (r + 100) % 65535
#     g = (g + 300) % 65535
#     b = (b + 500) % 65535
#     root.configure(background='#{:04x}{:04x}{:04x}'.format(r, g, b))
#     root.after(50, change_bg_color)

# change_bg_color()
# --------------------------------
# Set background image
# image_path = "C:\\Users\\saura\\Downloads\\WhatsApp Image 2023-05-03 at 2.06.08 PM.png"
# bg_image = tk.PhotoImage(file=image_path)
# bg_label = tk.Label(root, image=bg_image)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# ---------------------------------------------------------------
# url = "https://assets.tadigital.com/2022-09/The-Impact-of-AI-and-ML-on-Front-End-Development-Blog-banner.jpg"
# with urllib.request.urlopen(url) as u:
image_path = "C:\\Users\\saura\\Downloads\\import_tkinter\\Air.png"
# Load image and set alpha channel to 30%
image = Image.open(image_path).convert("RGBA")
alpha = Image.new("L", image.size, 190)
image.putalpha(alpha)

# Create PhotoImage and Label widgets
photo = ImageTk.PhotoImage(image)
bg_label = tk.Label(root, image=photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
# --------------------------------------------------------------------
# Use sys._MEIPASS to get the path to the temporary directory
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the temp directory is
    # sys._MEIPASS
    base_path = sys._MEIPASS
else:
    # If the application is run as a script, the temp directory is
    # the directory containing the script
    base_path = os.path.abspath(".")


# welcome_label = tk.Label(root, text=" AIR CLICK! ", font=("Algerian", 30),relief="groove")
# welcome_label.pack()

# def animate_label():
#     # Shift the text to the right
#     text = welcome_label.cget("text")
#     text = text[-1] + text[:-1]
#     welcome_label.config(text=text)

#     # Schedule the function to be called again after 100ms
#     root.after(600, animate_label)

# # Start the animation
# animate_label()

message_label = tk.Label(root, text="")
message_label.pack()

def on_button_hover(event):
    button1.configure(background="light grey", relief="raised",cursor="hand2",borderwidth=3)

def on_button_leave(event):
    button1.configure(background="grey", relief="flat", cursor="arrow")


button1 = tk.Button(root, text="Run Mouse", background="grey" ,width=10, height=2)
button1.bind("<Enter>", on_button_hover)
button1.bind("<Leave>", on_button_leave)
# button1.pack(side=tk.LEFT, padx=10)
button1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

def on_button_hover(event):
    button2.configure(background="#FF4136", relief="raised", cursor="hand2",borderwidth=3)

def on_button_leave(event):
    button2.configure(background="#9400D3", relief="flat", cursor="arrow")

button2 = tk.Button(root, text="Run Assistant",background="#9400D3" ,width=10, height=2 )
button2.bind("<Enter>", on_button_hover)
button2.bind("<Leave>", on_button_leave)
# button2.pack(side=tk.LEFT, padx=10)
button2.place(relx=0.5, rely=0.53, anchor=tk.CENTER)

process1 = None
process2 = None

# Use os.path.join to create a relative path to the additional files
script1_path = os.path.join(base_path, "Virtual_Mouse.py")
script2_path = os.path.join(base_path, "demovoice.py")

def run_script1():
    global process1, process2
    if process2 is None:
        process1 = subprocess.Popen(["python", script1_path])
        button1.config(state=tk.DISABLED)
        button2.config(state=tk.NORMAL)
        message_label.config(text="Running script 1...")
    else:
        message_label.config(text="Cannot run script 1 while script 2 is running.")

def run_script2():
    global process1, process2
    if process1 is None:
        process2 = subprocess.Popen(["python", script2_path])
        button1.config(state=tk.NORMAL)
        button2.config(state=tk.DISABLED)
        message_label.config(text="Running script 2...")
    else:
        message_label.config(text="Cannot run script 2 while script 1 is running.")

def stop_processes():
    global process1, process2
    if process1 is not None:
        process1.terminate()
        process1 = None
        button1.config(state=tk.NORMAL)
        button2.config(state=tk.NORMAL)
    if process2 is not None:
        process2.terminate()
        process2 = None
        button2.config(state=tk.NORMAL)
        button1.config(state=tk.NORMAL)
    message_label.config(text="Processes stopped.")

button1.config(command=run_script1)
button2.config(command=run_script2)

def on_button_hover(event):
    stop_button.configure( relief="raised", cursor="hand2")

def on_button_leave(event):
    stop_button.configure( relief="flat", cursor="arrow")
stop_button = tk.Button(root, text="Stop", command=stop_processes,width=10, height=2, borderwidth=3)
stop_button.bind("<Enter>", on_button_hover)
stop_button.bind("<Leave>", on_button_leave)
stop_button.place(relx=0.5, rely=0.66, anchor=tk.CENTER)

root.mainloop()
