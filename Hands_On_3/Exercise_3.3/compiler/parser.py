import ply.yacc as yacc
from lexer import tokens

# -------------------------------------------------------------
# parser.py - Analizador Sintáctico para Expresiones Aritméticas y Lógicas
#
# Este archivo define la gramática del lenguaje para evaluar 
# expresiones aritméticas y lógicas combinadas.
#
# - Utiliza los tokens definidos en lexer.py para interpretar 
#   expresiones que combinan operaciones aritméticas (+, -, *, /)
#   y lógicas (AND, OR, NOT).
#
# - El parser aplica las reglas de precedencia para asegurarse 
#   de que las operaciones se evalúen correctamente. Las operaciones
#   aritméticas tienen menor precedencia que las operaciones lógicas, 
#   y dentro de las operaciones aritméticas se respeta el orden convencional.
#
# - Se manejan tanto expresiones simples como agrupadas en paréntesis.
#
# - El parser simplemente valida si la expresión es correcta, 
#   sin retornar un valor.
#
# -------------------------------------------------------------

# Determinar el orden de los operadores para evitar ambigüedades.
precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('left', 'AND', 'OR'),
    ('right', 'NOT'),
    ('right', 'UMINUS'),
)

# Reglas de Gramática

def p_input(p):
    'input : expr NEWLINE'
    print("Expresión válida")

def p_input_error(p):
    'input : error NEWLINE'
    print("Expresión inválida")
    parser.errok()

# Reglas para operaciones aritméticas
def p_expr_binop(p):
    '''expr : expr '+' expr
            | expr '-' expr
            | expr '*' expr
            | expr '/' expr'''
    pass

# Reglas para operaciones lógicas
def p_expr_binop_logic(p):
    '''expr : expr AND expr
            | expr OR expr'''
    pass

def p_expr_not(p):
    'expr : NOT expr'
    pass

def p_expr_group(p):
    'expr : LPAREN expr RPAREN'
    pass

# Reglas para números y valores booleanos
def p_expr_number(p):
    'expr : NUMBER'
    pass

def p_expr_boolean(p):
    'expr : BOOLEAN'
    pass

def p_expr_uminus(p):
    'expr : \'-\' expr %prec UMINUS'
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}'")
    else:
        print("Error de sintaxis al final de la entrada")

try:
    parser = yacc.yacc()
except yacc.YaccError as e:
    print(f"Error al construir el parser: {e}")