#!/usr/bin/env python3
print('11)Escreva um script para encontrar a interseção, diferença, união e diferença simétrica entre esses dois conjuntos.')
print('')
Set_A = {'3', '14', '15', '9', '26', '5', '35', '9'}
Set_B = {'60', '22', '14', '0', '9'}
dif_AB = Set_A - Set_B
uni_AB = Set_A|Set_B
inter_AB = Set_A & Set_B
dif_sim_AB = Set_A ^ Set_B
print(f'Set A: {Set_A}')
print(f'Set B: {Set_B}')
print('')
print(f'dferença = {dif_AB}\nUnião = {uni_AB}\nInterseção = {inter_AB}\nDiferença simétrica ={dif_sim_AB}')

