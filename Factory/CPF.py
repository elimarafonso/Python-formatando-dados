from validate_docbr import CPF
class Cpf:

    def __init__(self):
        cpf = CPF()
        numero = cpf.generate(mask=False)

        if self.valida_cpf(numero):
            self._numero = cpf.mask(numero)
            print(f'CPF: {self._numero}')
        else:
            raise ValueError('CPF INVÁLIDO!')

######
######
    def __str__(self):
        return self.format_cpf()
######
######
    def valida_cpf(self, numero):
        if len(numero) == 11:
            cpf = CPF()
            return cpf.validate(numero)
        else:
            raise ValueError(f'CPF: {numero} não possui 11 digitos')
######
######
    def format_cpf(self):
        cpf = CPF()
        return cpf.mask(self._numero)


