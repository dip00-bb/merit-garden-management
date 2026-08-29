def show_grid(self,ctk):
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
