import customtkinter as ctk
from ...utilitis import grid_widget

def show_grid(self):
    for row in range(24):
        for column in range(1):

            label = ctk.CTkLabel(
                self,
                text=f"{column},{row}",
                fg_color="gray",
                text_color="white"
            )

            label.grid(
                row=row,
                column=column,
                sticky="nsew",
                padx=1,
                pady=1
            )

class StudentDashboardSidebar(ctk.CTkFrame):
    def __init__(self,parent,**kwargs):
        super().__init__(parent,fg_color="red",**kwargs)
        
        self.pack_propagate(False)
        
        for i in range (24):
            self.grid_rowconfigure(i,weight=1)
            
        self.grid_columnconfigure(0,weight=1)
        
        show_grid(self)
        
        self.attendance_monitor=ctk.CTkButton(
                master=self,
                text="Custom Button",
                border_width=2,
                corner_radius=10,
                font=("Helvetica", 14),
                command=lambda: print("Clicked!")
        )
        
        grid_widget(
            entry=self.attendance_monitor,
            c=0,
            r=0,
            px=0,
            py=0,
            direction="nsew"
        )