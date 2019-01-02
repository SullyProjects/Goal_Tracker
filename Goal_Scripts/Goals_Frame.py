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
        self._read_data = open("main", "r")

        for line in self._read_data:
            print(line.strip())

        self._read_data.close()

    def write_file(self):
        self._write_data = open("main", "a")

        self._write_data.write("\n")
        self._write_data.write("This is new written data for later on.")

        self._write_data.close()

app =App()
app.master.title("Title")
app.mainloop()