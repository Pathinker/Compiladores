import ply.lex as lex

# -------------------------------------------------------------
# lexer.py - Analizador Léxico usando PLY
#
# Este archivo define todos los tokens, palabras clave y símbolos
# que el parser espera recibir.
#
# - tokens: Son símbolos complejos que requieren expresiones regulares.
#           Ej: NUMBER, IDENTIFIER, IF, ELSE, etc.
#
# - literals: Son caracteres simples que se reconocen directamente
#             sin necesidad de expresión regular.
#             Ej: '+', '-', '*', '/', '(', ')', etc.
#
# - Las funciones t_... definen las reglas de reconocimiento para
#   cada token.
#
# - El lexer transforma la entrada en una secuencia de tokens para
#   que el parser (parser.py) la pueda interpretar.
# -------------------------------------------------------------

tokens = (
    'NUMBER',
    'NEWLINE',
)

literals = ['+', '-', '*', '/', '(', ')']

t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Manejo de nuevas líneas
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    print(f"Caracter ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()