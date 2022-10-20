from Factory_CPF_CNPJ import Documento as doc
from validate_docbr import CPF, CNPJ



#cria cpf aleatório
cpf_aleatorio = CPF()
cnpj_aleatorio = CNPJ()
numero_do_cpf = cpf_aleatorio.generate()
numero_do_cnpj = cnpj_aleatorio.generate()
print(f'CPF CRIADO: {cpf_aleatorio.mask(numero_do_cpf)}')
print(f'CNPJ CRIADO: {cnpj_aleatorio.mask(numero_do_cnpj)}')

#chama instancia da classe FACTORY
cpf = doc.cria_documento(numero_do_cpf)
cnpj =doc.cria_documento(numero_do_cnpj)
print('#######################')

print(f'{cpf}')
print(f'{cnpj}')


