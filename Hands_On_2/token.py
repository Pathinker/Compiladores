import re
import sys

# Asegurar codificación UTF-8 (especialmente para Windows)
sys.stdout.reconfigure(encoding='utf-8')

# Definición de patrones de tokens
token_specification = [
    ('COMMENT_MULTI', r'/\*[\s\S]*?\*/'),                    # Comentario multilínea
    ('COMMENT_SINGLE', r'//.*'),                             # Comentario una línea
    ('STRING',       r'"([^"\\]|\\.)*"'),                    # Cadenas de texto
    ('KEYWORD',      r'\b(?:int|return|char|float|if|else)\b'),  # Palabras clave
    ('IDENTIFIER',   r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),         # Identificadores
    ('NUMBER',       r'\b\d+(\.\d+)?\b'),                    # Números enteros y flotantes
    ('OPERATOR',     r'==|!=|<=|>=|&&|\|\||[+\-*/=%<>]'),    # Operadores
    ('DELIMITER',    r'[;,()[\]{}]'),                        # Delimitadores
    ('SKIP',         r'[ \t]+'),                             # Espacios y tabulaciones
    ('NEWLINE',      r'\n'),                                 # Saltos de línea
    ('UNKNOWN',      r'.'),                                  # Cualquier otro carácter
]

# Expresión regular combinada
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

def tokenize(code):
    """Función que analiza el código y cuenta los tokens."""
    counters = {
        'KEYWORD': 0,
        'IDENTIFIER': 0,
        'NUMBER': 0,
        'OPERATOR': 0,
        'DELIMITER': 0
    }

    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind in ('SKIP', 'COMMENT_SINGLE', 'COMMENT_MULTI', 'NEWLINE'):
            continue  # Ignoramos espacios, comentarios y saltos de línea
        elif kind == 'KEYWORD':
            counters['KEYWORD'] += 1
        elif kind == 'IDENTIFIER':
            counters['IDENTIFIER'] += 1
        elif kind == 'NUMBER':
            counters['NUMBER'] += 1
        elif kind == 'OPERATOR':
            counters['OPERATOR'] += 1
        elif kind == 'DELIMITER':
            counters['DELIMITER'] += 1
        # Opcional: Si quieres ver cada token identificado
        # print(f"{kind}: {value}")

    return counters

if __name__ == '__main__':
    # Variable de texto con el código fuente
    codigo_fuente = """
    int main() {
        // Comentario de una línea
        /* Comentario
           de varias líneas */
        int a = 5;
        float b = 3.14;
        if (a > 0) {
            a = a + 1;
        } else {
            b = b - 1.0;
        }
        return 0;
    }
    """

    print("Analizando el siguiente código:")
    print(codigo_fuente)

    resultado = tokenize(codigo_fuente)

    print("\nResumen del análisis léxico:")
    for token_type, count in resultado.items():
        print(f"{token_type}: {count}")