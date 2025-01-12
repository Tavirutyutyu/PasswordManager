from login_page import LoginPage
from manager import Manager
from manager_page import ManagerPage
from tkinter import Tk

window = Tk()
manager = Manager("security.csv", "definitely_not_passwords.csv")
main_page = ManagerPage(manager, window)
login_page = LoginPage(manager, main_page.setup, window)
login_page.setup()

window.mainloop()