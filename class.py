class Member():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print("Name:", self.name)
        print("Username:", self.username)

members = []


name = input("name : ")
username = input("username : ")
password = input("password : ")

member = Member(name, username, password)
member.display()    


members.append(name)

for i in members:
    member.display()   







