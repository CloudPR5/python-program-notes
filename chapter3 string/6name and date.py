#write a program to fill ina letter template given below with name an date
letter = '''Dear <|Name|>,
 you are selected!
 <|Date|>'''
print(letter.replace("<|Name|>", "prince").replace("<|Date|>","21 Feb 2025"))