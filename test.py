str = 'abcd xyz'

for i in str:
    if (i.isalpha()) and (i < 'w'):
        print('low')
    else:
        print('high')
print(str)