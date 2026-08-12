class Login:
    def authenticate(self, username, password):
        if username == "admin" and password == "1234":
            return "Login successful"

        return "Invalid username or password"

login = Login()
print(login.authenticate("admin", "1234"))