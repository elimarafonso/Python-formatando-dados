from datetime import datetime

class Datasbr:
    def __init__(self):
        self.momento = datetime.today()


    def mes_cadastro(self):
        ano = {
            '1':'Janeiro', '2':'Fevereiro', '3':'Março',  '4:':'Abril',
            '5': 'Maio',  '6': 'Junho', '7': 'Julho', '8': 'Agosto' , '9': 'Setembro' ,
            '10': 'Outubro', '11': 'Novembro',  '12': 'Dezembro'
        }
        return ano[str(self.momento.month)]

    def dia_semana_cadastro(self):
        semana = {
            '0':'Segunda-feira','1':'Terça-feira','2':'Quarta-feira',
            '3':'Quinta-feira','4': 'Sexta-feira','5':'Sábado',
            '6':'Domingo'
        }
        return semana[str(self.momento.weekday())]

    def dia_mes_cadastro(self):
        return self.momento.day

    def ano_cadastro(self):
        return self.momento.year