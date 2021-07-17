import tkinter as tk
from tkinter.constants import SUNKEN, TOP, X, Y
import time
from plyer import notification
from typing import Mapping

def notifyMe():
	print("Succesfull")
	
root = tk.Tk()

root.maxsize(300,300)
root.minsize(300,300)
root.title("Hydration Notifier")

#canvas = tk.Canvas(root, height=200, width=200)
#canvas.pack()

#background_image = tk.PhotoImage(file='water.png')
#background_label = tk.Label(root, image = background_image)
#background_label.place(relwidth=1, relheight=1)

#assigning a frame on the window
frame = tk.Frame(root,bg='#26b7ff',bd=10,relief=SUNKEN)
frame.pack(pady=30)

#adding text on the frame
text= tk.Label(frame, text="Hydration Notifier", font = "lucida 20 bold")
text.pack(side = TOP,pady = 10 , padx=10)

#adding labels
gender = tk.Label(frame, text= "Enter Your Gender: ", bg='#faa35c', font= "comicsans 15 bold")
gender.pack(fill=X, padx=5)

#taking input from the user
entry = tk.Entry(frame, bg='#d3fa5c',font=40)
entry.pack()

#adding labels
lower_label = tk.Label(frame, text= "Enter your age: ", bg='#faa35c' ,font= "comicsans 15 bold")
lower_label.pack(fill=X, padx=5)

#taking input from the user
lower_entry = tk.Entry(frame, bg='#d3fa5c',font=40)
lower_entry.pack()

#adding checkbox
check= tk.Checkbutton(text="I agree to all terms and conditions")
check.pack()

#adding final button
button = tk.Button(root, text= "Start Notifier", bg="#FFFF00", command= root.destroy)
button.pack()


root.mainloop()

# create Notification object
def notifyMe(title, message):
   
    notification.notify(
        title = title,
        
        message = message,
    
    # set timeout for a notification
        timeout = 15,
    )

if __name__ == '__main__':
    while True:
        notifyMe("Hey There, It's time to hydrate yourself" , "Your daily need of water needs to be fulfilled" )
   
    # short delay between notifications
        time.sleep(7200)
		