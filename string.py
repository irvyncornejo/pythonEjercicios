country = 'Mexico'

print(country)
# Saber la letra segun el indice
country[0]
#para contar la cadena de texto
len(country)

print(len(country))

# Para saber el id de una letra
print(id (country[1]))

#Python reutiliza las letras, por eso los str son inmutables

# Los string son inmutables, no se pueden modificar. Osea si se modica la cadena de text
# este genera una nueva cadena que es alacena en un nuevo espacio de memoria
print(id(country)) # id del objeto sin anadir natural o declarado al principio
country += 'R' # Se anade a la cadena country la letra 'R'
print(country) 
print(id(country))# el id de la cadena country cambia porque se anadio la letra 'R', se creo un nuevo str


