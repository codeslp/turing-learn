def ubbi_dubbi(word):
    output = []
    for char in word:
        if char in ['a','e','i','o','u']:
            output.append('ub'+char)
        else:
            output.append(char)
    print(''.join(map(str, output)))

print(ubbi_dubbi('callie is my wife'))