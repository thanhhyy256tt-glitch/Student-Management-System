class Account:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def to_string(self):
        return f"{self.username},{self.password},{self.role}\n"

    @staticmethod
    def from_string(line):
        parts = line.strip().split(",")
        if len(parts) == 3:
            return Account(parts[0], parts[1], parts[2])
        return None
