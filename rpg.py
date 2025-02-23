import random


print("BEM VINDO AO RPG PYTHON")
print("NESSA PEQUENA DEMO, VOCÊ DEVE ENFRENTAR UMA SERPENTE ENCONTRADA EM")
print("UMA CAVERNA QUE ESTAVA EXPLORANDO")

print("==============================================================")
print("─────▄████▀█▄")
print("───▄█████████████████▄")
print("─▄█████.▼.▼.▼.▼.▼.▼▼▼▼")
print("▄███████▄.▲.▲▲▲▲▲▲▲▲")
print("████████████████████▀▀")
print("==============================================================")
print("HP:3500 =============================== AT:100")
print("==============================================================")
print("==============================================================")
print("HP 1200 ================================AT:100")
print("PARA MATAR A SERPENTE, VOCÊ TEM TRÊS OPÇÕES PARA LUTAR")
print("VOCÊ PODE ATACAR, DEFENDER OU ESQUIVAR, ATACAR É PROGRESSIVO")
print("A CADA TEMPO SEU ATAQUE AUMENTA EM 50, DEFENDER RETIRA METADE DO")
print("DANO INIMIGO, ESQUIVAR TEM 50% DE CHANCE DE DAR ERRADO")
print("PARA ATACAR DIGITE: atacar")
print("PARA DEFESA DIGITE: defender")
print("PARA ESQUIVAR DIGITE: esquivar")
print("==============================================================")
print("==============================================================")

HP1 = 3500
HP2 = 1000
A = 100
D = 50
E = [1,2]
1 == A
2 == D
3 == E

ação = int(input("QUAL SUA PRIMEIRA AÇÃO?"))




if ação == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 100 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1= HP1-A
    HP2=HP2-100
    A = 150
elif ação == 2:
    print("VOÇÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2= HP2-50
    A= 150
elif ação == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A=150
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2=HP2-100
        A=150
else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)


ação2 = int(input("O QUE FARÁ AGORA?"))
if ação2 == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 150 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1 =HP1-A
    HP2=HP2-100
    A = 200
elif ação2 == 2:
    print("VOÇÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2=HP2-50
    A = 200
elif ação2 == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A=200
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2=HP2-100
        A=200
else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)

ação3 = int(input("O QUE FARÁ AGORA?"))
if ação3 == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 200 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1 =HP1-A
    HP2=HP2-100
    A = 250
elif ação3 == 2:
    print("VOCÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2=HP2-50
    A=250
elif ação3 == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A=250
        
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2=HP2-100
        A=250
else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)

ação4 = int(input("O QUE FARÁ AGORA?"))
if ação4 == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 250 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1 = HP1-A
    HP2= HP2-100
    A = 300
elif ação4 == 2:
    print("VOÇÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2=HP2-50
    A=300
elif ação4 == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A=300
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2=HP2-100
        A=300
else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)

ação5 = int(input("O QUE FARÁ AGORA?"))
if ação5 == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 300 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1 = HP1-A
    HP2=HP2-100
    A = 350
elif ação5 == 2:
    print("VOÇÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2 = HP2-50
    A = 350
elif ação5 == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A = 350
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2= HP2-100
        A = 350
else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)

ação6 = int(input("O QUE FARÁ AGORA?"))
if ação6 == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 350 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1 = HP1-A
    HP2=HP2-100
    A = 400
elif ação6 == 2:
    print("VOÇÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2 = HP2-50
    A = 400
elif ação6 == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A = 400
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2= HP2-100
        A = 400
else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)

ação7 = int(input("O QUE FARÁ AGORA?"))
if ação7 == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 400 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1 = HP1-A
    HP2=HP2-100
    A = 450
elif ação7 == 2:
    print("VOÇÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2 = HP2-50
    A = 450
elif ação7 == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A = 450
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2= HP2-100
        A = 450
else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)

ação8 = int(input("O QUE FARÁ AGORA?"))
if ação8 == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 450 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1 = HP1-A
    HP2=HP2-100
    A = 500
elif ação8 == 2:
    print("VOÇÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2 = HP2-50
    A = 500
elif ação8 == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A = 500
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2= HP2-100
        A = 500
else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)

ação9 = int(input("O QUE FARÁ AGORA?"))
if ação9 == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 500 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1 = HP1-A
    HP2=HP2-100
    A = 550
elif ação9 == 2:
    print("VOÇÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2 = HP2-50
    A = 550
elif ação9 == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A = 550
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2= HP2-100
        A = 550
else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)

ação10 = int(input("O QUE FARÁ AGORA?"))
if ação10 == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 550 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1 = HP1-A
    HP2=HP2-100
    A = 600
    if HP2== 0:
        print("==============VOCÊ MORREU==============")
        print("==============GAME OVER================")
        exit(0)
elif ação10 == 2:
    print("VOÇÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2 = HP2-50
    A = 600
elif ação10 == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A = 600
    if HP2== 0:
        print("==============VOCÊ MORREU==============")
        print("==============GAME OVER================")
        exit(0)
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2= HP2-100
        A = 600
    if HP2== 0:
        print("==============VOCÊ MORREU==============")
        print("==============GAME OVER================")


else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)

ação11 = int(input("O QUE FARÁ AGORA?"))
if ação11 == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 600 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1 = HP1-A
    HP2=HP2-100
    A = 650
    if HP2== 0:
        print("==============VOCÊ MORREU==============")
        print("==============GAME OVER================")
        exit(0)
        
elif ação11 == 2:
    print("VOÇÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2 = HP2-50
    A = 650
elif ação11 == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A = 650
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2= HP2-100
        A = 650
else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)

ação12 = int(input("O QUE FARÁ AGORA?"))
if ação12 == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 650 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1 = HP1-A
    HP2=HP2-100
    A = 700
    if HP2== 0:
        print("==============VOCÊ MORREU==============")
        print("==============GAME OVER================")
        exit(0)
    elif HP1<=0:
        print("=============PARABÉNS!! VOCÊ GANHOU!!=============")
        exit(0)

elif ação12 == 2:
    print("VOÇÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2 = HP2-50
    A = 700
elif ação12 == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A = 700
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2= HP2-100
        A = 700
else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)

ação13 = int(input("O QUE FARÁ AGORA?"))
if ação13 == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 700 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1 = HP1-A
    HP2=HP2-100
    A = 750
    if HP2== 0:
         print("==============VOCÊ MORREU==============")
         print("==============GAME OVER================")
         exit(0)
    elif HP1<=0:
        print("=============PARABÉNS!! VOCÊ GANHOU!!=============")
        exit(0)
elif ação13 == 2:
    print("VOÇÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2 = HP2-50
    A = A+50
elif ação13 == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A = A=50
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2= HP2-100
        A = A+50
        if HP2== 0:
         print("==============VOCÊ MORREU==============")
         print("==============GAME OVER================")
         exit(0)
else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)

ação14 = int(input("O QUE FARÁ AGORA?"))
if ação14 == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 750 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1 = HP1-A
    HP2=HP2-100
    A = A+50
    if HP2<= 0:
         print("==============VOCÊ MORREU==============")
         print("==============GAME OVER================")
         exit(0)
    elif HP1<=0:
        print("=============PARABÉNS!! VOCÊ GANHOU!!=============")
        exit(0)
elif ação14 == 2:
    print("VOÇÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2 = HP2-50
    A = A=50
    if HP2<= 0:
         print("==============VOCÊ MORREU==============")
         print("==============GAME OVER================")
         exit(0)
elif ação14 == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A = A+50
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2= HP2-100
        A = A+50
        if HP2<= 0:
         print("==============VOCÊ MORREU==============")
         print("==============GAME OVER================")
         exit(0)
else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)

ação15 = int(input("O QUE FARÁ AGORA?"))
if ação15 == 1:
    print ("VOCÊ DECIDIU ATACAR!! A SERPENTE RECEBEU 800 DE DANO")
    print (f"AGORA TEM {HP1-A} DE HP")
    print("VOCÊ FOI ATACADO TAMBÉM, AGORA TE RESTA:{} HP".format(HP2-100))
    HP1 = HP1-A
    HP2=HP2-100
    A = A+50
    if HP2<= 0:
         print("==============VOCÊ MORREU==============")
         print("==============GAME OVER================")
         exit(0)
    elif HP1<=0:
        print("=============PARABÉNS!! VOCÊ GANHOU!!=============")
        exit(0)
elif ação15 == 2:
    print("VOCÊ DECIDIU DEFENDER!")   
    print("A SERPENTE TE DEU 50 DE DANO, RESTAM {} ".format(HP2-50))
    HP2 = HP2-50
    A = A+50
    if HP2<= 0:
         print("==============VOCÊ MORREU==============")
         print("==============GAME OVER================")
         exit(0)
    elif HP1<=0:
        print("=============PARABÉNS!! VOCÊ GANHOU!!=============")
        exit(0)
elif ação15 == 3:
    print("VOCÊ DECIDIU ESQUIVAR")
    E1 = random.choice(E)
    if E1 == 2:
        print("VOCÊ CONSEGUIU ESQUIVAR, NÃO RECEBEU DANO!!!")
        A = A+50
    else:
        print("VOCÊ ERROU A ESQUIVA, RECEBEU 100 DE DANO")
        print("RESTA {} DE HP".format(HP2-100))
        HP2= HP2-100
        A = A+50
        if HP2<= 0:
         print("==============VOCÊ MORREU==============")
         print("==============GAME OVER================")
         exit(0)
else:
    print("VOCÊ DIGITOU UM COMANDO ERRADO, REINICIE O JOGO")
    exit(0)