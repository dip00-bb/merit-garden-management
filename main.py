import customtkinter as ctk
from pathlib import Path
from PIL import Image, ImageTk
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # screen size
        screen_width=self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()

        self.geometry(f"{screen_width}x{screen_height}")
        self.minsize(screen_width,screen_height)

        # title
        self.title("Merit Garden Girls School And College Management")
        # icon
        base_dir = Path(__file__).resolve().parent
        icon_path = base_dir / "src" / "school_management_app" / "assets" / "merit_icon.png"

        icon_image = Image.open(icon_path)
        self.icon = ImageTk.PhotoImage(icon_image)
        self.iconphoto(True, self.icon)

if __name__=="__main__":
    app=App()
    app.mainloop()