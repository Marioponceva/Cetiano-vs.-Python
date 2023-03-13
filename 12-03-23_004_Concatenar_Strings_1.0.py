#Mario Alberto Ponce Vazquez
#Registro: 20310317
#Materia: Ingeligencia Artificial
#Curso de Python: Capi≠tulo 4. Como concatenar Strings 2


#Ejercicio 7. Concatenar dos strings en una variable

#Creamos una variable string y concatemos con el operador + ambas cadenas
ProgramarPython = "°Programar Python " + "es facil!"

#Imprimimos la concatenacion
print(ProgramarPython)

#Ejercicio 8. Concatena dos variables con strings en una tercera variable.

#Creamos dos variables por separado de tipo string
ProgramarPython1 = "°Programar Python "
ProgramarPython2 = "es facil!"

#En una tercera variable concatemaos ambos mensajes
ProgramarPython3 = ProgramarPython1 + ProgramarPython2

#Finalmente lo imprimimos
print(ProgramarPython3)

#Ejercicio 9. Concatena una variable con string y un string directamente en un print().

#Creamos la varaible Escuela y le asignamos el valor de CETI
Escuela = "CETI"

print(Escuela + " Colomos es lo maximo")

#Ejercicio 10. Escribe tu nombre y apellidos separados en variables. 
#Despues concatena estas variables dentro de otra. No te olvides de concatenar los espacios entre el nombre y cada apellido. 
#Finalmente, imprime el resultado.

#Creamos dos variables, una para apellidos y otra para nombres y dentro concatenamos mensajes
Nombres = "Mario" + " " + "Alberto"
Apellidos = "Ponce" + " " + "Vazquez"
#Despues en una tercera variable concatenamos las concatenaciones anteriores
NombreCompleto = Nombres + " " + Apellidos

#Imprimimos el nombre completo
print(NombreCompleto)

#Ejercicio 11. Concatena dos n√∫meros, no los sumes.

#Declaramos dos numeros pero en tipo de dato string para poder concatenarlos
Numero1 = "90"
Numero2 = "210"

#Concatemos ambos numeros
NumeroConcatenado = Numero1 + Numero2

#Imprimimos el resultado
print(NumeroConcatenado)

