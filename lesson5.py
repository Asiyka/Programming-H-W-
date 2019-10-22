alphabet="абвгґдеєжзиіїйклмнопрстуфхцчшщьюабвгґдеєжзиіїйклмнопрстуфхцчшщьюяя"
shifred=""
shifr=input("Введіть кодову фразу:")

for letter in shifr:
    position=alphabet.find(letter)
    newPos=position+1
    if letter in alphabet:
        shifred=shifred+alphabet[newPos]
    else:
        shifred=shifred+letter

print("Ваш шифр:",shifred)
