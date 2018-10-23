dic = {"hello": "hola", "good": "bien", "how are you": "como esta"}
x = input('Enter your input: ').lower()

if x in dic.keys():
    print(dic[x])
else:
    print('Match not found')