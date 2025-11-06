from lexer import tokenizar
from parser_expr import ParserExpr
from symbols import TS, lookup
from ast_graphviz import graph_ast
import os

def eval_ast(node):
    if node is None:
        raise Exception("AST incompleto: falta un operando.")

    if node.op == "id":
        v = lookup(node.value)
        print(f"id({node.value}) = {v}")
        return v
    if node.op == "num":
        print(f"num({node.value}) = {node.value}")
        return node.value

    left = eval_ast(node.left)
    right = eval_ast(node.right)

    if node.op == "*":
        res = left * right
        print(f"mul({left},{right}) = {res}")
        return res
    if node.op == "/":
        if right == 0:
            raise ZeroDivisionError("División por cero no permitida.")
        res = left / right
        print(f"div({left},{right}) = {res}")
        return res
    if node.op == "+":
        res = left + right
        print(f"suma({left},{right}) = {res}")
        return res
    if node.op == "-":
        res = left - right
        print(f"resta({left},{right}) = {res}")
        return res


def main():
    print("=== Analizador Aritmético (EDTS) ===")
    print("Escriba 'exit' para terminar.\n")

    while True:
        entrada = input("Ingrese expresión: ").strip()
        if entrada.lower() == "exit":
            print("Saliendo... ✅")
            break

        if entrada == "":
            continue

        try:
            tokens = tokenizar(entrada)
            parser = ParserExpr(tokens)
            ast = parser.parse()

            if ast is None:
                raise Exception("Expresión incompleta o inválida.")

            print("\nÁrbol Sintáctico Decorado (AST):")
            ast.print()

            img = graph_ast(ast)
            print(f"\n✅ AST gráfico generado: {img}")

            try:
                os.startfile(img)  # Abrir ventana con el AST
            except:
                print("⚠ No se pudo abrir la imagen automáticamente.")

            print("\nTraducción Dirigida:")
            try:
                resultado = eval_ast(ast)
            except ZeroDivisionError as zde:
                print(f"❌ Error: {zde}\n")
                continue

            print("\nTabla de Símbolos:")
            if not TS:
                print("(vacía)")
            else:
                for k, v in TS.items():
                    print(f"{k} : NUM = {v}")

            print(f"\n➡ Resultado final: {resultado}\n")

        except Exception as e:
            print(f"❌ Error: {e}\n")


if __name__ == "__main__":
    main()
