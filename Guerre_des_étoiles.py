import tkinter as tk
import random as rd

class AppliCanevas(tk.Tk):
    def __init__(self):
        '''
        Initializes a Tkinter application creating a canvas to draw circles and lines randomly.

        Attributes:
            size (int): The size of the canvas.
        '''
        tk.Tk.__init__(self)
        self.size = 500
        self.create_widgets()

    def create_widgets(self):
        '''
        Creates canvas and buttons within the application window.
        '''
        # Canvas creation
        self.canv = tk.Canvas(self, bg="light gray", height=self.size,
                              width=self.size)
        self.canv.pack(side=tk.LEFT)

        # Buttons
        self.button_circles = tk.Button(self, text="Draw Circles",
                                        command=self.draw_circles)
        self.button_circles.pack(side=tk.TOP)
        self.button_lines = tk.Button(self, text="Draw Lines",
                                      command=self.draw_lines)
        self.button_lines.pack()
        self.button_quit = tk.Button(self, text="Quit",
                                     command=self.quit)
        self.button_quit.pack(side=tk.BOTTOM)

    def random_color(self):
        '''
        Randomly selects a color from a list of predefined colors.

        Returns:
            str: A randomly chosen color.
        '''
        return rd.choice(("black", "red", "green", "blue", "yellow", "magenta",
                          "cyan", "white", "purple"))

    def draw_circles(self):
        '''
        Draws circles on the canvas at random positions with random colors and sizes.
        '''
        for i in range(20):
            x, y = [rd.randint(1, self.size) for j in range(2)]
            diameter = rd.randint(1, 50)
            self.canv.create_oval(x, y, x+diameter, y+diameter,
                                  fill=self.random_color())

    def draw_lines(self):
        '''
        Draws lines on the canvas at random positions with random colors.
        '''
        for i in range(20):
            x, y, x2, y2 = [rd.randint(1, self.size) for j in range(4)]
            self.canv.create_line(x, y, x2, y2, fill=self.random_color())


if __name__ == "__main__":
    app = AppliCanevas()
    app.title("My Psychedelic Canvas!")
    app.mainloop()
