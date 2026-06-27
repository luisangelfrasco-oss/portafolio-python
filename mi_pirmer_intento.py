first_name="Mariana"
last_name="Bueno"
age=23
country="Méxicana"
full_info=f"Ella es {first_name}  {last_name} y tiene {age} años, tiene nacionalidad {country}"

print(full_info)

foods_str="enchiladas | caldo de res | salsa valentina | mole"
drinks_str="cafe | cafe de olla | limonada | agua simple | cafe muy dulce"
animals_str="patos | mosquitos"
tv_shows_str="avatar, el ultimo maestro aire | la leyenda de corra"

foods=foods_str.split(" | ")
tv_shows=tv_shows_str.split(" | ")
animals=animals_str.split(" | ")
drinks=drinks_str.split(" | ")

things_she_loves=f"""Ella realmente adora la serie de {tv_shows[0]}, ama a todos los animales pero especialmente a los {animals[0]}. 
Sus bebidas favoritas son el {drinks[0]}, el {drinks[1]} y la {drinks[2]}. Sus comidas favoritas son  las {foods[0]} y el {foods[1]}."""

print(things_she_loves)

things_she_hates=f"""Si bien ella realmente adora todo tipo de vida animal, hay uno al cual ella no tolera y son los {animals[1]}. En cuanto a programas de 
television ella detesta {tv_shows[1]}, la cual es la secuela de la leyenda de avatar, especialmente por su protagonista la cual no es la mejor...
En cuanto a las bebidas, realmente no odia la {drinks[3]} pero no es lo que mas prefiere, otra bebida que no le gusta es el {drinks[-1]}.
Por ultimo, ella enserio detesta y odia a muerte la {foods[-2]} y el {foods[-1]}"""
#en el caso de usar acortaciones con [] y numeros negativos, la parte del final debe quedar vacia [-inicio:(valor vacio)]

print(things_she_hates)