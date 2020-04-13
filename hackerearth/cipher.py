text = input()
cipherkey = int(input())

LOWERCASE_ALPHA = [97, 122]
UPPERCASE_ALPHA = [65, 90]
NUMERIC = [48, 57]


def shiftCipher(inputText: int, typeOfText: list, ShiftBy: int):
    # print(inputText)
    for position in range(0,ShiftBy):
        inputText = inputText + 1
        if inputText > typeOfText[1]:
            # print("resetting")
            inputText = typeOfText[0]
        # print(inputText)
    return chr(inputText)

# print(shiftCipher(ord('a'),UPPERCASE_ALPHA,26))

ans = ""
for i in range(0, len(text)):
    # print(i)
    ascii_value = ord(text[i])
    if NUMERIC[0] <= ascii_value <= NUMERIC[1]:
        ans = ans + shiftCipher(ascii_value, NUMERIC, cipherkey)
    elif UPPERCASE_ALPHA[0] <= ascii_value <= UPPERCASE_ALPHA[1]:
        ans = ans + shiftCipher(ascii_value, UPPERCASE_ALPHA, cipherkey)
    elif LOWERCASE_ALPHA[0] <= ascii_value <= LOWERCASE_ALPHA[1]:
        ans = ans + shiftCipher(ascii_value, LOWERCASE_ALPHA, cipherkey)
    else:
        ans = ans + text[i]

print(ans)

'''
All-convoYs-9-be:Alert1.
Epp-gsrzs]w-=-fi:Epivx5.
Epp-gsrzsCw-3-fi:Epivx5.
'''
