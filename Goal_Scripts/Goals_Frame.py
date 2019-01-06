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
        self._new_goal = Button(self, text="New File", command=self.new_file)
        self._add_data = Button(self,text="Add Data", command=self.add_data)

        self._button1.grid(row=0, column=0)
        self._button2.grid(row=1, column=0)
        self._new_goal.grid(row=3, column=0)
        self._add_data.grid(row=4, column=0)

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

    def new_file(self):
        try:
            self._find.destroy()
            self._loc_file.destroy()

        except AttributeError:
            pass

        self._new_file_name = Entry(self)
        self._new_file_name.grid(row=3, column=1)

        self._OK_Button = Button(self, text="OK", command=self.create_new_file)
        self._OK_Button.grid(row=3, column=2)

    def create_new_file(self):
        self._file_name = self._new_file_name.get() + ".txt"
        self._new_file = open(self._file_name, "w")

        self._create_message = Label(self, text="New Goal File has been created.")
        self._create_message.grid(row=4, column=0)

        try:
            self._OK_Button.destroy()
            self._new_file_name.destroy()

        except AttributeError:
            pass

        self._new_file.close()

    def add_data(self):
        try:
            self._OK_Button.destroy()
            self._new_file_name.destroy()
        except AttributeError:
            pass

        try:
            self._create_message.destroy()

        except AttributeError:
            pass

        self._loc_file = Entry(self)
        self._loc_file.grid(row=4, column=1)

        self._find = Button(self, text="Find", command=self.find_file)
        self._find.grid(row=4, column=2)

    def find_file(self):
        try:
            self._error_message.destroy()
        except AttributeError:
            pass

        file_name = self._loc_file.get()
        try:
            self._use_file = open(file_name, "r")
            self._found_message = Label(self, text="File found, what would you like to do with it?")
            self._found_message.grid(row=5, column=1)

        except FileNotFoundError:
            self._error_message = Label(self, text="File Not found, Please Try Again.")
            self._error_message.grid(row=5, column=1)

app =App()
app.master.title("Title")
app.mainloop()