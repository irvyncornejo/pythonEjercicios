""" Listas 
Como los strings, las listas son secunencias de valores.
    en las listas, los valores pueden tener cualquier tipo
ej.
    [2,5,2]
    ['Colombia', 'Mexico', 'Argentina']
    ['Tortas', 8 , 'Tacos de canasta', 5]
Las listas son mutables, a diferencia de los strings
    my_list = [1,2,3]
    my_list[2] = 6

        my_list = [2, 'hola', True]
        my_list[1]
        'hola'


los indices de las listas, funcionan igual que los de los  strings
las listas se inician cin [] o con la funcion list

>>> countries = ['Mexico', 'Canada', 'Venezuela']
>>> ages = [20, 58, 27]
>>> id(ages)
140342889688712
>>> numbers = [20, 58, 27]
>>> id(numbers)
140342889689032
>>> numbers[0] = 85
>>> numbers
[85, 58, 27]

Alias - copiar lista sin afectar el valor origal  """

import copy 
In [17]: import copy                                                            

In [18]: paises                                                                 
Out[18]: ['Venezuela', 'Brasil', 'México']

In [19]: global_countries                                                       
Out[19]: ['Venezuela', 'Brasil', 'México']

In [20]: global_countries = None                                                

In [21]: global_countries                                                       

In [22]: global_countries = paises                                              

In [23]: global_countries = copy.copy(paises)                                   

In [24]: paises                                                                 
Out[24]: ['Venezuela', 'Brasil', 'México']

In [25]: global_countries                                                       
Out[25]: ['Venezuela', 'Brasil', 'México']

In [26]: paises[1] = 'Honduras'                                                 

In [27]: paises                                                                 
Out[27]: ['Venezuela', 'Honduras', 'México']

In [28]: global_countries                                                       
Out[28]: ['Venezuela', 'Brasil', 'México']

In [29]:  

#Importamos el 
In [40]: import random                                                          

In [41]: lista_num1 = list(range(0,100,2))                                      

In [42]: lista_num2 = list(range(0,10,1))                                       

In [43]: random_numbers = []                                                    

In [44]: for n in range (20)                                                    
  File "<ipython-input-44-9da5a7c89a2c>", line 1
    for n in range (20)
                       ^
SyntaxError: invalid syntax


In [45]: for n in range (20): # Ciclar 20 veces y anadir elementos de mamnera aleatoria del numero 0 al 18
    ...:     random_numbers.append(random.randint(0, 18)) 
    ...:                                                                        

In [46]: random_numbers                                                         
Out[46]: [2, 7, 2, 11, 10, 11, 2, 16, 7, 6, 7, 14, 5, 11, 6, 8, 8, 13, 0, 8]

In [47]: ordered_numbers = sorted(random_numbers)                               

In [48]: letter = [a,r,f,y,u,b]                                                 
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-48-4e36e82b78a6> in <module>
----> 1 letter = [a,r,f,y,u,b]

NameError: name 'a' is not defined

In [49]: letter = ['a', 'g', 'w', 'c', 'b']                                     

In [50]: letter_ordered = sorted (letter)                                       

In [51]: letter_ordered                                                         
Out[51]: ['a', 'b', 'c', 'g', 'w']
