import  re

#máscara do número
#+xxx(xx)xxxxx-xxxx

class Telefone:

    def __init__(self, numero):
        self.telefone = numero

    def __str__(self):
        return self.format_telefone(self.telefone)

    def format_telefone(self, numero):
        padrao = "([0-9]{2})?" \
                 "([0-9]{2})" \
                 "([9]{1})?" \
                 "([0-9]{4,5})" \
                 "([0-9]{4})"
        resposta = re.search(padrao,numero)
        return '+{}({}){}{}-{}'.format(resposta.group(1),resposta.group(2),resposta.group(3),resposta.group(4),resposta.group(5))


###############################
#Usando a classe TELEFONE

numero = '5533998029799'
telefone = Telefone(numero)
print(telefone)


#saída:
#55(33)99802-9799