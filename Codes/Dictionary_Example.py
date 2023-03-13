#CREATE A DITIONARY 
planet = {
    'name' : 'Mars',
    'moons':2
}
# two forms can retrive information using get or printf
print(f'{planet["name"]} has {planet["moons"]} moon(s)')
#update information  and created a ditionary inside dictionary
planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')
###############################################################################################
Recuperación de todas las claves y valores
El método keys() devuelve un objeto de lista que contiene todas las claves. Puede usar este método para iterar por todos los elementos del diccionario.

Imagine que tiene el siguiente diccionario, en el que se almacenan los últimos tres meses de precipitaciones.

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
Muestra de todas las precipitaciones
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')
# Output:
# october: 3.5cm
# november: 4.2cm
# december: 2.1cm
#######################################
Determinación de la existencia de una clave en un diccionario
Al actualizar un valor en un diccionario, Python sobrescribirá el valor existente o creará uno, si la clave no existe. 
Si quiere agregar a un valor en lugar de sobrescribirlo, puede comprobar si la clave existe mediante in. 
Por ejemplo, si quiere agregar un valor a diciembre o crear uno si no existe, puede usar lo siguiente:


if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1

# Because december exists, the value will be 3.1
################################################
Recuperación de todos los valores
De forma similar a keys(), values() devuelve la lista de todos los valores de un diccionario sin sus claves correspondientes. values() puede resultar útil cuando se usa la clave con fines de etiquetado,
como en el ejemplo anterior, en el que las claves son el nombre del mes. Puede usar para values() determinar el importe total de las precipitaciones:
  
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter')

# Output:
# There was 10.8cm in the last quarter
#####################################
Example caculate average  planets of the moons
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
moons = planet_moons.values()
total_planets=len(planet_moons.keys())
total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

average = total_moons / total_planets

print(f'Each planet has an average of {average} moons')
