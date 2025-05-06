import ply.lex as lex

# -------------------------------------------------------------
# lexer.py - Analizador Léxico para Validación de Expresiones Lógicas
#
# Este archivo define todos los tokens, palabras clave y símbolos
# que el parser espera recibir para validar expresiones lógicas.
#
# - tokens: Son símbolos complejos que requieren expresiones regulares.
#           Ej: AND, OR, NOT, BOOLEAN.
#
# - literals: Son caracteres simples que se reconocen directamente
#             sin necesidad de expresión regular.
#             Ej: '(', ')'.
#
# - Las funciones t_... definen las reglas de reconocimiento para
#   cada token.
#
# - El lexer transforma la entrada en una secuencia de tokens para
#   que el parser (parser.py) la pueda interpretar.
# -------------------------------------------------------------

tokens = (
    'BOOLEAN',
    'AND',
    'OR',
    'NOT',
    'LPAREN',
    'RPAREN',
    'NEWLINE',
)

literals = ['(', ')']

t_AND = r'AND'
t_OR = r'OR'
t_NOT = r'NOT'
t_BOOLEAN = r'TRUE|FALSE|1|0'  # Modificado para aceptar '1' y '0'

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t'

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(t):
    print(f"Caracter ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()