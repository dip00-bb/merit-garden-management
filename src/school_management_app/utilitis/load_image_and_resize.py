from pathlib import Path
from PIL import Image, ImageTk



def load_image_and_resize (w,h,file_name):
        base_dir = Path(__file__).resolve().parent.parent
        print("base directory::",base_dir)
        icon_path = base_dir /"assets" / file_name
        
        # open image from file path and save as a pillow image object
        pillow_image= Image.open(icon_path).resize((w,h))
        
        tkinter_image=ImageTk.PhotoImage(pillow_image)
        
        return tkinter_image