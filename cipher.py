x = raw_input()
y = int(raw_input())
encrypted = []

for i in range(0, len(x)):
    if ord(x[i]) in range(97, 122):
        ascii = ord(x[i])
        test = ascii + y
        quo = test/122
        if test > 122:
            if quo > 1:
                for j in range(0, quo):
                    test = test - 122
                salt = test - 122
                letter = 96 + int(salt)
                encrypted.append(chr(letter))
            else:
                salt = test - 122
                letter = 96 + int(salt)
                encrypted.append(chr(letter))
        else:
            encrypted.append(chr(test))
    elif ord(x[i]) in range(65, 90):
        ascii = ord(x[i])
        test = ascii + y
        quo = test / 90
        if test > 90:
            if quo > 1:
                for j in range(0, quo):
                    test = test - 90
                salt = test - 90
                letter = 64 + int(salt)
                encrypted.append(chr(letter))
            else:
                salt = test - 90
                letter = 64 + int(salt)
                encrypted.append(chr(letter))
        else:
            encrypted.append(chr(test))
    elif ord(x[i]) in range(48, 58):
        ascii = ord(x[i])
        test = ascii + y
        if test > 57:
            salt = test - 57
            letter = 47 + int(salt)
            encrypted.append(chr(letter))
        else:
            encrypted.append(chr(test))
    else:
        encrypted.append(x[i])

final = ""
print final.join(encrypted)
