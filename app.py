import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome} se o serviço for apenas banho o valor é R$ XX,XX. Se o serviço for de banho mais a tosa o valor é de R$ xxx,xx.{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome} nosso horário de funcionamento é de segunda a sexta, das 8 hrs até as 18hrs com pausa para o almoço as 11 hs e retornamos as 14hs{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome} estamos localizados na Rua Olivia Palito numero 1352, centro, na Cidade de Algum Lugar{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome} podera nos contactar pelo whatsapp (xx) xxxxx-xxxx{os.linesep}')
    elif resposta == '5':
        print(f'{nome} Espero ter ajudado você.')
        quit()
    else:
        print('Resposta invalida! Por favor digite apenas 1, 2, 3 ou 4.')


def start():
    print("Olá! Be-vindo a Hidropet's")
    nome = input('Digite seu nome: ')
    telefone = input('Digite seu telefone: ')
    while True:
        resposta = input(f'O que gostaria de saber?{os.linesep}[1] - Qual o valor do banho e da tosa?{os.linesep}[2] - Quais os horarios de funcionamento?{os.linesep}[3] - Qual o endereço?{os.linesep}[4] - Como entro em contato?{os.linesep}[5] - Sair{os.linesep}')
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()