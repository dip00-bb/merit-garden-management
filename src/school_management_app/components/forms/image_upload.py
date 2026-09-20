import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from ...utilitis import image_to_binary
class ImageUpload(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        # binary image data
        
        self.image_data=""

        # Initialize the label without text so it remains invisible until an image is loaded
        self.image_label = ctk.CTkLabel(self, text="",width=100,height=100,bg_color="red")
        self.image_label.pack(pady=10)
        
        self.button = ctk.CTkButton(self, text="Upload Image", command=self.open_image, corner_radius=0)
        self.button.pack(pady=10)
        
        
    def open_image(self):
        file_path = filedialog.askopenfilename(
            title="Open Image File", 
            filetypes=[("Image files", "*.png *.jpg *.jpeg")]
        )
        if file_path:
            self.display_image(file_path)
            self.image_path=file_path
            
  
    def display_image(self, file_path):
        print(file_path)
        # 1. Open the original image using PIL
        raw_image = Image.open(file_path)
        # 2. Define the maximum allowed passport-size boundaries
        max_width = 100
        max_height = 100
        
        blob_image_data=image_to_binary(file_path)
        self.image_data=blob_image_data
        # 3. Create the CTkImage using the safe, full-view dimensions
        photo = ctk.CTkImage(
            light_image=raw_image, 
            dark_image=raw_image, 
            size=(max_width, max_height)
        )
        
        # 4. Apply the image to the label and save the reference
        self.image_label.configure(image=photo)
        self.image_label.photo = photo  
