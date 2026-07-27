letter =    '''Dear <|Name|>,
You are Selected !
<|Date|>'''

name = str(input("Enter your name: "))
date = str(input("Enter the date: "))
# print(letter.replace("<|Name|>", "Hitesh").replace("<|Date|>", "21/11/2005"))
print(letter.replace("<|Name|>", name).replace("<|Date|>", str(date)))