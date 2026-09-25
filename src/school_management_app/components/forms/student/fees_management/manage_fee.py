import customtkinter as ctk
from .....utilitis import grid_widget

class ManageFee(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent,border_width=1,border_color="blue", **kwargs)



        # # Add more widgets and functionality for managing fees here
        
        # self.year_label = ctk.CTkLabel(self, text="2026", font=("Arial", 16))
        # grid_widget( entry=self.year_label, r=0, c=10, colspan=1,rowspan=1,direction="ew", px=10, py=10)        
        
        label_specs = [
            "Admission\nFee",
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "June",
            "July",
            "August",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
            "First\nTerm",
            "Second\nTerm",
            "Annual\nExam",
            "Total",
            "Paid",
            "Due",
        ]

        # =========================
        # Main table
        # =========================

        table_frame = ctk.CTkFrame(
            self,
            fg_color="transparent",
            corner_radius=0
        )
        table_frame.pack(fill="x")


        # Make every column the same width
        for column in range(len(label_specs)):
            table_frame.columnconfigure(
                column,
                weight=1,
                uniform="fee_column"
            )


        # =========================
        # Header Row
        # =========================

        for column, text in enumerate(label_specs):

            title_label = ctk.CTkLabel(
                table_frame,
                text=text,
                font=("Arial", 16),
                height=40,
                padx=5,
                border_width=1,
                corner_radius=0
            )

            grid_widget(entry=title_label, r=0, c=column, colspan=1, rowspan=1, direction="ew", px=0, py=0)


        # =========================
        # Amount Row
        # =========================

        for column, item in enumerate(label_specs):

            amount_label = ctk.CTkLabel(
                table_frame,
                text="1000",
                font=("Arial", 16),
                height=40,
                padx=5,
                border_width=1,
                corner_radius=0
            )

            grid_widget(entry=amount_label, r=1, c=column, colspan=1, rowspan=1, direction="ew", px=0, py=0)
        # =========================
        # Status Row
        # =========================
        
        for column, item in enumerate(label_specs):

            status_label = ctk.CTkLabel(
                table_frame,
                text="UNPAID",
                font=("Arial", 16),
                height=40,
                padx=5,
                border_width=1,
                corner_radius=0
            )


            
            grid_widget(entry=status_label, r=2, c=column, colspan=1, rowspan=1, direction="ew", px=0, py=0)            