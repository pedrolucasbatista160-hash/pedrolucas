from datetime import datetime 
nome = input('digite seu nome:')
idade = int(input('digite sua idade:'))


ano_atual = datetime.now().year
ano_cem = ano_atual + (100 - idade)


print(f'olá,{nome}! você completara 100 anos no ano de {ano_cem}.')