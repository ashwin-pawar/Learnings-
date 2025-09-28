from  itertools import cycle #infinte loop 
from time import sleep
import time
from PIL import Image, ImageTk #load and manipulation images
import tkinter as tk #library hai 


root = tk.Tk()
#tittle of Window

root.title("Python images slideshow Viwers")

#importing images by their path

image_paths = [
            r"C:\Users\Ashwin\OneDrive\Pictures\Screenshots\Screenshot 2025-09-07 231048.png",
            r"C:\Users\Ashwin\OneDrive\Pictures\Screenshots\Screenshot 2025-09-07 231558.png",
            r"C:\Users\Ashwin\OneDrive\Pictures\Screenshots\Screenshot 2025-09-07 232047.png",
            r"C:\Users\Ashwin\OneDrive\Pictures\Screenshots\Screenshot 2025-09-07 232404.png",
            r"C:\Users\Ashwin\OneDrive\Pictures\Screenshots\Screenshot 2025-09-07 234814.png",
            r"C:\Users\Ashwin\OneDrive\Pictures\Screenshots\Screenshot 2025-09-07 235701.png",
            r"C:\Users\Ashwin\OneDrive\Pictures\Screenshots\Screenshot 2025-09-08 032944.png",
            r"C:\Users\Ashwin\OneDrive\Pictures\Screenshots\Screenshot 2025-09-08 041347.png",
            r"C:\Users\Ashwin\OneDrive\Pictures\Screenshots\Screenshot 2025-09-08 155715.png",
            r"C:\Users\Ashwin\OneDrive\Pictures\Screenshots\Screenshot 2025-09-08 163632.png",
            r"C:\Users\Ashwin\OneDrive\Pictures\Screenshots\Screenshot 2025-09-08 232853.png",
            r"C:\Users\Ashwin\OneDrive\Pictures\Screenshots\Screenshot 2025-09-09 182712.png",
            r"C:\Users\Ashwin\OneDrive\Pictures\Screenshots\Screenshot 2025-09-09 190708.png",
            r"C:\Users\Ashwin\OneDrive\Pictures\Screenshots\Screenshot 2025-09-09 193327.png",

             ]


#resize the images into 1080x1080 

image_size =(1280,720)
images =[Image.open(path).resize(image_size) for path in image_paths]
Photo_images = [ImageTk.PhotoImage(image) for image in images]

#label for images 
label = tk.Label(root)
label.pack ()

# fucntion for updatung image label in window
def update_image():
      for Photo_image in Photo_images:
          label.config(image=Photo_image)
          label.update()
          time.sleep(3)


slideshow = cycle(Photo_images)
def Start_slideshow():
   for _ in range(len(Photo_images)):
      update_image()

#adding button to start slideshow
play_button =tk.Button(root, text='Play Slideshow', command=Start_slideshow)
play_button.pack()

#Infinite Loop so our Slideshow will not close

root.mainloop()