print('=======================================================')
print('Digite "S" para Sim e "N" para não!')
print('=======================================================')
resp=input("É mamifero?")

if resp=='S' or resp=='s':
    resp = input("É Quadrupede?")
    if resp=='S' or resp=='s':
        resp = input("É Carnivoro?")
        if resp == 'S' or resp == 's':
            print('É um leão')
        elif resp =='N' or resp =='n':
            resp = input("É Herbivoro?")
            if resp=='S' or resp=='s':
                print('É um cavalo')
    elif resp =='N' or resp =='n':
        resp = input("É Bípede?")
        if resp=='S' or resp=='s':
            resp = input("É onivero?")
            if resp == 'S' or resp == 's':
                print('Homem')
            elif resp =='N' or resp =='n':
                resp = input("É Frutífero?")
                if resp=='S' or resp=='s':
                    print('Macaco')
elif resp =='N' or resp =='n':
    resp = input("É ave?")
    if resp == 'S' or resp == 's':
        resp = input("É Não-voador?")
        if resp == 'S' or resp == 's':
            resp = input("É tropical?")
            if resp == 'S' or resp == 's':
                print('Avestruz')
            elif resp =='N' or resp =='n':
                resp = input("É Polar?")
                if resp == 'S' or resp == 's':
                    print('pinguin')
        elif resp =='N' or resp =='n':
            resp = input("É Nadador?")
            if resp == 'S' or resp == 's':
                print('Pato')
            elif resp =='N' or resp =='n':
                resp = input("É de rapina?")
                if resp == 'S' or resp == 's':
                    print('Águia')
    elif resp =='N' or resp =='n':
        resp = input("É Répitel?")
        if resp == 'S' or resp == 's':
            resp = input("É com casco?")
            if resp == 'S' or resp == 's':
                print('Tartaruga')
            elif resp =='N' or resp =='n':
                resp = input("É carnívoro?")
                if resp == 'S' or resp == 's':
                    print('Crocodilo')
                elif resp =='N' or resp =='n':
                    resp = input("É sem patas?")
                    if resp == 'S' or resp == 's':
                        print('Cobra')
