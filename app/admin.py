import customtkinter as ctk
import customtkinter



class SlidePanel(ctk.CTkFrame):
	def __init__(self, parent, start_pos, end_pos):
		super().__init__(master = parent)

		# general attributes 
		self.start_pos = start_pos + 0.04
		self.end_pos = end_pos - 0.06
		self.width = abs(start_pos - end_pos)

		# animation logic
		self.pos = self.start_pos
		self.in_start_pos = True

		# layout
		self.place(relx = self.start_pos, rely = 0.05, relwidth = self.width, relheight = 0.9)

	def animate(self):
		if self.in_start_pos:
			self.animate_forward()
		else:
			self.animate_backwards()
			

	def animate_forward(self):
		if self.pos > self.end_pos:
			self.pos -= 0.008
			self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
			self.after(4, self.animate_forward)
		else:
			self.in_start_pos = False

	def animate_backwards(self):
		if self.pos < self.start_pos:
			self.pos += 0.008
			self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
			self.after(4, self.animate_backwards)
		else:
			self.in_start_pos = True



window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400')


animated_panel = SlidePanel(window, 1.0, 0.10)    
slide = ctk.CTkFrame(animated_panel, height=120, width=300, corner_radius = 0)
slide.pack(pady = 10)

entry = customtkinter.CTkEntry(master=slide, width=220, height=30, placeholder_text='just trying something')
entry.place(x=60, y=50)


button = ctk.CTkButton(window, text = 'toggle sidebar', command = animated_panel.animate)
button.place(relx = 0.5, rely = 0.5, anchor = 'center')


window.mainloop()