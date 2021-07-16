import sys
sys.path.insert(1, r'classes')

from employee import Employee


class Company(Employee):
    """
    A class to represent the company
    """

    def __init__(self):
        """
        Initialization of "company" class
        """    
        
        self.employees = dict()
        
        with open("data.txt", "r") as data:
            all_data = data.readlines()

        for employee in all_data:
            nome, sobrenome, idade, sexo, cpf, salario, cargo = employee.split(",")
            self.employees[f"{nome} {sobrenome}"] = \
                Employee(nome, sobrenome, int(idade), sexo, cpf, float(salario), cargo)

    
    def employees_info(self) -> str:
        """return a string with all employees information

        Returns:
            [str]: [person information]
        """
        keys = self.employees.keys()
        txt = ""

        for key in keys:
            print(self.employees[key].employee_info())

        return txt

    def __str__(self) -> str:
        """return a string with all employees information

        Returns:
            [str]: [person information]
        """
        return self.employees_info()

    
    def all_payment(self) -> str:
        """returns all salary together

        Returns:
            [str]: [all salary]
        """
        keys = self.employees.keys()
        value = 0

        for key in keys:
            value += (self.employees[key].salario)

        return f"O valor do salário de todos os empregados é R${value}"


if __name__ == '__main__':
    x = Company()
    print(x.all_payment())