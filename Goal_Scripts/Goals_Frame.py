from tkinter import *
#from Goal_Scripts import Goal_Functions


class App(Frame):
    def __init__(self, master=None):
        super(App, self).__init__(master)
        self.grid()
        self.MM()

    def MM(self):
        self._button1 = Button(self, text="button1", command=self.read_file)
        self._button2 = Button(self, text="button2", command=self.write_file)

        self._button1.grid(row=0, column=0)
        self._button2.grid(row=1, column=0)

    def read_file(self):
        pass

    def write_file(self):
        pass

app =App()
app.master.title("Title")
app.mainloop()