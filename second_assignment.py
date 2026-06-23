class FileBank:

    def __init__(self):
        self.filename = "userlist.txt"
        self.users = self.load_file()

    # ---------------- LOAD FILE -> DICT ----------------
    def load_file(self):
        users = {}

        try:
            file = open(self.filename, "r")

            for line in file:
                data = line.strip().split(",")

                if len(data) == 4:
                    user_id = int(data[0])
                    username = data[1]
                    password = data[2]
                    amount = int(data[3])

                    users[user_id] = {
                        "username": username,
                        "password": password,
                        "amount": amount
                    }

            file.close()

        except FileNotFoundError:
            pass

        return users

    # ---------------- SAVE DICT -> FILE ----------------
    def save_file(self):
        file = open(self.filename, "w")

        for uid in self.users:
            u = self.users[uid]
            line = f"{uid},{u['username']},{u['password']},{u['amount']}\n"
            file.write(line)

        file.close()

    # ---------------- REGISTER ----------------
    def register(self):
        print("\n----- REGISTER -----")

        username = input("Enter username: ")
        password = input("Enter password: ")
        amount = int(input("Enter amount: "))

        user_id = len(self.users) + 1

        self.users[user_id] = {
            "username": username,
            "password": password,
            "amount": amount
        }

        self.save_file()

        print("Registration successful!")

    # ---------------- LOGIN ----------------
    def login(self):
        print("\n----- LOGIN -----")

        username = input("Enter username: ")
        password = input("Enter password: ")

        user_id = self.check_user(username, password)

        if user_id:
            print("Login successful!")
            self.menu(user_id)
        else:
            print("Login failed!")

    def check_user(self, username, password):
        for uid in self.users:
            if self.users[uid]["username"] == username and self.users[uid]["password"] == password:
                return uid
        return None

    # ---------------- MENU ----------------
    def menu(self, user_id):
        while True:
            print("\n1-Transfer")
            print("2-Withdraw")
            print("3-Update")
            print("4-Logout")

            choice = input("Choose: ")

            if choice == "1":
                self.transfer(user_id)

            elif choice == "2":
                self.withdraw(user_id)

            elif choice == "3":
                self.update(user_id)

            elif choice == "4":
                break

            else:
                print("Invalid")

    # ---------------- TRANSFER ----------------
    def transfer(self, user_id):
        to_user = input("Transfer username: ")
        to_id = self.find_user(to_user)

        if to_id is None:
            print("User not found")
            return

        amount = int(input("Enter amount: "))

        if self.users[user_id]["amount"] < amount:
            print("Not enough balance")
            return

        self.users[user_id]["amount"] -= amount
        self.users[to_id]["amount"] += amount

        self.save_file()
        print("Transfer successful")

    def find_user(self, username):
        for uid in self.users:
            if self.users[uid]["username"] == username:
                return uid
        return None

    # ---------------- WITHDRAW ----------------
    def withdraw(self, user_id):
        amount = int(input("Enter withdraw: "))

        if self.users[user_id]["amount"] < amount:
            print("Not enough balance")
            return

        self.users[user_id]["amount"] -= amount
        self.save_file()

        print("Withdraw successful")
        # ---------------- UPDATE (FILE BASED) ----------------
    def update(self, user_id):
        print("\n1-Name change")
        print("2-Password change")
        print("3-Amount change")

        choice = input("Choose: ")

        if choice == "1":
            new_name = input("New name: ")
            self.users[user_id]["username"] = new_name

        elif choice == "2":
            new_pw = input("New password: ")
            self.users[user_id]["password"] = new_pw

        elif choice == "3":
            new_amount = int(input("New amount: "))
            self.users[user_id]["amount"] = new_amount

        else:
            print("Invalid")

        self.save_file()
        print("Updated successfully")

    # ---------------- MAIN MENU ----------------
def main(self):
        while True:
            print("\n===== FILE BANK =====")
            print("1-Login")
            print("2-Register")
            print("3-Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.login()
            elif choice == "2":
                self.register()
            elif choice == "3":
                break
            else:
                print("Invalid")


# ---------------- RUN ----------------
if __name__ == "__main__":
    app = FileBank()

    while True:
        print("\n===== FILE BANK SYSTEM =====")
        print("1 - Login")
        print("2 - Register")
        print("3 - Exit")

        choice = input("Choose: ")

        if choice == "1":
            app.login()
        elif choice == "2":
            app.register()
        elif choice == "3":
            break
        else:
            print("Invalid choice")