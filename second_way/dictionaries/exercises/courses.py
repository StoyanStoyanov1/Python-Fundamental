class Courses:
    __book_courses = {}

    def __init__(self, course, name):
        self.course = course
        self.name = name
        self.add_course()

    def add_course(self):
        if self.course not in self.__book_courses:
            self.__book_courses[self.course] = []
        self.__book_courses[self.course].append(self.name)

    @staticmethod
    def result():
        result = []
        for course, names in Courses.__book_courses.items():
            result.append(f"{course}: {len(names)}")
            for name in names:
                result.append(f"-- {name}")

        return "\n".join(result)


while True:
    command = input()
    if command == "end":
        print(Courses.result())
        break
    course, name = command.split(" : ")
    Courses(course, name)
