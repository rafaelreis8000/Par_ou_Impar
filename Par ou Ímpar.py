from os import system
from time import sleep
from random import randint

jogo = bool(True)
tentativas = int(0)

while jogo == True:

    checagem = bool(False) #utilizada para fazer o usuário inserir um valor válido

    while checagem == False:

        system('cls')
        tentativas += 1

        escolhaUser = str(
            input(
                'Vamos jogar! Escolha par ou ímpar: '
                '\n[ P ] PAR'
                '\n[ I ] ÍMPAR'
                '\n[ S ] SAIR'
                '\n ---> '
            )
        ).strip().upper()

        if escolhaUser == 'P':
            isEven = True
            decisao = 'PAR'
            sleep(1)
            checagem = True

        elif escolhaUser == 'I':
            decisao = 'ÍMPAR'
            isEven = False
            sleep(1)
            checagem = True

        elif escolhaUser == 'S':

            while True:
                system('cls')
                sair = str(
                    input(
                        'Deseja realmente sair???'
                        '\n[ S ] SIM'
                        '\n[ N ] NÃO'
                        '\n --> '
                    )
                ).strip().upper()

                if sair == 'S':
                    sleep(0.5)
                    print('Saindo...')
                    sleep(1)
                    system('cls')
                    exit()

                elif sair == 'N':
                    jogo = True
                    break

                else:
                    print('Insira um input válido e tente novamente')
                    sleep(2)
                    system('cls')

        else:
            print('\nPor favor, insira um valor válido!')
            sleep(1)
            system('cls')
            checagem = False

    lance = bool(False)

    while lance == False:

        system('cls')

        user = int(
            input(
                '\nVocê escolheu {}'
                '\nAgora escolha um número entre 1 e 10: '
                .format(decisao)
            )
        )

        if user <= 0 or user > 10:
            print('\nPor favor, insira um valor válido!')
            sleep(1)
            system('cls')
            lance = False

        else:
            sleep(1)
            print('\nVocê escolheu {}!'.format(user))
            lance = True

        computer = randint(1 , 10)
        sleep(1)
        print('E eu escolhi {}!'.format(computer))
        sleep(1)
        print('\npar')
        sleep(0.5)
        print('ou')
        sleep(0.5)
        print('ímpar!')
        sleep(1)
        total = computer + user
        system('cls')

        if total % 2 == 0 and decisao == 'PAR':
            print(
                '\nVocê escolheu PAR, e {} + {} realmente é PAR!!! Você venceu!!!'
                .format(user, computer)
            )

            if tentativas == 1:
                print('Você ganhou de mim de primeira!!!')
                jogo = False

            else:
                print('{} tentativas foram necessárias para me vencer!'.format(tentativas))
                jogo = False

        elif total % 2 == 1 and decisao == 'ÍMPAR':
            print(
                '\nVocê escolheu ÍMPAR, e {} + {} realmente é ÍMPAR!!! Você venceu!!!'
                .format(user, computer)
            )

            if tentativas == 1:
                print('Ganhou de mim de primeira!!!')
                jogo = False

            else:
                print('{} tentativas foram necessárias para me vencer!'.format(tentativas))
                jogo = False

        else:
            print(
                '\nVocê escolheu {}, mas {} + {} não é {}!!!'
                '\nJogue outra vez e tente me vencer!'
                .format(decisao, user, computer, decisao)
            )
            sleep(3)
            jogo = True

print('\n\nFIM!')
#Jogue par ou ímpar com o computador. O jogo só acaba quando a máquina perder! O total de tentativas deve ser mostrado