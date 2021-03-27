def find_duplicates(s):
    elements = {}
    for char in s:
        if elements.get(char,None) != None:
            elements[char]+=1
        else:
            elements[char] = 1
    return [k for k,v in elements.items() if v>1]
print(find_duplicates("Hello World Is Myth"))