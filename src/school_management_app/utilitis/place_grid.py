def grid_widget(
                entry,
                r,
                c,
                py,
                px,
                direction="ew",
                colspan=1,
                rowspan=1):
    entry.grid(
        row=r, 
        column=c,
        pady=py,
        padx=px,
        sticky=direction,
        columnspan=colspan,
        rowspan=rowspan
    )
    