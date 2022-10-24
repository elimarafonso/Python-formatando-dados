from Datas_br import Datasbr
#from datetime import datetime, timedelta


cadastro = Datasbr()
print(f'Data do Python: {cadastro.momento}')
print(f'Mes cadastro: {cadastro.mes_cadastro()}')
print(f'Dia do mês: {cadastro.dia_mes_cadastro()}')
print(f'Dia da Semana: {cadastro.dia_semana_cadastro()}')

print('O cadastro foi feito em uma < {} > dia {} de {} de {}'.format(
        cadastro.dia_semana_cadastro(),cadastro.dia_mes_cadastro(),cadastro.mes_cadastro(),cadastro.ano_cadastro()))