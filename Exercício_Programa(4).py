import random
Fichas = 100
print ('Você tem 100 fichas')
quer_jogar = 'sim'
quer_jogar = input ('quer jogar? ' )
while Fichas > 0 and quer_jogar == 'sim':
    print ('Fase Come Out')
    aposta = input('Muito bem, escolha qual tipo de aposta vai querer fazer, podendo ser: Line Bet, Fields, Any Craps ou Twelve: ')


    if aposta == 'Line Bet' or aposta == 'line bet':
        valor_apostado = int(input('quanto gostaria de apostar?' ))
        r1 = random.randint (2,12)
        print ('A soma foi {0}'.format(r1))
        if r1 == 7 or r1 == 11:
            Fichas == Fichas + valor_apostado
        elif r1==2 or r1==3 or r1==12:
            Fichas = Fichas - valor_apostado
        else:
            print ('Fase Point')
            r2 = random.randint (2,12)
            print ('A soma foi {}'.format(r2))
            while r2 != r1 or r2 != 7:
                print ('jogar novamente os dados')
                r2 = random.randint (2,12)
                print ('A soma foi {}'.format(r2))               
            
                if r2==r1:
                    Fichas = Fichas + valor_apostado            
                elif r2==7:
                    Fichas = Fichas - valor_apostado
            


    if aposta == ' Fields' or aposta == 'fields':
        valor_apostado = int(input('quanto gostaria de apostar?' ))
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


    if aposta =='Any Craps' or aposta == 'any craps':
        valor_aposta = int(input('quanto gostaria de apostar?' ))
        r1 = random.randint (2,12)
        print ('A soma foi {0}'.format(r1))
        if r1 == 2 or r1==3 or r1==12:
            Fichas = Fichas + valor_apostado*7
        else:
            Fichas = Fichas - valor_aposta


    if aposta == 'Twelve' or aposta == 'twelve':
        valor_aposta = int(input('quanto gostaria de apostar?' ))       
        r1 = random.randint (2,12)
        print ('A soma foi {0}'.format(r1))
        if r1==12:
            Fichas = Fichas + valor_aposta*30
        else:
            Fichas = Fichas - valor_aposta
        
        
    print('Agora você tem:{0}'.format(Fichas))
    quer_jogar =input ('quer jogar novamente?')
    
if Fichas == 0 and quer_jogar =='sim':
    print ('que pena, não pode')
