import pandas
from cryptography.fernet import Fernet


class Manager:
    def __init__(self, security_file, passwords_path):
        self.security_file = security_file
        self.passwords_path = passwords_path
        self.masterpass = None
        self.key = None
        self.load_or_initialise_security_file()

    def load_or_initialise_security_file(self):
        try:
            security_data = pandas.read_csv(self.security_file)
            self.key = security_data.loc[0, "key"].encode("utf-8")
            self.masterpass = self.decrypt_data(security_data.loc[0, "masterpass"])
        except FileNotFoundError:
            self.initialise_security_file()

    def initialise_security_file(self):
        self.key = Fernet.generate_key()
        self.masterpass = input("Enter a new master-password: ")
        encrypted_masterpass = self.encrypt_data(self.masterpass)
        security_file = {"masterpass": [encrypted_masterpass], "key": [self.key.decode("utf-8")]}
        pandas.DataFrame(security_file).to_csv(self.security_file, index=False, mode="w")


    def encrypt_data(self, data):
        f = Fernet(self.key)
        encrypted_data = f.encrypt(data.encode("utf-8"))
        return encrypted_data.decode("utf-8")

    def decrypt_data(self, data):
        f = Fernet(self.key)
        decrypted_data = f.decrypt(data.encode("utf-8")).decode("utf-8")
        return decrypted_data

    def login(self, entered_password):
        return self.masterpass == entered_password

    def save_password(self, user):
        new_user = {"username": self.encrypt_data(user[0]), "password": self.encrypt_data(user[1]),
                    "email": self.encrypt_data(user[2])}
        passwords_dataframe = pandas.read_csv(self.passwords_path)
        new_user_dataframe = pandas.DataFrame([new_user])
        passwords_dataframe = pandas.concat([passwords_dataframe, new_user_dataframe], ignore_index=True)
        passwords_dataframe.to_csv(self.passwords_path, index=False)

    def delete_password(self, user):
        username_encrypted = user[0]
        password_encrypted = user[1]
        email_encrypted = user[2]

        password_dataframe = pandas.read_csv(self.passwords_path)

        decrypted_usernames = password_dataframe["username"].apply(self.decrypt_data)
        decrypted_passwords = password_dataframe["password"].apply(self.decrypt_data)
        decrypted_emails = password_dataframe["email"].apply(self.decrypt_data)

        mask = (decrypted_usernames == username_encrypted) & \
               (decrypted_passwords == password_encrypted) & \
               (decrypted_emails == email_encrypted)

        if mask.any():
            password_dataframe = password_dataframe[~mask]
            password_dataframe.to_csv(self.passwords_path, index=False)  # Saving to csv
            print("Deleted")
        else:
            print("No user found!")

    def edit_password(self, old_user, new_user):
        old_username = old_user[0]
        old_password = old_user[1]
        old_email = old_user[2]
        new_username = self.encrypt_data(new_user[0])
        new_password = self.encrypt_data(new_user[1])
        new_email = self.encrypt_data(new_user[2])

        password_dataframe = pandas.read_csv(self.passwords_path)

        decrypted_usernames = password_dataframe["username"].apply(self.decrypt_data)
        decrypted_passwords = password_dataframe["password"].apply(self.decrypt_data)
        decrypted_emails = password_dataframe["email"].apply(self.decrypt_data)

        mask = (decrypted_usernames == old_username) & \
               (decrypted_passwords == old_password) & \
               (decrypted_emails == old_email)

        if mask.any():
            password_dataframe.loc[mask, "username"] = new_username
            password_dataframe.loc[mask, "password"] = new_password
            password_dataframe.loc[mask, "email"] = new_email
            password_dataframe.to_csv(self.passwords_path, index=False)
            print("Edited Successfully")
        else:
            print("Failed to edit")

    def get_users(self):
        users_data = pandas.read_csv(self.passwords_path)
        users = [{"username": self.decrypt_data(user["username"]), "password": self.decrypt_data(user["password"]),
                  "email": self.decrypt_data(user["email"])} for _, user in users_data.iterrows()]
        return users
