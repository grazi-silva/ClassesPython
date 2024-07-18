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


class Teste:
    def executar(self):
        pessoa = Pessoa("Maria", 30)
        pessoa.set_cpf("123.456.789-00")
        print(pessoa)

        pessoa.set_idade(31)
        print(f"CPF de {pessoa.nome}: {pessoa.get_cpf()}")

        funcionario = Funcionario("João", 40, 5000)
        funcionario.set_cpf("987.654.321-00")
        print(funcionario)

        funcionario.aumentar_salario(10)
        print(f"Após aumento salarial: {funcionario}")


teste = Teste()
teste.executar()
