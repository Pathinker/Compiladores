def validate_alpha(s):
    return s.isalpha()

def validate_real(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def validate_if_else(s):
    return "if" in s and "else" in s

input_string = "HelloWorld"

if validate_alpha(input_string):
    print("Cadena Valida")
else:
    print("Cadena Invalida")