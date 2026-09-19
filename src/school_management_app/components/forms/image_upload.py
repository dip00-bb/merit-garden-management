import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from PIL import Image

class ImageUpload(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        

        
        # Initialize the label without text so it remains invisible until an image is loaded
        self.image_label = ctk.CTkLabel(self, text="",width=100,height=100,bg_color="red")
        self.image_label.pack(pady=10)
        
        self.button = ctk.CTkButton(self, text="Upload Image", command=self.open_image, corner_radius=0)
        self.button.pack(pady=10)
    def open_image(self):
        file_path = filedialog.askopenfilename(
            title="Open Image File", 
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")]
        )
        if file_path:
            self.display_image(file_path)
            
    def display_image(self, file_path):
        # 1. Open the original image using PIL
        raw_image = Image.open(file_path)
        orig_width, orig_height = raw_image.size
        
        # 2. Define the maximum allowed passport-size boundaries
        max_width = 100
        max_height = 100
        
    
        
        # 4. Create the CTkImage using the safe, full-view dimensions
        photo = ctk.CTkImage(
            light_image=raw_image, 
            dark_image=raw_image, 
            size=(max_width, max_height)
        )
        
        # 5. Apply the image to the label and save the reference
        self.image_label.configure(image=photo)
        self.image_label.photo = photo  
        

        

