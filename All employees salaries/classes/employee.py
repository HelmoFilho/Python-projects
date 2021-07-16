"""
2. Implemente uma classe para representar um Empregado, 
utilizando herança e a classe Pessoa do item 1. 
O Empregado tem como atributos adicionais um salário e um cargo.
"""

from person import Pessoa


class Employee(Pessoa):
    """
    A class to represent a employee
    """

    def __init__(self, nome: str, sobrenome: str, idade: int, sexo: str, cpf: str, salario: float, cargo: str):
        """Initialization of "employee" class

        Args:
            nome (str): [name]
            sobrenome (str): [surname]
            idade (int): [age]
            sexo (str): [sex]
            cpf (str): [cpf]
            salario (float): [salary]
            cargo (str): [cargo]
        """
        super().__init__(nome, sobrenome, idade, sexo, cpf)
        self.salario = salario
        self.cargo = cargo


    @classmethod
    def from_string(cls, employee_data):
        """create class from string

        Args:
            employee_data (str): string with person information

        Returns:
            [class]: person class
        """
        nome, sobrenome, idade, sexo, cpf, salario, cargo = employee_data.split(",")
        return cls(nome, sobrenome, int(idade), sexo, cpf, float(salario), cargo)

    def employee_info(self) -> str:
        """return a string with person's information

        Returns:
            [str]: [person information]
        """
        txt = self.info()
        txt += f"Cargo: {self.cargo} Salario: R${self.salario}"
        return txt

    def __str__(self) -> str:
        """return a string with person's information

        Returns:
            [str]: [person information]
        """
        return self.employee_info()


if __name__ == '__main__':
    p = Employee.from_string("jose,helmo,23,masculino,99999999999,3500,desenvolvedor")
    print(p)