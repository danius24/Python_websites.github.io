!pip install flask
from flask import Flask
app = Flask (_name_)
@app.route ('/')
def home ():
  return 'hello world'
  if _name_ == '_main_':
    app.run()
!pip install googletrans==4.0.0-rc1
from googletrans import Translator

nombre = input("Ingresa tu nombre: ")
print("Hola " + nombre + ", bienvenid@")

print("¿Qué deseas traducir?")
lenguaje = int(input("Elige (0) si es español-inglés o (1) si es inglés-español: "))

if lenguaje == 0:
    texto = input("Ingresa texto en español: ")
else:
    texto = input("Ingresa texto en inglés: ")

translator = Translator()

# Traducción del texto
if lenguaje == 0:
    traduccion = translator.translate(texto, dest='en', src='es')
    print(f'Tu texto fue traducido a inglés como: {traduccion.text}')
    print("Gracias por usar el traductor.")
else:
    traduccion = translator.translate(texto, dest='es', src='en')
    print(f'Tu texto fue traducido a español como: {traduccion.text}')
    print("Gracias por usar el traductor.")
    print('¿Te gustaría probar una función en español? Elige "si" o "no"')
    test = input("Elige 'si' o 'no': ")
    if test.lower() == "si":
        print("La actividad consiste en la búsqueda del significado de las palabras en diferentes regiones del habla hispana, con énfasis en el uso de jergas.")
        dic = {
            'amigo': 'parcero, pibe, pana, wey, tío, tronco, hermano, tronco, chaval, colega, compa, hermano, primo(pimo), picha, chocho, carnal, cuate, vato, causa, weon',
            'saludo': 'Que onda?, Que xopa?, Como esta la cosa?, Que más?, Que hue(Fue)?, Que hace wacho? Quibo?, Que pedo?, En que andas?, Que paso?'
        }

        ans = input("Ingresa texto: ").lower()

        if ans == "amigo":
            print(ans + " también puede escribirse como: " + dic['amigo'])
        elif ans == "saludo":
            print(ans + " también puede escribirse como: " + dic['saludo'])
        else:
            print("Error")

        # Llama a la función para recibir un comentario
        comentario = input("¿Quieres dejar un comentario? (si/no): ")
        if comentario.lower() == "si":
            recibir_comentario()

    elif test.lower() == "no":
        print("Se ha finalizado.")
    else:
        print("Opción no válida.")