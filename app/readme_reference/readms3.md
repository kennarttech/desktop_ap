# self.new_frame.mainloop()


    def new_frameexit(self)-> None:
        if messagebox.askyesno('Logout', 'Please remember to save\nyour works\nDo you want to exit', icon='warning'):
            homepage.Homepage(self.new_frame)
            self.new_frame.destroy()
            sys.exit()
        else:
            self.new_frame = self.new_frame



    def Dsales(self):
        if messagebox.askyesno('Logout', 'Are you sure you want to exit', icon='info'):
            dashboard.Dashboard()
            self.new_frame.destroy()
        else:
            self.new_frame = self.



-------------------------------------

def gotonewf(self):
        if messagebox.askyesno('New frame', 'New frame!\nremember to save your work after you finish', icon='info'):
            newframes.Newframe()
            self.dash.destroy()
        else:
            self.dash = self.dash




    def nothing(self):
        if messagebox.showinfo('Dashbord', 'Already hear😀😀', icon='info'):
            return self.dash
-----------------------------------------------------------------


def gotonewf(self):
        if messagebox.askyesno('New frame', 'Welcome to users dashboard\nDo you want to proceed', icon='info'):
            newframes.Newframe()
            self.admin__a.destroy()
        else:
            self.admin__a = self.admin__a



    def usrnothing(self):
        if messagebox.askyesno('admin__abord', 'Users page', icon='info'):
            dashboard.Dashboard()
            self.admin__a.destroy()
        else:
            self.admin__a = self.admin__a