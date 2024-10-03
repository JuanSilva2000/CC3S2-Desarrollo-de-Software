from behave import given, when, then
import re

numeros_espaniol = {
    "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
    "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
    "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
    "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
    "ochenta": 80, "noventa": 90, "media": 0.5, "un montón": 999, "veinticinco": 25, "mil": 1000
}  
  
numeros_ingles = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
    "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90
}

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        if palabra in numeros_espaniol:  
            return numeros_espaniol.get(palabra.lower(), 0)  
        elif palabra in numeros_ingles: 
            return numeros_ingles.get(palabra.lower(),0)
    
@given('que he comido {cukes}')
def step_given_eaten_cukes(context, cukes):
    cukes = cukes.replace(" pepinos","")
    cukes = cukes.replace(" de","")
    cukes = cukes.replace('"','').lower()
    context.belly.comer(convertir_palabra_a_numero(cukes))  

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('y', ' ')
    time_description = time_description.replace('and', ' ')
    time_description = time_description.strip()

    if time_description == 'media hora':
        total_time_in_hours = 0.5
    else:
        pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?\s*(?:(\w+)\s*segundos?)?')  
          
        pattern_2 = re.compile(r'(?:(\w+)\s*hours?)?\s*(?:(\w+)\s*minutes?)?\s*(?:(\w+)\s*seconds?)?')  

        match = pattern.match(time_description)
        match_2 = pattern_2.match(time_description)
        
        if match.group(1) != None or match.group(2) != None or match.group(3) != None:
            hours_word = match.group(1) or "0"
            minutes_word = match.group(2) or "0"
            seconds_word = match.group(3) or "0"

            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)
            seconds = convertir_palabra_a_numero(seconds_word)

            total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)  
        
        elif match_2.group(1) != None or match_2.group(2) != None or match_2.group(3) != None:  
            hours_word = match_2.group(1) or "0"
            minutes_word = match_2.group(2) or "0"
            seconds_word = match_2.group(3) or "0"

            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)
            seconds = convertir_palabra_a_numero(seconds_word)

            total_time_in_hours = hours + (minutes / 60) + (seconds / 3600) 
            
        else:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

    context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."  
      
@then('debería ocurrir un error de cantidad no válida')
def step_then_invalid_cucumber_amount(context):
    try:
        assert context.belly.pepinos_comidos < 100, "Cantidad de pepinos no válida"
    except AssertionError as e:
        print(str(e))