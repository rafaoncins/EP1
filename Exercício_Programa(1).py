import random
Fichas = 100
print ('Você tem 100 fichas')

while Fichas >= 0:
    if Fichas == 0:
        print ('Você está fora')
    else:
        quer_jogar = input('quer jogar?(sim/não) ')                
        if quer_jogar == 'não':
             print ('Você está fora')
        elif quer_jogar == 'sim':
            print ('Fase Come Out')
            qual_aposta = input('Escolha uma aposta: Pass Line Bet, Fields, Any Craps ou Twelve ')

            if qual_aposta == 'Fields':
                def fields (aposta_f):
                    while aposta_f<=Fichas:
                        aposta_f=int(input('faça sua aposta: '))
                        r1 = random.randint (2,12)
                        if r1==5 or r1==6 or r1==7 or r1==8:
                            return 0+Fichas
                        elif r1==3 or r1==4 or r1==9 or r1==10 or r1==11:
                            return aposta_f+Fichas
                        elif r1==2:
                            return 3*aposta_f+Fichas
                        else:
                            return 4*aposta_f+Fichas

            elif qual_aposta == 'Any Craps':
                def any_craps (aposta_a):
                    while aposta_a<=Fichas:
                        aposta_a=int(input('faça sua aposta: '))
                        r2 = random.randint (2,12)
                        if r2==2 or r2==3 or r2==12:
                            return aposta_a*8+Fichas
                        else: 
                            return 0+Fichas

            elif qual_aposta == 'Twelve':
                def twelve (aposta_t):
                    while aposta_t<=Fichas:  
                        aposta_t=int(input('faça sua aposta: '))
                        r3 = random.randint (2,12)
                        if r3==12:
                            return aposta_t*31+Fichas
                        else:
                            return 0+Fichas
                    
                    



