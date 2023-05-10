import os
from time import sleep
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import tkinter


class image:
    def __init__(self):
        self.images = {}
        self.loader()
    
    def loader(self):
        for file in os.listdir("img"):
            self.images[file.split(".")[0]] = mpimg.imread(f"img/{file}")

    def show(self, name):
        plt.rcParams['toolbar'] = 'None'
        plt.axis('off')
        plt.imshow(self.images[name])
        plt.show(block=False)
        # sleep(2)
        plt.pause(3)
        plt.close()

# from tk import *

# # Define the function to be called when the button is clicked
# def show_message():
#     name = input_entry.get() # Get the user's input
#     message = f"Hello, {name}!" # Create the message to display
#     message_label.config(text=message) # Update the label text

# # Create the Tkinter window
# root = Tk()

# # Create the input label and entry
# input_label = tk.Label(root, text="Enter your name:")
# input_label.pack()
# input_entry = tk.Entry(root)
# input_entry.pack()

# # Create the button to submit the input
# submit_button = tk.Button(root, text="Submit", command=show_message)
# submit_button.pack()

# # Create the label to display the message
# message_label = tk.Label(root, text="")
# message_label.pack()

# # Create the label to display the image
# image_label = tk.Label(root, image=None)
# image_label.pack()

# # Start the Tkinter event loop
# root.mainloop()