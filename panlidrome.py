def palindrom(w):
    for i in range(int(len(w)/2)):
        if w[i] != w[-i-1]:
            return False
    return True

for w in str(raw_input('Enter the string : ')).split():
    if not palindrom(w) : print w,
