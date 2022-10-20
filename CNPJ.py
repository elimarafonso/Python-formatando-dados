from validate_docbr import CNPJ
class Cnpj:
     def __init__(self):
         cnpj = CNPJ()
         self._numero = cnpj.generate(True)
         print(f'CNPJ: {self._numero}')
