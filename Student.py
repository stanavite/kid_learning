class Student:

    def__init__(self,name,major,gpa, on_honor_roll)
    self.name = name
    self.major = major
    self.gpa = gpa
    self._on_honor_roll = on_honor_roll
    def on_honor_roll(self):
        if self.gpa >= 3.2:
            return True
            else:
            return False   