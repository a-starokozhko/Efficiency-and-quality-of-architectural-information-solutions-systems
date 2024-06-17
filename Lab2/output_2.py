class UserType:
    ENGINEER = 1
    MANAGER = 2    

class User:
    def __init__(self, name, age, user_type, phone, phone_code):
        self.name = name
        self.age = age
        self.user_type = user_type
        self.phone = phone
        self.phone_code = phone_code

    def print_details(self):
        # Виведення інформації про користувача
        print("Name:", self.name)
        print("Age:", self.age)
        print("Type:", self.get_user_type())
        print("Phone:", self.get_full_phone_number())

    def get_user_type(self):
        if self.user_type == UserType.ENGINEER:
            return "Engineer"
        elif self.user_type == UserType.MANAGER:
            return "Manager"
        else:
            return "Unknown"

    def get_full_phone_number(self):
        return f"{self.phone_code}{self.phone}"

# Приклад використання класу
user = User("John", 25, UserType.ENGINEER, "9379992", "050")
user.print_details()