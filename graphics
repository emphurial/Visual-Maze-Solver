from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = ""
        self.canvas = Canvas(self, bg="white")
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()
        print("The window closed.")
    
    def close(self):
        self.running = False