# ===========================================
#                   PORTADA
# ===========================================
# Nombre: Elliutth Isaac Guevara Liñan
# Matricula: 2630015
# Grupo: IM 1-2
# ===========================================
#             RESUMEN EJECUTIVO
# ===========================================
# Un string en Python es un tipo de dato que representa
# una secuencia inmutable de caracteres, como letras,
# números, espacios y símbolos.
# Las operaciones básicas incluyen concatenar cadenas,
# obtener su longitud con len(), extraer subcadenas mediante
# slicing, buscar texto con find(), reemplazar contenido
# con replace(), dividir con split() y unir con join().
# La validación y normalización de entradas permite detectar
# datos incorrectos y mantener información consistente,
# especialmente en nombres, correos electrónicos y contraseñas.
# Este documento presenta seis problemas de procesamiento
# de cadenas con descripciones, entradas, salidas, validaciones
# y casos de prueba normales, límite y de error.
# ===========================================
#              BUENAS PRÁCTICAS
# ===========================================
# - Los strings son inmutables: sus transformaciones generan
#   nuevas cadenas sin modificar el texto original.
# - Utilizar strip() y lower() para normalizar entradas
#   antes de compararlas, cuando sea apropiado.
# - Evitar índices numéricos sin explicación y documentar
#   qué parte del texto extrae cada operación de slicing.
# - Preferir los métodos integrados de Python para procesar
#   cadenas en lugar de reescribir funciones existentes.
# - Validar primero que la entrada no esté vacía y después
#   comprobar que cumpla con el formato requerido.
# - Utilizar nombres de variables claros y mensajes de error
#   comprensibles para facilitar la lectura del código.
# ===========================================
#                PROBLEMAS
# ===========================================
# Problem 1: Full name formatter (name + initials)
# ===========================================
# Description:
# Receives a person's full name, removes extra spaces,
# converts the name to title case, and generates the
# initials of each word separated by periods.
#
# Inputs:
# - full_name: A string containing the person's full name.
#
# Outputs:
# - The formatted full name.
# - The initials separated by periods.
#
# Validations:
# - The name must not be empty.
# - The name must contain at least two words.
# - Numbers and special characters are not allowed.
#
# Test cases:
# 1) Normal:
#    Input: "elliutth isaac guevara"
#    Expected: "Elliutth Isaac Guevara"
#              "E.I.G."
#
# 2) Border:
#    Input: "Ana López"
#    Expected: "Ana López"
#              "A.L."
#
# 3) Error:
#    Input: "Ana"
#    Expected: "Please enter at least two names."
full_name = input("Enter your name:\n") # ejemplo "   ElliUtth isAac gueVara liñaN   " 
full_names = full_name.split()
number_in_your_name = False
special_character_in_name = False
special_characters = "!#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

if len(full_names) < 2:
    print("Please enter at least two names.")
else:
    if full_name.strip() == "":
        print("Your name cannot be empty.")
    for character_numeric in full_name:
        if character_numeric >= "0" and character_numeric <= "9":
            number_in_your_name = True
        if character_numeric in special_characters:
            special_character_in_name = True

    if number_in_your_name:
        print("Your name must not contain numbers.")
    elif special_character_in_name:
        print("Don't use special characters.")
    else:
        full_name = full_name.strip().title()
        print(full_name) 
        full_names = full_name.split()
        full_name_initials = [initial[0].upper() for initial in full_names]
        initials = ".".join(full_name_initials)+"." 
        print(initials) 


# ===========================================
# Problem 2: Simple email validator
# (structure + domain)
# ===========================================
# Description:
# Checks whether an email address follows a basic format.
# If the email is valid, extracts and displays the domain
# located after the @ symbol.
#
# Inputs:
# - email_text: A string containing an email address.
#
# Outputs:
# - "Valid email: true" if the email passes validation.
# - "Valid email: false" otherwise.
# - "Domain: <domain_part>" when the email is valid.
#
# Validations:
# - The email must not be empty after strip().
# - The email must contain exactly one @ symbol.
# - The email must not contain spaces.
# - The domain must contain a period after the @ symbol.
#
# Test cases:
# 1) Normal:
#    Input: "elliutthisaac@gmail.com"
#    Expected: "Valid email: true"
#              "Domain: gmail.com"
#
# 2) Border:
#    Input: "a@b.c"
#    Expected: "Valid email: true"
#              "Domain: b.c"
#
# 3) Error:
#    Input: "ana.gmail.com"
#    Expected: "Valid email: false"

email_text = input("Email address:") #"elliutthisaac@gmail.com"

email_text = email_text.strip()

number_of_ats = email_text.count("@")
validation = email_text.find("@")

no_spaces = " " not in email_text

if (email_text != "" and
    number_of_ats == 1 and
    no_spaces and
    "." in email_text[validation + 1:]):

    print("Valid email: true")

    domain_part = email_text[validation + 1:]
    print("Domain:", domain_part)

else:
    print("Valid email: false")

# ===========================================
# Problem 3: Palindrome checker
# (ignoring spaces and case)
# ===========================================
# Description:
# Determines whether a phrase reads the same forward
# and backward, ignoring spaces and letter case.
# Displays the normalized phrase and the result.
#
# Inputs:
# - phrase: A string containing a phrase to check.
#
# Outputs:
# - "Is palindrome: true" if the phrase is a palindrome.
# - "Is palindrome: false" otherwise.
# - "Normalized phrase: <normalized_phrase>" when processed.
#
# Validations:
# - The phrase must not be empty after strip().
# - The normalized phrase must contain at least three characters.
#
# Test cases:
# 1) Normal:
#    Input: "Anita lava la tina"
#    Expected: "Is palindrome: true"
#              "Normalized phrase: anitalavalatina"
#
# 2) Border:
#    Input: "aba"
#    Expected: "Is palindrome: true"
#              "Normalized phrase: aba"
#
# 3) Error:
#    Input: "ab"
#    Expected: "Is palindrome: false"

phrase = input("Enter a phrase: ")

phrase = phrase.strip()

normalized_phrase = phrase.lower().replace(" ", "")

if phrase == "" or len(normalized_phrase) < 3:
    print("Is palindrome: false")
else:
    reversed_phrase = normalized_phrase[::-1]


    if normalized_phrase == reversed_phrase:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")

    print("Normalized phrase:", normalized_phrase)


# ===========================================
# Problem 4: Sentence word stats
# (lengths and first/last word)
# ===========================================
# Description:
# Receives a sentence, removes extra spaces, and separates
# it into words. Calculates the word count and identifies
# the first, last, shortest, and longest words.
#
# Inputs:
# - sentence: A string containing a sentence.
#
# Outputs:
# - "Word count: <n>"
# - "First word: <first_word>"
# - "Last word: <last_word>"
# - "Shortest word: <shortest_word>"
# - "Longest word: <longest_word>"
#
# Validations:
# - The sentence must not be empty after strip().
# - The sentence must contain at least one word after split().
#
# Test cases:
# 1) Normal:
#    Input: "Python is very useful"
#    Expected:
#      Word count: 4
#      First word: Python
#      Last word: useful
#      Shortest word: is
#      Longest word: Python
#
# 2) Border:
#    Input: "Hi"
#    Expected:
#      Word count: 1
#      First word: Hi
#      Last word: Hi
#      Shortest word: Hi
#      Longest word: Hi
#
# 3) Error:
#    Input: "   "
#    Expected: "Invalid sentence"

sentence = input("Enter a sentence: ")

sentence = sentence.strip()

words = sentence.split()

if len(words) == 0:
    print("Invalid sentence")
else:
    word_count = len(words)
    first_word = words[0]
    last_word = words[-1]
    shortest_word = words[0]
    longest_word = words[0]

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word

        if len(word) > len(longest_word):
            longest_word = word

    print("Word count:", word_count)
    print("First word:", first_word)
    print("Last word:", last_word)
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)


# ===========================================
# Problem 5: Password strength classifier
# ===========================================
# Description:
# Classifies a password as weak, medium, or strong
# according to its length and character types.
#
# Inputs:
# - password_input: A string containing a password.
#
# Outputs:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"
# - "Password cannot be empty" for empty input.
#
# Validations:
# - The password must not be empty.
# - Passwords shorter than eight characters are weak.
# - A strong password must contain an uppercase letter,
#   a lowercase letter, a digit, and a symbol.
# - A medium password must contain letters and digits,
#   or both uppercase and lowercase letters.
#
# Test cases:
# 1) Normal:
#    Input: "Abcdef1!"
#    Expected: "Password strength: strong"
#
# 2) Border:
#    Input: "Abcdef1"
#    Expected: "Password strength: weak"
#
# 3) Error:
#    Input: ""
#    Expected: "Password cannot be empty"

password_input = input("Enter a password: ")

if password_input == "":
    print("Password cannot be empty")
else:
    if len(password_input) < 8:
        strength = "weak"
    else:
        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False

        for char in password_input:
            if char.isupper():
                has_upper = True

            elif char.islower():
                has_lower = True

            elif char.isdigit():
                has_digit = True

            elif not char.isalnum():
                has_symbol = True

        if has_upper and has_lower and has_digit and has_symbol:
            strength = "strong"

        elif ((has_upper or has_lower) and has_digit):
            strength = "medium"

        elif has_upper and has_lower:
            strength = "medium"

        else:
            strength = "weak"

    print("Password strength:", strength)


# ===========================================
# Problem 6: Product label formatter
# (fixed-width text)
# ===========================================
# Description:
# Receives a product name and a positive price.
# Creates a formatted product label with a fixed length
# of exactly 30 characters, truncating or padding as needed.
#
# Inputs:
# - product_name: A string containing the product name.
# - price_value: A string representing a positive number.
#
# Outputs:
# - "Label: <label>" where the label contains 30 characters.
# - "Invalid product name" if the name is empty.
# - "Invalid price" if the price is not a positive number.
#
# Validations:
# - The product name must not be empty after strip().
# - The price must represent a positive numeric value.
# - The final label must contain exactly 30 characters.
#
# Test cases:
# 1) Normal:
#    Input: product_name = "Pen", price_value = "10"
#    Expected: A 30-character label beginning with
#              "Product: Pen | Price: $10"
#
# 2) Border:
#    Input: product_name = "", price_value = "10"
#    Expected: "Invalid product name"
#
# 3) Error:
#    Input: product_name = "Pen", price_value = "-5"
#    Expected: "Invalid price"

product_name = input("Enter product name: ").strip()
price_value = input("Enter product price: ").strip()

if product_name == "":
    print("Invalid product name")

elif price_value.replace(".", "", 1).isdigit() and float(price_value) > 0:
    label = f"Product: {product_name} | Price: ${price_value}"
    label = label[:30]
    label = label.ljust(30)

    print(f'Label: "{label}"')

else:
    print("Invalid price")

# ========================================
# conclusiones 
# ========================================
# El manejo de strings es esencial para recibir y mostrar datos correctamente.
# lower() convierte el texto a minúsculas y strip() elimina espacios externos.
# split() separa palabras y join() permite unirlas con un separador.
# Normalizar el texto ayuda a evitar errores al comparar cadenas.
# Las validaciones permiten detectar datos vacíos o incorrectos.
# Los strings son inmutables, por lo que sus métodos generan nuevas cadenas.
# Los slices permiten extraer partes de un texto o invertirlo fácilmente.
# ========================================
# Referencias
# ========================================
# 1) lenovo glosario strings 
# https://www.lenovo.com/mx/es/glosario/string/?orgRef=https%253A%252F%252Fwww.google.com%252F
# 2) strings mas que un simple array 
# https://dev.to/aws/strings-en-programacion-mas-que-un-simple-array-de-caracteres-1knd
# 3) busqueda con patrones 
# https://www.aulascript.com/lenguaje/objetos/string/buscar_con_patrones.htm
# 4) documentos de python 
# https://docs.python.org/es/3/howto/regex.html
# 5) importancia de la validacion 
# https://medium.com/design-bootcamp/the-importance-of-input-validation-and-error-handling-5359a4cd7a80