def grid_widget(
                entry,
                r,
                c,
                py,
                px,
                direction="ew",
                colspan=1,
                rowspan=1,
                ipadx=0,
                ipady=0
                ):
    entry.grid(
        row=r, 
        column=c,
        pady=py,
        padx=px,
        sticky=direction,
        columnspan=colspan,
        rowspan=rowspan,
        ipadx=ipadx,
        ipady=ipady
    )
    