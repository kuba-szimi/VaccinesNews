import tkinter as tk
from datetime import date, datetime, timedelta 


#def main():
class WindowApplication(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.configure_gui()
		self.add_label()
		self.add_text_box()
		self.add_button()


	def get_time(self):
		now = datetime.now()
		if now.hour < 11:
			current_date = datetime.today() - timedelta(days=1)
		else:
			current_date = datetime.today()
		return current_date.strftime("%Y-%m-%d")

	def configure_gui(self):
		#self.master.geometry("700x400")
		self.master.title(f"Daily Vaccines News - {self.get_time()}") 

	def add_label(self):
		self.label = tk.Label(
			text = f"News on vaccines in Poland for {self.get_time()}",
			fg = "white",
			bg = "black",
			width = 55,
			height = 4,
			)
		self.label.grid(row=0, column=0)
	
	def add_text_box(self):
		self.text_box = tk.Text(
			master=self.master, 
			height=20, 
			width=55,
			fg="white",
			bg="black"
			)
		self.text_box.grid(row=1, column=0)

	def add_button(self):
		self.button = tk.Button(
			master=self.master,
			text = "Close",
			width = 20,
			height = 2,
			bg = "grey",
			fg = "black",
			command = self.master.destroy
			)
		self.button.grid(row=2,column=0)

	def display_text(self, text_content):
		self.text_box.insert(tk.END, text_content)
	


"""
window = tk.Tk()
window_app = WindowApplication(master=window)
window_app.display_text("Tutaj beda wyswietlane dane.")
tk.mainloop()

if __name__ == "__main__":
	main()
"""






