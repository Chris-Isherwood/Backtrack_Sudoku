import tkinter as tk

class MainApplication:
    def __init__(self, master):
        self.master = master
        self.width = master.winfo_screenheight() // 2
        self.height = master.winfo_screenheight() // 2
        master.title('Sudoku')
        master.geometry('{}x{}'.format(self.width, self.height))

root = tk.Tk()
Application = MainApplication(root)
root.mainloop()