#O código a seguir representa o Exercício Programa 1 feito por Gustavo Katz e Rafael Oncins, do 1° semestre de Engenharia da turma B 

import random
Fichas = 100
print ('Você tem 100 fichas')
quer_jogar = 'sim'
quer_jogar = input ('quer jogar? ' )
while Fichas > 0 and quer_jogar == 'sim':
    print ('Fase Come Out')
    aposta = input('Muito bem, escolha qual tipo de aposta vai querer fazer, podendo ser: Pass Line Bet, Fields, Any Craps ou Twelve: ')

    valor_apostado = int(input('quanto gostaria de apostar? '))
    if aposta == 'Pass Line Bet' or aposta == 'pass line bet' and valor_apostado <= Fichas:
        print ('Nessa aposta, caso a soma dos dados seja igual a 7 ou 11 você ganha o valor que foi apostado, caso a soma seja 2, 3 ou 12 você perde e caso a soma seja outro valor, esse valor passa a ser chamado de Point e você vai para a fase Point')
        r1 = random.randint (2,12)
        print ('A soma foi {0}'.format(r1))
        if r1 == 7 or r1 == 11:
            Fichas = Fichas + valor_apostado
        elif r1==2 or r1==3 or r1==12:
            Fichas = Fichas - valor_apostado
        else:
            print ('Fase Point')
            print ('Nessa fase, a soma dos dados lançados deve ser igual ao valor "Point" para você ganhar o mesmo valor que foi apostado, caso seja igual a 7 você perde e caso seja qualquer outro valor, os dados continuarão sendo lançados até haver um veredito')
            Point = True
            while Point and valor_apostado <= Fichas:
                r2 = random.randint (2,12)
                print ('A soma foi {}'.format(r2))                       
                if r2==r1:
                    Fichas = Fichas + valor_apostado
                    Point = False
                elif r2==7:
                    Fichas = Fichas - valor_apostado
                    Point = False
                else:
                    Point = True
                    print ('jogar novamente os dados')



    elif aposta == ' Fields' or aposta == 'fields' and valor_apostado <=Fichas:
        print ('Nessa aposta, caso a soma dos dados seja igual a 3, 4, 9, 10 ou 11 você ganha o mesmo valor que foi apostado, caso a soma seja 2 você ganha 2 vezes o valor apostado, caso a soma seja 12 você ganha 3 vezes o valor apostado e caso a soma seja outro valor você perde')
        r1 = random.randint (2,12)
        print ('A soma foi {0}'.format(r1))
        if r1==5 or r1==6 or r1==7 or r1==8:
            Fichas = Fichas - valor_apostado          
        elif r1==3 or r1==4 or r1==9 or r1==10 or r1==11:
            Fichas = valor_apostado + Fichas
        elif r1==2:
            Fichas = 2* valor_apostado + Fichas
        else:
            Fichas = 3* valor_apostado + Fichas


    elif aposta =='Any Craps' or aposta == 'any craps' and valor_apostado <=Fichas:
        print ('Nessa aposta, caso a soma dos dados seja igual a 2, 3 ou 12 você ganha 7 vezes o valor apostado, caso seja outro valor você perde')
        r1 = random.randint (2,12)
        print ('A soma foi {0}'.format(r1))
        if r1 == 2 or r1==3 or r1==12:
            Fichas = Fichas + valor_apostado*7
        else:
            Fichas = Fichas - valor_apostado


    elif aposta == 'Twelve' or aposta == 'twelve'and valor_apostado <=Fichas:
        print ('Nessa aposta, caso a soma dos dados seja igual a 12 você ganha 30 vezes o valor apostado, caso seja outro valor você perde')  
        r1 = random.randint (2,12)
        print ('A soma foi {0}'.format(r1))
        if r1==12:
            Fichas = Fichas + valor_apostado*30
        else:
            Fichas = Fichas - valor_apostado
        
    elif valor_apostado > Fichas:
        print('você nao pode apostar tanto')

    print('Agora você tem:{0}'.format(Fichas))
    quer_jogar =input ('quer jogar novamente?')
    
    

if Fichas == 0 and quer_jogar =='sim':
    print ('que pena, não pode')