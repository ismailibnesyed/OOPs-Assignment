class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.max_attempts = 3

    def login(self, entered_username, entered_password):

        if (
            self.username == entered_username
            and self.password == entered_password
        ):
            return True

        return False