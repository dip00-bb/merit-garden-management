from pathlib import Path
from PIL import Image, ImageTk



def load_image_and_resize (w,h,file_name):
        base_dir = Path(__file__).resolve().parent.parent
        icon_path = base_dir /"assets" / file_name
        
        print("base directory::",base_dir)
        print("icon path::", f"{base_dir /"assets"/file_name}")
        # open image from file path and save as a pillow image object
        pillow_image= Image.open(icon_path).resize((w,h))

        
        return pillow_image