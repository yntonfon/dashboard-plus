class Account:
    def __init__(self, username, email, hash_password, email_confirmed):
        self.email = email
        self.username = username
        self.hash_password = hash_password
        self.email_confirmed = email_confirmed
