def wordBreak(dict, str, out=""):
    if not str:
        print(out)
        return
    for i in range(1, len(str) + 1):
        prefix = str[:i]
        if prefix in dict:
            wordBreak(dict, str[i:], out + " " + prefix)
dict = ["self", "th", "is", "famous", "Word","break", "b", "r", "e", "a", "k", "br", 'eak',"bre", "brea", "ak", "problem"]
str = "Wordbreakproblem"
wordBreak(dict, str)