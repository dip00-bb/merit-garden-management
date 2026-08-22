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
        self.resizable(False,False)

        # title
        self.title("Merit Garden Girls School And College Management")

        # icon
        base_dir = Path(__file__).resolve().parent
        icon_path = base_dir / "src" / "school_management_app" / "assets" / "merit_icon.png"

        icon_image = Image.open(icon_path)
        self.icon = ImageTk.PhotoImage(icon_image)
        # self.wm_iconphoto(True, self.icon)
        self.iconphoto(True, self.icon)

        welcome_canvas=ctk.CTkCanvas(self,
                                     height=screen_height,
                                     width=screen_width,
                                     bg="black",
                                     highlightthickness=0
                                     )

        welcome_canvas.pack()
        welcome_canvas.create_image(
      0,
            0,
            image=self.icon,
            anchor="center",

        )
        welcome_canvas.create_text(
            screen_width/2,screen_height/2,
            text="MERIT GARDEN GIRLS SCHOOL AND COLLEGE",
            font=("Arial",50,"bold"),
            fill="sky blue"
        )


if __name__=="__main__":
    app=App()
    app.mainloop()