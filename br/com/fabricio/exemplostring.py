import string

# exemplo de concatenação!
string_1 = 'Good'
string_2 = ' day'
string_3 = string_1 + string_2

print(string_3)
print('Hello ' + 'World')
# subset of characters
print(string_3[4:7]*10)


string_4 = "Batatinha quando nasce espalha a rama pelo chão"
string_5 = 'Nome:Fabricio'
print(string_4)
print(string_4.split('a'))
print(string_5.split(':')[1])
print(string_4.count('a'))
print(string_4.replace('chão', 'solo'))

print('Fabricio' == 'Fabricio') # True or False

format_ex = '{}, seja bem vindo ao maravilhoso mundo do Python {}!!'
print(format_ex)
print(format_ex.format('Larissa', 3.0))

print('|{:>50}|'.format('Alinhado à direita'))
print('|{:<50}|'.format('Alinhado à esquerda'))
print('|{:^50}|'.format('Alinhado ao centro'))

template_ex = string.Template('$artist sang $song in $year')
print(template_ex.substitute(artist='Freddie Mercury', song='The great pretender',
                             year=1987))

idade = True
print(type(idade))

# +, -, *, /
# // - divisão de inteiros 10.5 // 2
# % - Módulo 5%3
# ** exponenciação

