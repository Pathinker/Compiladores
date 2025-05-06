import ply.lex as lex

# -------------------------------------------------------------
# lexer.py - Analizador Léxico para Expresiones Aritméticas y Lógicas
#
# Este archivo define todos los tokens, palabras clave y símbolos
# que el parser espera recibir para evaluar expresiones tanto 
# aritméticas como lógicas.
#
# - Los tokens incluyen operadores aritméticos (+, -, *, /), 
#   operadores lógicos (AND, OR, NOT), paréntesis, y valores 
#   booleanos (TRUE, FALSE, 1, 0), así como números enteros.
#
# - Las funciones t_... definen las reglas de reconocimiento para
#   cada token, usando expresiones regulares.
#
# - El lexer transforma la entrada en una secuencia de tokens para
#   que el parser (parser.py) pueda analizar y evaluar las expresiones.
#
# -------------------------------------------------------------

tokens = (
    'NUMBER',
    'BOOLEAN',
    'AND',
    'OR',
    'NOT',
    'LPAREN',
    'RPAREN',
    'NEWLINE',
)

literals = ['+', '-', '*', '/', '(', ')']

# Definición de tokens
t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'
t_BOOLEAN = r'TRUE|FALSE|1|0'  # Modificado para aceptar '1' y '0'

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t'  # Ignorar espacios y tabulaciones

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_NUMBER(t):
    r'\d+'  # Reconocer números enteros
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Caracter ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()