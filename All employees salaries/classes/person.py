"""
1. Implemente uma classe para representar uma Pessoa.
Como atributos, nome, sobrenome, idade, sexo, CPF.
"""

class Pessoa():
    """
    A class to represent a normal person
    """

    def __init__(self, nome: str, sobrenome: str, idade: int, sexo: str, cpf: str):
        """
        Initialization of the "Pessoa" class 

        Args:
            nome (str): [name]
            sobrenome (str): [surname]
            idade (int): [age]
            sexo (str): [sex]
            cpf (str): [cpf]
        """
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf


    @classmethod
    def from_string(cls, string: str):
        """create class from string

        Args:
            string (str): string with person information

        Returns:
            [class]: person class
        """
        nome, sobrenome, idade, sexo, cpf = string.split(",")
        return cls(nome, sobrenome, idade, sexo, cpf)


    def info(self) -> str:
        """return a string with person's information

        Returns:
            [str]: [person information]
        """
        txt = f"nome: {self.nome} {self.sobrenome}\n"
        txt += f"idade: {self.idade}   sexo: {self.sexo}   CPF: {self.cpf}\n"
        return txt

    
    def __str__(self) -> str:
        """return a string with person's information

        Returns:
            [str]: [person information]
        """
        return self.info()

    
if __name__ == '__main__':
    p = Pessoa.from_string("jose,helmo,23,masculino,99999999999")
    print(p)