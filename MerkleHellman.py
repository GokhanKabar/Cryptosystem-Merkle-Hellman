
w = [2, 7, 11, 21, 42, 89, 180, 354]
n = 588
m = 881

def encryptMerkleHellman():
    b = []
    word = (input("Écrire un mot :  "))
    for i in range(len(w)):
        temp = (w[i] * n) % m #création de la clé publique
        b.append(temp)
        
    print("Clé public : ", b)
    asci = [ord(a) for a in word]
    liste = []

    for i in asci:
        s = bin(i).replace("0b", "0") #on met le message en binaire
        liste.append(s)
  
    for i in liste:
        temp = 0
        cnt = 0
        for j in str(i):
            temp += (int(j) * b[cnt])#on calcule le message chiffré
            cnt += 1
        list_crypt.append(temp)

    print("Message chiffré ", list_crypt)



def decryptMerkleHellman():
    d = 1
    while True:
        x = (n * d) % m #Calcule de l'inverse modulaire
        if x == 1:
            break
        d += 1
    inverse = d
    
    bin_l = []
    for i in list_crypt:
        p = (i * inverse) % m #Bob calcule P
        
        bin = 0 
        inverseW = sorted(w, reverse=True) #Algorithme de glouton
        sum = 0
        for i in range(len(w)): 
            sum += w[i - 1]
        for g, j in enumerate(inverseW):
            if j <= p:
                p = p - j
                binaire = pow(10, g)
                bin += binaire
            else:
                continue
        bin_l.append(bin)
        
    print("Le message en binaire :", bin_l)


if __name__ == '__main__':
    list_crypt = []

    encryptMerkleHellman()

    decryptMerkleHellman()
    
 