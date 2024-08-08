class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
    
    def check_password(self, password):
        return str (self.password) == str(password)
    
    def __str__(self):
        return f"User(username= {self.check_password}, role= {self.role})"