import sys
import os
import webbrowser
import traceback
import shutil
from processor.lexer import Lexer
from processor.parser import Parser
from processor.interpreter import Interpreter

VERSION = "1.2.0"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, "_MEIPASS", None)
    if base_path is None:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def ensure_default_libs():
    local_libs_dir = os.path.join(os.environ.get("LOCALAPPDATA", ""), "nscript_libs")
    target_libs_dir = os.path.join(local_libs_dir, "defaultlibs")
    default_libs_dir = resource_path("defaultlibs")
    print(f"default_libs_dir resolved to: {default_libs_dir}")
    print(f"target_libs_dir resolved to: {target_libs_dir}")
    if not os.path.exists(target_libs_dir):
        os.makedirs(target_libs_dir, exist_ok=True)
    if not os.path.exists(default_libs_dir):
        print(f"[WARNING] Default libs folder not found: {default_libs_dir}")
        return
    for root, dirs, files in os.walk(default_libs_dir):
        rel_path = os.path.relpath(root, default_libs_dir)
        target_dir = os.path.join(target_libs_dir, rel_path) if rel_path != "." else target_libs_dir
        if not os.path.exists(target_dir):
            os.makedirs(target_dir, exist_ok=True)
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(target_dir, file)
            if not os.path.exists(dst_file):
                shutil.copyfile(src_file, dst_file)

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
    ensure_default_libs()
    if len(sys.argv) == 2 and sys.argv[1] in ("-v", "--version"):
        print(f"NScript version {VERSION}")
        return
    if len(sys.argv) == 2 and sys.argv[1] in ("--docs", "-d"):
        docs_path = resource_path("docs.html")
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