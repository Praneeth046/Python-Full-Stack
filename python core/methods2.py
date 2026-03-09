class Student:
    total_students=0
    passing_marks=40
    def __init__ (self,name,marks):
        self.name=name
        self.marks=marks
        Student.total_students+=1
    def result(self):
        if self.marks >= Student.passing_marks:
            return "Pass"
        else:
            return "Fail"

    def curve_marks(self,percent):
        self.marks=self.marks+(self.marks * percent/100)
    @staticmethod
    def grades(marks):
        if marks>=90:
            return"A"
        elif marks>=80:
            return"B"
        elif marks>=60:
            return"c"
        elif marks>=50:
            return"D"
        elif marks>=40:
            return"E"
        else:
            return"F"
s1=Student("ram",82)
# s2=Student("sai",56)
# s3=Student("shiva",91)
s1.curve_marks(10)
print(s1.name,s1.marks)
print(s1.result())
print(Student.grades(s1.marks))



