import sys
import os
import webbrowser
import traceback
from nscript.lexer import Lexer
from nscript.parser import Parser
from nscript.interpreter import Interpreter

VERSION = "1.1.0"

def handle_nscript_error(e, script_file=None, playground=False):
    print("\n--- NacoScript Error ---")
    print(f"Error: {e}")
    tb = getattr(e, "__traceback__", None)
    if tb and not playground:
        stack = traceback.extract_tb(tb)
        shown = False
        for frame in stack:
            if frame.filename.endswith(".n") or (script_file and os.path.abspath(frame.filename) == os.path.abspath(script_file)):
                print(f'  File "{os.path.basename(frame.filename)}", line {frame.lineno}')
                print(f'    {frame.line}')
                shown = True
        if not shown and script_file:
            print(f'  In script: {os.path.basename(script_file)}')
    elif playground:
        print("  (Playground mode: error in your code)")
    print("-----------------------\n")

def main():
    if len(sys.argv) == 2 and sys.argv[1] in ("-v", "--version"):
        print(f"NScript version {VERSION}")
        return
    if len(sys.argv) == 2 and sys.argv[1] in ("--docs", "-d"):
        docs_path = os.path.join(os.path.dirname(__file__), "docs.html")
        if os.path.exists(docs_path):
            webbrowser.open(f"file://{os.path.abspath(docs_path)}")
            print("Opened documentation in your default browser.")
        else:
            print("Documentation file 'docs.html' not found.")
        return
    if len(sys.argv) == 2 and sys.argv[1].lower().endswith('.n'):
        filename = sys.argv[1]
        try:
            with open(filename, "r", encoding="utf-8") as f:
                code = f.read()
            lexer = Lexer(code)
            parser = Parser(lexer)
            tree = parser.parse()
            interpreter = Interpreter()
            interpreter.interpret(tree)
        except Exception as e:
            handle_nscript_error(e, script_file=filename)
    else:
        print("NScript Interactive Console (type 'exit' to quit)")
        interpreter = Interpreter()
        while True:
            try:
                line = input(">>> ")
                if line.strip().lower() == "exit":
                    break
                lexer = Lexer(line)
                parser = Parser(lexer)
                tree = parser.parse()
                interpreter.interpret(tree)
            except Exception as e:
                handle_nscript_error(e, playground=True)

if __name__ == "__main__":
    main()