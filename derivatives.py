import sympy as sp

def calcular_derivada():
    # Solicitar a função do usuário
    f_x_str = input("Digite a função f(x): ").strip()

    try:
        # Definir a variável simbólica x e a função f(x)
        x = sp.symbols('x')
        f_x = sp.sympify(f_x_str)

        # Definir o valor de dx
        dx = sp.symbols('dx')

        # Calcular f(x+dx)
        f_x_plus_dx = f_x.subs(x, x + dx)

        # Calcular a diferença f(x+dx) - f(x)
        difference = f_x_plus_dx - f_x

        # Calcular a derivada f'(x) usando a definição
        derivative = difference / dx

        # Simplificar a expressão da derivada
        derivative_simplified = sp.simplify(derivative)

        # Calcular o limite conforme dx se aproxima de 0
        derivative_limit = sp.limit(derivative_simplified, dx, 0)

        # Imprimir os resultados
        print("\n" + "_" * 50)
        print("Função original: f(x) =", f_x)
        print("\nPasso 1: Calculando f(x+dx)\n  f(x+dx) =", f_x_plus_dx)
        print("\nPasso 2: Calculando a diferença f(x+dx) - f(x)\n  f(x+dx) - f(x) =", difference)
        print("\nPasso 3: Calculando a derivada f'(x) usando a definição\n  f'(x) =", derivative)
        print("\nPasso 4: Simplificando a expressão da derivada\n  f'(x) =", derivative_simplified)
        print("\nPasso 5: Calculando o limite conforme dx se aproxima de 0\n  f'(x) =", derivative_limit)

    except sp.SympifyError:
        print("Erro: Função inválida.")

# Loop para permitir que o usuário insira várias funções
while True:
    calcular_derivada()
    continuar = input("\nDeseja calcular a derivada de outra função? (s/n): ").lower()
    if continuar != 's':
        break
