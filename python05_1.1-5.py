#!/usr/bin/env python3
import sys

print('1)Escreva um script no qual você construa um dicionário de suas coisas favoritas:')
fav_dict = {'livro':'cronicas de gelo e fogo','som':'AC/DC','arvore':'cedro'}
print('')

print('2)Print o seu livro favorito:')
print(fav_dict['livro'])
print('')

print('3)Print o seu livro favorito, mas use uma variável na chave:')
fav_thing = 'livro'
print(fav_dict[fav_thing])
print('')

print('4)Agora print a sua árvore favorita:')
print(fav_dict['arvore'])
print('')

print('5)Adicione o seu "organismo" favorito ao dicionário. Faça com que "organismo" seja o novo valor da chave fav_thing:')
fav_dict.update({'organismo':'planta'})
fav_thing = 'organismo'
print(fav_dict[fav_thing])

