import ply.yacc as yacc
from lexer import tokens

# -------------------------------------------------------------
# parser.py - Analizador Sintáctico usando PLY
#
# Este archivo define la gramática del lenguaje que se desea reconocer.
#
# - Usa los tokens definidos en lexer.py.
# - Define reglas de producción (expr, input, etc.) con funciones p_...
# - Utiliza reglas de precedencia para manejar ambigüedad.
# - El parser analiza la estructura de la secuencia de tokens producida
#   por el lexer y verifica si corresponde a una gramática válida.
#
# -------------------------------------------------------------

# Determinar el orden de los caracteres para evitar ambiguedades.
# Útil para jerarquia de operaciones.

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

# Reglas de Grámatica

def p_input(p):
    'input : expr NEWLINE'
    print("Expresión válida")

def p_input_error(p):
    'input : error NEWLINE'
    print("Expresión inválida")
    parser.errok()

def p_expr_binop(p):
    '''expr : expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr'''
    if p[2] == '+': p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]

def p_input(p):
    'input : expr NEWLINE'
    print("Expresión válida")

def p_expr_uminus(p):
    'expr : \'-\' expr %prec UMINUS'
    p[0] = -p[2]

def p_expr_group(p):
    'expr : "(" expr ")"'
    p[0] = p[2]

def p_expr_number(p):
    'expr : NUMBER'
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis al final de la entrada")

try:
    parser = yacc.yacc()
except yacc.YaccError as e:
    print(f"Error al construir el parser: {e}")