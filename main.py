#William Bukowski | Chatbot with Chatterbot lib and Tkinter custom GUI

#William's chatbot w/ Chatterbot in Python 3

#imports
from email import message
from tkinter import *
import tkinter as tk
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


#training statements
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]


#get from chatwindow, print
def printChat():
    messageWindow.delete("1.0", "end")
    result = chatWindow.get("1.0", "end")
    chatWindow.delete("1.0", "end")
    #print(result)
    response = chatbot.get_response(result)
    #print(response)
    messageWindow.insert("end-1c", response)
    
   


#new chatbot object named HAL 9000
chatbot = ChatBot("HAL 9000")
#train the chabot
trainer = ListTrainer(chatbot)
trainer.train(conversation)



#initialize tkinter object
root = tk.Tk()


#GUI dimensions, title, set resize to false
root.title("Chat With HAL 9000")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)

#create menu from root object
main_menu = Menu(root)

#new menu from root object 
file_menu = Menu(root)

#Add commands to submenu
file_menu.add_command(label="New..")
file_menu.add_command(label="Save As..")
file_menu.add_command(label="Exit")
main_menu.add_cascade(label="File", menu=file_menu)

#Add the rest of the menu options to the main menu
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
root.config(menu=main_menu)

#create and size new text window (typable)
chatWindow = Text(root, bd=1, bg="black",  width="50", height="8", font=("Arial", 23), foreground="#00ffff")
chatWindow.place(x=6,y=6, height=385, width=370)

#create and size window for response (typable)
messageWindow = Text(root, bd=0, bg="black",width="30", height="4", font=("Arial", 23), foreground="#00ffff")
messageWindow.place(x=128, y=400, height=88, width=260)

#its a scrollbar bro
scrollbar = Scrollbar(root, command=chatWindow.yview, cursor="star")
scrollbar.place(x=375,y=5, height=385)

#Send button, brosef
Button= Button(root, text="Send",
    width="12", height=5,
    bd=0, bg="#0080ff", 
    activebackground="#00bfff",
    foreground='#ffffff',
    font=("Arial", 12), command=printChat)
Button.place(x=6, y=400, height=88)   



#bind enter key to send button via printChat function command
root.bind('<Return>',lambda event:printChat())

#call mainloop on tkinter object, opens window *
root.mainloop()