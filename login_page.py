from tkinter import Entry, Button, Label


class LoginPage:
    def __init__(self, manager, load_main_page, window):
        self.window = window
        self.login_label = Label(self.window, text="Password")
        self.password_input_field = Entry(self.window)
        self.login_button = Button(self.window, text="Login", command=self.login)
        self.manager = manager
        self.load_main_page = load_main_page

    def setup(self):
        self.window.title("Password Manager")
        self.window.minsize(width=500, height=250)
        self.window.config(padx=150, pady=150)

        self.login_label.grid(row=0, column=0)
        self.password_input_field.grid(row=0, column=1)
        self.login_button.grid(row=1, column=1)

    def login(self):
        password = self.password_input_field.get()
        if password:
            if self.manager.login(password):
                print("Logged In")
                self.remove_widgets()
                self.load_main_page()
            else:
                print("Incorrect Password")
        else:
            print("Enter a password!")

    def remove_widgets(self):
        self.login_label.grid_forget()
        self.login_button.grid_forget()
        self.password_input_field.grid_forget()