
w = [2, 7, 11, 21, 42, 89, 180, 354]
n = 588
m = 881


def encryptMerkleHellman():
    b = []
    word = (input("Écrire un mot :  "))
    for i in range(len(w)):
        temp = (w[i] * n) % m #création de la clé publique
        b.append(temp)
        
    print("Publique clé : ", b)
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


if __name__ == '__main__':
    list_crypt = []

    encryptMerkleHellman()


    
 