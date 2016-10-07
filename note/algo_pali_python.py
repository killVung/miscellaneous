def isPali(string):
    for i in range(len(string)):
        if string[i] != string[len(string)-i-1]:
            return False
    return True

def isPali_all(string):
    return all(string[i] == string[len(string)-i-1] for i in range(len(string)//2))
print(isPali_all(input()))
