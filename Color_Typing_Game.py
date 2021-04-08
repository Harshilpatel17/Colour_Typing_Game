#!/usr/bin/env python
# coding: utf-8

# In[20]:


import tkinter 
import random 
from tkinter import messagebox

colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown','Cyan'] # list of possible colour. 
score = 0
timeleft = 30 #Timelimit
  
# function that will start the game. 
def startGame(event): 
      
    if timeleft == 30: 
          
        countdown() # Function that will start the countdown timer. 
           
    nextColour() # Function that will change the color of text shown in screen.
    
def nextColour(): 
    global timeleft 
    global score 
    
    if timeleft > 0:  # if a game is active
  
        # For focus in entry box. 
        e.focus_set() 
   
        if e.get().lower() == colours[1].lower():  # if the colour typed is equal to the colour of the text
              
            score += 1
  
        e.delete(0, tkinter.END) # clear the text entry box. 
          
        random.shuffle(colours) 
          
        # change the colour to type, by changing the text _and_ the colour to a random colour value.
        label.config(fg = str(colours[1]), text = str(colours[0])) 
          
        scoreLabel.config(text = "Score: " + str(score))  # update the score. 

def countdown(): 
  
    global timeleft 
    if timeleft==0:
        messagebox.showinfo("timeleft","Time is over and Your Score is "+str(score))
  
    if timeleft > 0: # if a game is active
        
        timeleft -= 1 # decrement the timer.

        timeLabel.config(text = "Time left: "+ str(timeleft))  # update the time left label 
                                 
        timeLabel.after(1000, countdown)  # run the function again after 1 second (Time is in milisecond).

root = tkinter.Tk() # For a GUI window 
  
root.title("COLORGAME") 
root.geometry("500x250") 
  
# add an instructions label 
instructions = tkinter.Label(root, text = "Type in the colour of the words, and not the word text!",font = ('Verdana', 12)) 
instructions.pack()  
  
# add a score label 
scoreLabel = tkinter.Label(root, text = "Press enter to start",font = ('Verdana', 12)) 
scoreLabel.pack() 
  
# add a time left label 
timeLabel = tkinter.Label(root, text = "Time left: " +str(timeleft), font = ('Verdana', 12)) 
                
timeLabel.pack() 

  
# add a label for displaying the colours 
label = tkinter.Label(root, font = ('Verdana', 60)) 
label.pack() 
# add a text entry box for 
# typing in colours 
e = tkinter.Entry(root) 
  
# run the 'startGame' function  
# when the enter key is pressed 
root.bind('<Return>', startGame) 
e.pack() 
# set focus on the entry box 
e.focus_set() 
# start the GUI 
root.mainloop() 


# In[4]:





# In[ ]:




