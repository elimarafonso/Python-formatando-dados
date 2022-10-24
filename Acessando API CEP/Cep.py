import requests

class Cep:

    def __init__(self, cep):
        cep = str(cep)
        if self.validaCep(cep):
            self.cep = cep
        else:
            raise ValueError (f'O CEP <{cep}> é inválido')

    def __str__(self):
        return self.formataCep()

    def validaCep(self,cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formataCep(self):
        #39680-000
        return '{}-{}'.format(self.cep[:5],self.cep[5:])

    def buscaCep(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        endereco = requests.get(url).json()
        return  f'Rua: {endereco["logradouro"]}\n' \
                f'Complemento: {endereco["complemento"] }\n' \
                f'Bairro: {endereco["bairro"]} \n' \
                f'Cidade: {endereco["localidade"]} \n' \
                f'UF: {endereco["uf"]}\n'