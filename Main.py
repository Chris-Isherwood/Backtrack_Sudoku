import tkinter as tk

class MainApplication:
    def __init__(self):
        #Construct the window
        self.root = tk.Tk()
        self.root.title('Sudoku')
        self.background = '#1788AD'
        self.width = round(self.root.winfo_screenheight() * 0.75)
        self.height = round(self.root.winfo_screenheight() * 0.75)
        self.xOffset = round(self.root.winfo_screenwidth() * 0.5) - round(self.root.winfo_screenheight() * 0.375)
        self.yOffset = round(self.root.winfo_screenheight() * 0.1)
        self.root.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.xOffset, self.yOffset))
        self.frame = tk.Frame(self.root, width = self.width, height = self.height, background = self.background)
        self.frame.place(x = 0, y = 0)

class Sudoku():
    def __init__(self, master):
        self.root = master

        self.Title = tk.Label(self.root.frame, text = 'Sudoku', background = self.root.background, font = 'Helvetica 30')
        self.Title.place(relx = 0.5, rely = 0.1, anchor = 'center')

        self.width = self.root.width // 2
        self.height = self.root.height // 2
        self.canvas = tk.Canvas(self.root.frame, width = self.width, height = self.height, background = 'white')
        self.canvas.place(x = self.root.width // 4, y = self.root.height // 4)

        self.grid = [
            #Horizontal Thin Lines
            self.canvas.create_line(1 * self.width // 9, 0, 1 * self.width // 9, self.height, width = 1, fill = 'grey'),
            self.canvas.create_line(2 * self.width // 9, 0, 2 * self.width // 9, self.height, width = 1, fill = 'grey'),
            self.canvas.create_line(4 * self.width // 9, 0, 4 * self.width // 9, self.height, width = 1, fill = 'grey'),
            self.canvas.create_line(5 * self.width // 9, 0, 5 * self.width // 9, self.height, width = 1, fill = 'grey'),
            self.canvas.create_line(7 * self.width // 9, 0, 7 * self.width // 9, self.height, width = 1, fill = 'grey'),
            self.canvas.create_line(8 * self.width // 9, 0, 8 * self.width // 9, self.height, width = 1, fill = 'grey'),
            #Vertical Thin Lines
            self.canvas.create_line(0, 1 * self.height // 9, self.width, 1 * self.height // 9, width = 1, fill = 'grey'),
            self.canvas.create_line(0, 2 * self.height // 9, self.width, 2 * self.height // 9, width = 1, fill = 'grey'),
            self.canvas.create_line(0, 4 * self.height // 9, self.width, 4 * self.height // 9, width = 1, fill = 'grey'),
            self.canvas.create_line(0, 5 * self.height // 9, self.width, 5 * self.height // 9, width = 1, fill = 'grey'),
            self.canvas.create_line(0, 7 * self.height // 9, self.width, 7 * self.height // 9, width = 1, fill = 'grey'),
            self.canvas.create_line(0, 8 * self.height // 9, self.width, 8 * self.height // 9, width = 1, fill = 'grey'),
            #Horizontal Thick Lines
            self.canvas.create_line(0, 6 * self.height // 9, self.width, 6 * self.height // 9, width = 3),
            self.canvas.create_line(3 * self.width // 9, 0, 3 * self.width // 9, self.height, width = 3),
            #Vertical Thick Lines
            self.canvas.create_line(6 * self.width // 9, 0, 6 * self.width // 9, self.height, width = 3),
            self.canvas.create_line(0, 3 * self.height // 9, self.width, 3 * self.height // 9, width = 3),
        ]

        self.sudoku = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

    def gridLocation(self, eventorigin):
        x = 1 + int(9 * eventorigin.x // self.width)
        y = 1 + int(9 * eventorigin.y // self.height)
        print(x, y)

#Run the application
if __name__ == '__main__':
    Application = MainApplication()
    test = Sudoku(Application)
    test.canvas.bind('<Button-1>', test.gridLocation)
    Application.root.mainloop()