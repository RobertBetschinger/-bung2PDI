from itertools import chain #Only for A Nice Print of the Result
# TextEinlesen
f = open("encrypted06", "rt")
lines = f.readline()
myAdvaziList = []
myAdvaziList = lines.split()
f.close()

# ReadSecretKey
mySecretKeyCrypted = []
mySecretKeyCrypted = myAdvaziList[-10:]



# CalculateBufferSize
# If the Key doesnt match the CipherText we reached the end of the Padding
theNumberofPaddingBytes = 0
for x in range(99, 1, -1):
    if (myAdvaziList[x] != mySecretKeyCrypted[x % 10]):
        theNumberofPaddingBytes = 100 - (x + 1)
        break
print("The Number of Padding Bytes is:")
print(theNumberofPaddingBytes)

# Caluculate the right Key
# xor falsekey with paddingByte to receive the Correct Key.
print("This is The Secret Key, but Cryped, as Hex")
print(mySecretKeyCrypted)
myCorrectKey = []
for x in range(0,10):
    currentFalseKeyInteger = int(mySecretKeyCrypted[x], 16)
    rightKeyValue = currentFalseKeyInteger^theNumberofPaddingBytes
    myCorrectKey.append(rightKeyValue)
#This little *** line above costet me an hour, i compared the int List My correct Key with the right Hex Values for the Key,
# which i calculated manually and thougt the would be wrong

print("This is the Correct Key as Ints.")
print(myCorrectKey)

# XorAddieren mit gegebener Schlüssellänge
myXOrList = []
for x in range(0, 99):
   current_integer = int(myAdvaziList[x], 16)
   current_secret_key_integer = myCorrectKey[x % 10]
   currentXORedValue = current_integer ^ current_secret_key_integer
   myXOrList.append(currentXORedValue)

#Remove Padding Bytes
#I used integer List in the first time, because its easier to handline than Hex List in my Opinion
noPaddingList = [i for i in myXOrList if i != theNumberofPaddingBytes] #DudeComeON

#Klartext Ausgeben
mydecryptedList = []
for x in noPaddingList:
    hex_string = hex(x)[2:]
    bytes_object = bytes.fromhex(hex_string)
    ascii_string = bytes_object.decode("ASCII")
    mydecryptedList.append(ascii_string)
print("The Result List:")
print(mydecryptedList)

print("\nNice To Read")
print (" ".join(chain.from_iterable(mydecryptedList)))


