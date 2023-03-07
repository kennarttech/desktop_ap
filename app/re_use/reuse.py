print_data = customtkinter.CTkButton(master=middle_frame, text='Print Data',
                                                   text_color=("white"), 
                                                   fg_color=self.user_data['theme3'],
                                                   hover_color=("gray70", "gray30"), 
                                                   height=30, width=106, anchor='S',
                                                   corner_radius=4, border_width=1,
                                                   font=('Roboto', 16),command=None)
        print_data.grid(row=7, column=3, padx=(0, 130), pady=(140, 10), sticky='e')


        submit_button = customtkinter.CTkButton(master=middle_frame, text='Save Record',
                                                   text_color=("white"), 
                                                   fg_color=self.user_data['theme2'],
                                                   hover_color=("gray70", "gray30"), 
                                                   height=30, width=106, anchor='S',
                                                   corner_radius=4, border_width=1,
                                                   font=('Roboto', 16),command=None)
        submit_button.grid(row=7, column=3, padx=(30, 10), pady=(140, 10), sticky='e')