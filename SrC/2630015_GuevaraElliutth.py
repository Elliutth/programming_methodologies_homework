# ==================================
#              PORTADA
# ==================================
# Nombre: Elliutth Isaac Guevar Liñan
# Matricula: 2630015
# Grupo: IM 1-2
# ==================================
#         RESUMEN EJECUTIVO
# ==================================
# En Python, el tipo int representa números enteros, mientras que float permite trabajar con números decimales.
# La diferencia principal es que int no tiene parte decimal y float puede representar valores con decimales.
# Un booleano es un tipo de dato que solo puede tomar dos valores: True (verdadero) o False (falso).
# Los booleanos se obtienen mediante comparaciones, como edad >= 18, que devuelve True o False.
# Validar rangos permite comprobar que los datos ingresados estén dentro de los límites permitidos.
# También es importante evitar la división entre cero, ya que provoca un error ZeroDivisionError en Python.
# Mi documento describirá cada problema, el diseño de sus entradas y salidas y las validaciones aplicadas.
# Además, explicará cómo se utilizan int, float y booleanos para realizar cálculos y tomar decisiones.
# ==================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# ==================================
# 1. Usar los tipos de datos apropiados: int para contadores y float para cantidades con decimales.
# 2. Evitar duplicar expresiones complejas, guardando los resultados intermedios en variables.
# 3. Validar los datos antes de realizar operaciones, comprobando que las horas y los salarios no sean negativos.
# 4. Utilizar nombres de variables descriptivos y mensajes claros para facilitar la comprensión del programa.
# 5. Documentar el significado de los booleanos: True indica que una condición se cumple y False que no se cumple.
# ==================================
#           PROBLEMAS
# ==================================
# Problem 1: Temperature converter
# and range flag
# ==================================
# Description:
# Converts a temperature from Celsius to Fahrenheit and Kelvin.
# Determines whether the temperature is high.
#
# Inputs:
# - temp_c (float; temperature in Celsius)
#
# Outputs:
# - "Fahrenheit:" <temp_f>
# - "Kelvin:" <temp_k>
# - "High temperature:" true|false
#
# Validations:
# - Verify that temp_c can be converted to float.
# - temp_k must be >= 0.0
#
# Test cases:
# 1) Normal: temp_c = 25
# 2) Border: temp_c = -273.15
# 3) Error: invalid input or temp_c < -273.15
# ==========================================

temp_c = input("Enter a temperature in Celsius: ")

if temp_c.replace(".", "", 1).replace("-", "", 1).isdigit():

    temp_c = float(temp_c)
    temp_k = temp_c + 273.15

    if temp_k < 0.0:
        print("Error: Temperature is impossible in Kelvin.")
    else:
        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = (temp_c >= 30.0)

        print(f"Fahrenheit: {temp_f}")
        print(f"Kelvin: {temp_k}")
        print(f"High temperature: {str(is_high_temperature).lower()}")

else:
    print("Error: Please enter a valid number.")


# ==================================
# Problem 2: Weekly pay calculator
# ==================================
# Description:
# Calculates a worker's total weekly pay.
# Overtime hours are paid at 150% of the regular rate.
#
# Inputs:
# - hours_worked (float; weekly hours worked)
# - hourly_rate (float; payment per hour)
#
# Outputs:
# - "Regular pay:" <regular_pay>
# - "Overtime pay:" <overtime_pay>
# - "Total pay:" <total_pay>
# - "Has overtime:" true|false
#
# Validations:
# - hours_worked >= 0
# - hourly_rate > 0
# - Inputs must be valid numbers.
#
# Test cases:
# 1) Normal: hours_worked = 35, hourly_rate = 100
# 2) Border: hours_worked = 40, hourly_rate = 100
# 3) Error: hours_worked = -5 or hourly_rate = 0
# ==========================================

hours_worked = input("Enter hours worked: ")
hourly_rate = input("Enter hourly rate: ")

if (hours_worked.replace(".", "", 1).isdigit() and
    hourly_rate.replace(".", "", 1).isdigit()):

    hours_worked = float(hours_worked)
    hourly_rate = float(hourly_rate)

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay

        has_overtime = (hours_worked > 40)

        print(f"Regular pay: {regular_pay}")
        print(f"Overtime pay: {overtime_pay}")
        print(f"Total pay: {total_pay}")
        print(f"Has overtime: {str(has_overtime).lower()}")

else:
    print("Error: invalid input")

# ==================================
# Problem 3: Discount eligibility
# with booleans
# ==================================
# Description:
# Determines whether a customer qualifies for a discount.
# Applies a 10% discount when at least one condition is met.
#
# Inputs:
# - purchase_total (float; total purchase amount)
# - is_student_text (string; YES or NO)
# - is_senior_text (string; YES or NO)
#
# Outputs:
# - "Discount eligible:" true|false
# - "Final total:" <final_total>
#
# Validations:
# - purchase_total >= 0.0
# - Normalize text to uppercase.
# - Responses must be YES or NO.
#
# Test cases:
# 1) Normal: purchase_total = 500, student = YES, senior = NO
# 2) Border: purchase_total = 1000, student = NO, senior = NO
# 3) Error: negative purchase_total or invalid response
# ==========================================
purchase_total = input("Enter purchase total: ")
is_student_text = input("Are you a student? (YES/NO): ")
is_senior_text = input("Are you a senior? (YES/NO): ")

is_student_text = is_student_text.upper()
is_senior_text = is_senior_text.upper()

if purchase_total.replace(".", "", 1).isdigit():

    purchase_total = float(purchase_total)

    if (purchase_total < 0 or
        (is_student_text != "YES" and is_student_text != "NO") or
        (is_senior_text != "YES" and is_senior_text != "NO")):

        print("Error: invalid input")

    else:
        is_student = (is_student_text == "YES")
        is_senior = (is_senior_text == "YES")

        discount_eligible = (
            is_student or
            is_senior or
            (purchase_total >= 1000.0)
        )

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print(f"Discount eligible: {str(discount_eligible).lower()}")
        print(f"Final total: {final_total}")

else:
    print("Error: invalid input")

    
# ==================================
# Problem 4: Basic statistics
# of three integers
# ==================================
# Description:
# Calculates the sum, average, maximum, and minimum.
# Determines whether all three integers are even.
#
# Inputs:
# - n1 (int; first integer)
# - n2 (int; second integer)
# - n3 (int; third integer)
#
# Outputs:
# - "Sum:" <sum_value>
# - "Average:" <average_value>
# - "Max:" <max_value>
# - "Min:" <min_value>
# - "All even:" true|false
#
# Validations:
# - Verify that all three inputs can be converted to int.
# - Negative integers are allowed.
#
# Test cases:
# 1) Normal: n1 = 2, n2 = 4, n3 = 6
# 2) Border: n1 = 0, n2 = -2, n3 = 2
# 3) Error: one or more inputs are not integers
# ==========================================

n1 = input("Enter the first integer: ")
n2 = input("Enter the second integer: ")
n3 = input("Enter the third integer: ")

if (n1.lstrip("-").isdigit() and
    n2.lstrip("-").isdigit() and
    n3.lstrip("-").isdigit()):

    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)

    all_even = (
        n1 % 2 == 0 and
        n2 % 2 == 0 and
        n3 % 2 == 0
    )

    print(f"Sum: {sum_value}")
    print(f"Average: {average_value}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")

else:
    print("Error: invalid input")

# ==================================
# Problem 5: Loan eligibility
# ==================================
# Description:
# Calculates the ratio of monthly debt to income.
# Determines eligibility based on income, debt ratio, and credit score.
#
# Inputs:
# - monthly_income (float; monthly income)
# - monthly_debt (float; monthly debt payments)
# - credit_score (int; credit score)
#
# Outputs:
# - "Debt ratio:" <debt_ratio>
# - "Eligible:" true|false
#
# Validations:
# - monthly_income > 0.0
# - monthly_debt >= 0.0
# - credit_score >= 0
# - Inputs must have valid numeric formats.
#
# Test cases:
# 1) Normal: income = 10000, debt = 3000, score = 700
# 2) Border: income = 8000, debt = 3200, score = 650
# 3) Error: income = 0, debt < 0, or score < 0
# ==========================================

monthly_income = input("Enter monthly income: ")
monthly_debt = input("Enter monthly debt: ")
credit_score = input("Enter credit score: ")

if (monthly_income.replace(".", "", 1).isdigit() and
    monthly_debt.replace(".", "", 1).isdigit() and
    credit_score.isdigit()):

    monthly_income = float(monthly_income)
    monthly_debt = float(monthly_debt)
    credit_score = int(credit_score)

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income

        eligible = (
            monthly_income >= 8000.0 and
            debt_ratio <= 0.4 and
            credit_score >= 650
        )

        print(f"Debt ratio: {debt_ratio}")
        print(f"Eligible: {str(eligible).lower()}")

else:
    print("Error: invalid input")


# ==================================
# Problem 6: Body Mass Index (BMI)
# and category flag
# ==================================
# Description:
# Calculates BMI using weight in kilograms and height in meters.
# Determines the BMI category using the specified ranges.
#
# Inputs:
# - weight_kg (float; weight in kilograms)
# - height_m (float; height in meters)
#
# Outputs:
# - "BMI:" <bmi_rounded>
# - "Underweight:" true|false
# - "Normal:" true|false
# - "Overweight:" true|false
#
# Validations:
# - weight_kg > 0.0
# - height_m > 0.0
# - Inputs must be valid numbers.
#
# Test cases:
# 1) Normal: weight = 67, height = 1.67
# 2) Border: BMI = 18.5 or BMI = 25.0
# 3) Error: weight <= 0 or height <= 0
# ==========================================

weight_kg = input("Enter weight in kilograms: ")
height_m = input("Enter height in meters: ")

if (weight_kg.replace(".", "", 1).isdigit() and
    height_m.replace(".", "", 1).isdigit()):

    weight_kg = float(weight_kg)
    height_m = float(height_m)

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)

        is_underweight = (bmi < 18.5)
        is_normal = (18.5 <= bmi < 25.0)
        is_overweight = (bmi >= 25.0)

        print(f"BMI: {round(bmi, 2)}")
        print(f"Underweight: {str(is_underweight).lower()}")
        print(f"Normal: {str(is_normal).lower()}")
        print(f"Overweight: {str(is_overweight).lower()}")

else:
    print("Error: invalid input")

# ==========================================
# 8. CONCLUSIONES
#
# Los enteros y los flotantes se utilizan juntos para realizar
# cálculos con números enteros y valores decimales de la vida real.
# Las comparaciones generan booleanos (True o False) que permiten
# tomar decisiones dentro del programa mediante instrucciones if.
# Validar los rangos de entrada y evitar divisiones entre cero
# ayuda a prevenir errores y obtener resultados confiables.
# Aprendí a combinar condiciones con and, or y not para evaluar
# reglas en problemas de nómina, descuentos, préstamos y otros casos.
# ==========================================
# Referencias
# https://docs.python.org/3/builtins/stdtypes.html
# https://docs.python.org/3/tutorial/introduction.html
# https://greenteapress.com/wp/think-python-2e/
# https://openstax.org/books/introduction-python-programming/pages/1-introduction
# https://docs.python.org/3/tutorial/errors.html