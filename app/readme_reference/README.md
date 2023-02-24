### Creating Modern GUI (Graphical user interface) using customtkinter

## The user or Company using this App is (DS Enterprise located in Ho)

   ##   Function or the purpose of the application   ##
1. this App is to enable them or help them to keep daily record, sales etc.


def dashexit(self)-> None:
        if messagebox.askyesno('Logout', 'Please remember to save\nyour works\nDo you want to exit', icon='warning'):
            homepage.Homepage(self.dash)
            self.dash.destroy()
            sys.exit()
        else:
            self.dash = self.dash