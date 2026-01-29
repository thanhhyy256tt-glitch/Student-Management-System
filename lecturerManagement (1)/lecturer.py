class Lecturer:
    def __init__(self, lecturer_id, name, password, department):
        self.lecturer_id = lecturer_id
        self.name = name
        self.password = password
        self.department = department

    # chuyển object → list (để lưu txt)
    def to_list(self):
        return [
            self.lecturer_id,
            self.name,
            self.password,
            self.department
        ]

