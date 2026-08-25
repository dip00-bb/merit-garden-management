

import customtkinter as ctk

        
class TkCanvas(ctk.CTkCanvas):
    def __init__ (
                  self,
                  parent,
                  screen_width,
                  screen_height,
                  background_image,
                  **kwargs
                  ):
        super().__init__(parent,**kwargs)
        
        self.background_image=background_image
        
        self.create_image(
            screen_width/2,
            screen_height/2,
            image=self.background_image,
            anchor="center"
        )

        self.create_text(
            screen_width/2,
            screen_height/2,
            text="MERIT GARDEN GIRLS SCHOOL AND COLLEGE",
            font=("Arial",50,"bold"),
            fill="blue"
        )
