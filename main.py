from tkinter import *
import turtle
import time
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import subprocess
import os
from shutil import copyfile


turtle.setup(1200,500)
t = turtle.Turtle()
screen = turtle.Screen()
screen.title("SENTINEL")
screen.bgpic("my1.gif")
t.hideturtle()

t.penup()
t.goto(0,110)
t.pendown()
t.pencolor("black")
t.write("SENTINEL", move='true', align="center", font=("Georgia", 50))
t.penup()
t.goto(-20,70)
t.pendown()
t.write("Developed By : Vidhun Raj, Elias Joy, Telphin Ralphy, Sravan Sathyan",align="left",font=("georgia",13,"normal",'italic'))

t.penup()
t.goto(-207,-130)
t.pendown()
t.write("Loading .......",align='right',font=("Ariel",13,'normal','italic'))

t.pensize(3)
t.penup()
t.goto(-300,-100)
t.pendown()
t.pencolor("white")
t.forward(200)
time.sleep(1)
t.forward(150)
time.sleep(1)
t.forward(200)

time.sleep(2)
t.forward(190)
time.sleep(1)
turtle.bye()


def intruder_directory():
    subprocess.run(["explorer", os.path.realpath("outputs")])

def Exit():
    return exit()
def save_image(file_path, save_folder, filename=None):
    file_name = f"{filename}.jpg"
    destination_path = os.path.join(save_folder, file_name)
    try:
        copyfile(file_path, destination_path)

        print("Image saved successfully.")
    except Exception as e:
        print("Failed to save the image:", str(e))

def select_image():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

    if file_path:
        folder_path = filedialog.askdirectory()

        if folder_path:
            root2 = Tk()
            root2.title("New Member")
            root2.geometry("200x100")
            label = Label(root2, text="Enter Name:")
            label.pack()
            entry = Entry(root2)
            entry.pack()

            def save_with_filename():
                filename = entry.get()
                save_image(file_path, folder_path, filename)
                root2.destroy()

            button = Button(root2, text="Save", command=save_with_filename)
            button.pack()

            root2.mainloop()
            
        else:
            print("Folder not selected.")
    else:
        print("Image file not selected.")

def start_detection():
    subprocess.call(["python", "pro1.py"])




def mainwin():
    global gui, text1

    gui = Tk()

    # gui.configure(bg='blue')
    gui.title("SETUP")
    gui.geometry("900x539")
    bg=PhotoImage(file="my2.gif")
    label1 = Label(gui, image=bg)
    label1.place(x=0, y=0)
    image1=ImageTk.PhotoImage(Image.open("my4.gif"))
    label2=Label(gui,image=image1)
    label2.grid(row=0,column=0, padx=60,pady=80)
    button1=Button(gui,text="ADD NEW MEMBER", command=select_image, activeforeground="cyan", activebackground="yellow")
    button1.place(x=80, y=350)
    image2=ImageTk.PhotoImage(Image.open("my5.gif"))
    label4=Label(gui,image=image2)
    label4.place(x=600, y=60)
    button2=Button(gui, text="WHO'S INTRUDING?", command=intruder_directory, activeforeground="red", activebackground="pink")
    button2.place(x=650, y=350)
    button3=Button(gui, text="START DETECTING", command=start_detection,activeforeground="cyan", activebackground="yellow")
    button3.place(x=400,y=450)
    gui.mainloop()

mainwin()


