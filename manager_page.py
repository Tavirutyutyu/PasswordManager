from tkinter import Entry, Button, Label, ttk


class ManagerPage:
    def __init__(self, manager, window):
        self.window = window
        self.tree = ttk.Treeview(self.window, columns=("username", "password", "email"), show="headings")
        self.username_field = Entry(self.window)  # Specify self.window as parent
        self.username_label = Label(self.window, text="Username")  # Specify self.window as parent
        self.password_field = Entry(self.window)  # Specify self.window as parent
        self.password_label = Label(self.window, text="Password")  # Specify self.window as parent
        self.email_field = Entry(self.window)  # Specify self.window as parent
        self.email_label = Label(self.window, text="Email")  # Specify self.window as parent
        self.add_new_user_button = Button(self.window, text="Add New", command=self.add_or_edit_user)  # Specify self.window
        self.delete_user_button = Button(self.window, text="Delete", command=self.delete_user)  # Specify self.window
        self.manager = manager

    def setup(self):
        self.window.title("Password Manager")
        self.window.minsize(width=500, height=250)
        self.window.config(padx=50, pady=50)
        self.tree.heading("username", text="Username")
        self.tree.heading("password", text="Password")
        self.tree.heading("email", text="Email")
        for user in self.manager.get_users():
            self.tree.insert("", "end", values=(user["username"], user["password"], user["email"]))
        self.tree.bind("<Double-1>", self.on_double_click)
        self.tree.grid(row=0, column=1)
        self.username_field.grid(row=2, column=0)
        self.username_label.grid(row=1, column=0)
        self.password_field.grid(row=2, column=1)
        self.password_label.grid(row=1, column=1)
        self.email_field.grid(row=2, column=2)
        self.email_label.grid(row=1, column=2)
        self.add_new_user_button.grid(row=3, column=1)
        self.delete_user_button.grid(row=0, column=2)

    def on_double_click(self, _):
        selected_item = self.tree.focus()
        if selected_item:
            values = self.tree.item(selected_item, "values")
            username, password, email = values

            self.username_field.delete(0, "end")
            self.username_field.insert(0, username)
            self.password_field.delete(0, "end")
            self.password_field.insert(0, password)
            self.email_field.delete(0, "end")
            self.email_field.insert(0, email)
            self.add_new_user_button.config(text="Edit User")

    def add_or_edit_user(self):
        username = self.username_field.get()
        password = self.password_field.get()
        email = self.email_field.get()

        if username and password and email:
            selected_item = self.tree.focus()
            if selected_item:
                old_user = self.tree.item(selected_item, "values")
                new_user = (username, password, email)
                self.manager.edit_password(old_user, new_user)
                self.tree.item(selected_item, values=(username, password, email))
                self.add_new_user_button.config(text="Add New")
            else:
                self.tree.insert("", "end", values=(username, password, email))
                self.manager.save_password((username, password, email))

            self.username_field.delete(0, "end")
            self.password_field.delete(0, "end")
            self.email_field.delete(0, "end")

    def delete_user(self):
        selected_item = self.tree.focus()
        if selected_item:
            values = self.tree.item(selected_item, "values")
            self.tree.delete(selected_item)
            self.manager.delete_password(values)
