#!/usr/bin/env python3
import sys

fav_dict = {'livro':'cronicas de gelo e fogo','som':'AC/DC','arvore':'cedro','organismo':'planta'}

print('6)Obtenha um valor da linha de comando para fav_thing e print o valor desse item do dicionário:')
print(fav_dict.keys())
print('Qual informação deseja obter?')
fav_thing = input()
print(fav_dict[fav_thing])
print('')

print('7)Altere o valor do seu organismo favorito:')
fav_dict.update({'organismo':'virus'})
print('')

print('8)Obtenha fav_thing da linha de comando e um novo valor para essa chave. Altere o valor com o valor inserido pelo usuário:')
print('Qual seu assunto favorito?')
fav_thing = input()
print('especifique:')
coisa = input()
fav_dict.update({fav_thing:coisa})
print('')
print(f'dados atualizados:\n{fav_dict}')
print('')

print('9)Use um loop for para imprimir cada chave e valor do dicionário:')
for item in fav_dict:
    print(f'{item} = {fav_dict[item]}')

