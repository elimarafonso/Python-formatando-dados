from validate_docbr import CPF, CNPJ

#FACTORY
class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return Doc_CPF(documento)
        if len(documento) == 14:
            return Doc_CNPJ(documento)
        else:
            raise ValueError(f'Quantidade de dígitos inválida: (CPF = 11 / CNPJ = 14)')


class Doc_CPF:
    def __init__(self, documento):
        if self.valida_CPF(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF INVÁLIDO')

    def __str__(self):
        return f'CPF formatado: < {self.formata_CPF()} >'

    def formata_CPF(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def valida_CPF(self, documento):
        validador = CPF()
        return validador.validate(documento)


class Doc_CNPJ:
    def __init__(self, documento):
        if self.valida_CNPJ(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ INVÁLIDO!')

    def __str__(self):
        return f'CNPJ formatado: < {self.formata_CNPJ(self.cnpj)} >'

    def formata_CNPJ(self, documento):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def valida_CNPJ(self, documento):
        validador = CNPJ()
        return validador.validate(documento)







