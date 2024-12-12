import tkinter as tk
import pyttsx3

def PlayButton():
    text = text_entry.get()
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

def exitButton():
    root.destroy()

def setButton():
    text_entry.delete(0, tk.END)


root = tk.Tk() 
root.title("Text to Speech")
root.geometry("600x400")


label = tk.Label(root, text="Enter the text:")  
label.pack(pady=10)


text_entry = tk.Entry(root, width=50)  
text_entry.pack(pady=10)


play_button = tk.Button(root, text="Play", width=7, command=PlayButton)  
play_button.pack(side=tk.LEFT, padx=60)

exit_button = tk.Button(root, text="Exit", width=7, bg="red", command=exitButton)

set_button = tk.Button(root, text="Set", width=7, command=setButton)
set_button.pack(side=tk.LEFT, padx=100)


root.mainloop()
