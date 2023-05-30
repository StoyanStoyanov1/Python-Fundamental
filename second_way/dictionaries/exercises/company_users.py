class CompanyUsers:
    __company_users = {}

    def __init__(self, company_name, employees_id):
        self.company_name = company_name
        self.employees_id = employees_id
        self.add_employees_id()

    def add_employees_id(self):
        if self.company_name not in self.__company_users:
            self.__company_users[self.company_name] = []
        if self.employees_id not in self.__company_users[self.company_name]:
            self.__company_users[self.company_name].append(self.employees_id)

    @staticmethod
    def return_company_users():
        result = []
        for company_name, employees_id in CompanyUsers.__company_users.items():
            result.append(company_name)
            for id in employees_id:
                result.append(f"-- {id}")

        return "\n".join(result)


while True:
    command = input()
    if command == "End":
        print(CompanyUsers.return_company_users())
        break
    company_name, employees_id = command.split(" -> ")
    CompanyUsers(company_name, employees_id)
