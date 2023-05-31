from twilio.rest import Client
import pandas as pd


account_sid = "$TWILIO_SID"
auth_token  = "$TWILIO_AUTH_TOKEN"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril' , 'maio', 'junho' ]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'no mes de {mes} foi encontrado o {vendedor} com {vendas} em vendas')
        message = client.messages.create(
            to="+5561981783644",
            from_="+13203358552",
            body=f'No mês de {mes} foi encontrado o {vendedor} com {vendas} em vendas')
        print(message.body)












