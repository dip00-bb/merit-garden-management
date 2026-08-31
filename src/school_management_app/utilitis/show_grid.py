def show_grid(self,ctk,r,c):
    for row in range(r):
        for column in range(c):

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
