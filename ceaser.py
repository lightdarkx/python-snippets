def ceaser(str):
    for i in str:
        x = ord(i) + 4
        print(chr(x))
        str=str.replace(i, chr(x))
    print(str) 