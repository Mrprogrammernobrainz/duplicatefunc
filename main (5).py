def duplicate(iterat, word):
    ans = ''
    if iterat == 0:
        return ''
    for i in range(len(word)):
        if word[i] != ' ' and word[i] != ',' and word[i] != '!' and word[i] != '?' and word[i] != '(' and word[i] != ')' and word[i] != ";" and word[i] != ":" and word[i] != '[' and word[i] != ']' and word[i] != '{' and word[i] != '}' and word[i] != '-':
            ans = ans + word[i] * iterat
        else:
            ans = ans + word[i]
    return ans
a = int(input())
b = input()
print(duplicate(a, b))