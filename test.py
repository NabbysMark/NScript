import sys
from processor.lexer import Lexer
from processor.parser import Parser
from processor.interpreter import Interpreter

def main():
    if len(sys.argv) < 2:
        print("Usage: python test.py <script.n>")
        return
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        source = f.read()
    lexer = Lexer(source)
    parser = Parser(lexer)
    tree = parser.parse()
    interpreter = Interpreter()
    interpreter.interpret(tree)

if __name__ == "__main__":
    main()
