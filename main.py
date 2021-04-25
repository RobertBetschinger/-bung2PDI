from itertools import chain #Only for A Nice Print of the Result
#TextEinlesen
f = open("encrypted03", "rt")
lines = f.readline()
myBinaryList =[]

myBinaryList = lines.split()
f.close()
#Letzte 10 Zeichen nehmen
#Länge der Blöcke ist gegeben aus Aufgabenstellung-->Somit auch Länge der Schlüsseltexte gegeben

mySecretKey =[]
mySecretKey = myBinaryList[-10:] #Cooler Slicer von StackOverflow
print(mySecretKey)


#XorAddieren mit gegebener Schlüssellänge
myXOrList=[]
for x in range(0,100):
    current_integer = int(myBinaryList[x], 16)
    print(current_integer)
    current_secret_key_integer = int(mySecretKey[x%10],16)
    print(current_secret_key_integer)
    currentXORedValue= current_integer^current_secret_key_integer
    myXOrList.append(currentXORedValue)

#0x0 können gelöscht werden sind nur Füllbytes
noPaddingList = [i for i in myXOrList if i != 0] #DudeComeON
print(type(noPaddingList[0]))
#Klartext Ausgeben
mydecryptedList =[]
for x in noPaddingList:
    hex_string = hex(x)[2:]
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode("ASCII")
    mydecryptedList.append(ascii_string)
print("The Result List:")
print(mydecryptedList)

print("\nNice To Read:")
print (" ".join(chain.from_iterable(mydecryptedList)))