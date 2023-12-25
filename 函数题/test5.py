def acronym(phrase):
    StrList = phrase.split()
    str = ""
    for i in StrList:
        str += i[0].upper()
    return str