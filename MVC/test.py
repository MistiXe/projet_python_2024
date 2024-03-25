# Import the required libraries
from tkinter import *
import pygame
pygame.mixer.init()
pygame.mixer.music.load("MVC/troll.wav")

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x500")

# Add a background image




# Initialize mixer module in pygame


# Define a function to play the music
def play_sound():
   pygame.mixer.music.set_volume(1)
   pygame.mixer.music.play()

# Add a Button widget
b1 = Button(win, text="Play Music", command=play_sound)
b1.pack(pady=60)

win.mainloop()