
class Student:

    def __init__(self, student_nr: int, student_name: str,
                 student_residence: str, student_age: int)->None:
        self._student_nr = student_nr
        self.age = student_age
        self.name = student_name
        self.residence = student_residence

    @property
    def student_nr(self)->int:
        print('using getter')
        return self._student_nr

    @student_nr.setter
    def student_nr(self, student_nr: int)->None:
        print('using setter')
        self._student_nr = student_nr

    def set_age(self, new_age: int)->None:
        self.age = new_age

    def get_age(self)->int:
        return self.age

def main()->None:
    student = Student(1, 'Mies', 'Den Haag', 2)
    print(student.student_nr)
    student.student_nr = 13

    pass

if __name__ == '__main__':
    main()
