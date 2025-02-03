size = int((input("QUANTI NUMERI VUOI CONVERTIRE?: ")))
codifica =[]
Numeri = []
indice = 0
N = 0
C = ''
k = 0
for i in range(size):
    C = input("Inserire la codifica del numero : (d/D per \"DECIMALE\" o b/B  per \"BINARIO\"): ") #chiedo all'utente se il numero è decimale o binario
    while C not in ["d", "D", "b", "B"]: #controllo se il carattere inserito è corretto
        print( "ERRORE, IL FORMATO SELEZIONATO NON è ANCORA SUPPORTATO/NON ESISTE, SI PREGA DI RIPROVARE.")
        C = input("Inserire la codifica del numero : (d/D per \"DECIMALE\" o b/B  per \"BINARIO\"): ")# se il carattere inserito non è corretto chiedo all'utente di reinserirlo
    N = int(input("Inserire il numero nel formato selezionato: ")) #chiedo all'utente di inserire il numero
    if C == "d" or C == "D":
        if N < 0 : #controllo se il numero inserito è negativo nel caso in cui il numero sia decimale
            while N < 0:
                print("Il numero inserito è negativo, si prega di inserire un numero positivo")
                N = int(input("Inserire il numero nel formato selezionato: "))
    elif C =="b" or C=="B":
        N = str(N)
        if not all(c in '01' for c in N): #controllo se il numero inserito è composto solo da zero e uno se è stata selezionata la codifica binaria
            while not all(c in '01' for c in N):    #chiedo all'utente di reinserire il numero se non è binario
                print("Il numero inserito non è binario")
                N = int(input("Inserire il numero nel formato selezionato: "))
                N = str(N)
    N = int(N)
    if C == "d" or C == "D":
        codifica.append("DECIMALE") #aggiungo alla lista codifica la stringa "DECIMALE" se il numero è decimale
    elif C == "b" or C == "B":
        codifica.append("BINARIO")
    Numeri.append(N) #aggiungo alla lista Numeri il numero inserito dall'utente

print("Codifica: ",codifica)
print("Numeri: ",Numeri)

Numero_Complementare = []
Codifica_complementare =[]

for i in range(size):
    if codifica[i] == "DECIMALE":
        Codifica_complementare.append("BINARIO")
        print("il numero "+str(Numeri[i])+" è un numero decimale")
        X = Numeri[i]
        binario = ""
        while X > 0:
            binario =str(X%2)+ binario 
            X = X//2
        print("il numero binario è: ",binario)
        Numero_Complementare.append(int(binario))
    elif codifica[i] == "BINARIO":
        Codifica_complementare.append("DECIMALE")
        print("il numero "+str(Numeri[i])+" è un numero binario")
        X = str(Numeri[i])
        decimale = 0
        for j in range(len(X)):
            indice = len(X)-j-1
            decimale = decimale +int(X[j])*pow(2,indice)
        else:
            print("il numero decimale è: ",decimale)
        Numero_Complementare.append(decimale)
print("Codifica Originale: ",codifica)
print("Codifica complementare: ",Codifica_complementare)
print("Numero Originale: ",Numeri)
print("Numero complementare: ",Numero_Complementare)