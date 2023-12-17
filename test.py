class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

if __name__ == "__main__":
    student1 = Student("Luke", "CS", 3.6)
    student2 = Student("Tom", "Art", 3.1)
    print(student2.on_honor_roll())