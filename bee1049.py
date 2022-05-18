"""
1049 -Animal
Neste problema, você deverá ler 3 palavras que definem o tipo de 
animal possível segundo o esquema abaixo, da esquerda para a direita.  
Em seguida conclua qual dos animais seguintes foi escolhido, 
através das três palavras fornecidas.

"""


x = input()
y = input()
z = input()

if x == 'vertebrado' and y == 'ave' and z == 'carnivoro':
    animal = 'aguia'
if x == 'vertebrado' and y == 'ave' and z == 'onivoro':
    animal = 'pomba'

if x == 'vertebrado' and y == 'mamifero' and z == 'onivoro':
    animal = 'homem'

if x == 'vertebrado' and y == 'mamifero' and z == 'herbivoro':
    animal = 'vaca'

if x == 'invertebrado' and y == 'inseto' and z == 'hematofago':
    animal = 'pulga'

if x == 'invertebrado' and y == 'inseto' and z == 'herbivoro':
    animal = 'lagarta'

if x == 'invertebrado' and y == 'anelideo' and z == 'hematofago':
    animal = 'sanguessuga'

if x == 'invertebrado' and y == 'anelideo' and z == 'onivoro':
    animal = 'minhoca'


print(animal)