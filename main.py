class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade
        self.__cpf = None

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        if idade > 0:
            self._idade = idade
        else:
            raise ValueError("Idade deve ser positiva")

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self._idade}, CPF: {self.__cpf or 'Não definido'}"


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)

    def __str__(self):
        return f"{super().__str__()}, Salário: {self.salario}"
