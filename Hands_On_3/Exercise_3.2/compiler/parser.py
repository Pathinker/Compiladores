import ply.yacc as yacc
from lexer import tokens

# -------------------------------------------------------------
# parser.py - Analizador Sintáctico para Validación de Expresiones Lógicas
#
# Este archivo define la gramática del lenguaje que se desea reconocer
# para validar expresiones lógicas simples (AND, OR, NOT).
#
# - Usa los tokens definidos en lexer.py.
# - Define reglas de producción (expr, input, etc.) con funciones p_...
# - El parser analiza la estructura de la secuencia de tokens producida
#   por el lexer y verifica si corresponde a una gramática válida.
#
# -------------------------------------------------------------

# Determinar el orden de los operadores lógicos para evitar ambigüedades.
# Útil para jerarquía de operaciones.

precedence = (
    ('left', 'AND', 'OR'),
    ('right', 'NOT'),
)

# Reglas de Grámatica

def p_input(p):
    'input : expr NEWLINE'
    print("Expresión lógica válida")

def p_input_error(p):
    'input : error NEWLINE'
    print("Expresión lógica inválida")
    parser.errok()

def p_expr_binop(p):
    '''expr : expr AND expr
            | expr OR expr'''
    if p[2] == 'AND': p[0] = p[1] and p[3]
    elif p[2] == 'OR': p[0] = p[1] or p[3]

def p_expr_not(p):
    'expr : NOT expr'
    p[0] = not p[2]

def p_expr_group(p):
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_expr_boolean(p):
    'expr : BOOLEAN'
    p[0] = True if p[1] == 'TRUE' else False

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis al final de la entrada")

try:
    parser = yacc.yacc()
except yacc.YaccError as e:
    print(f"Error al construir el parser: {e}")