import tkinter as tk

def validar_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def adicionar():
    resultado.delete(0, tk.END)
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    if validar_numero(num1) and validar_numero(num2):
        resultado.insert(0, float(num1) + float(num2))
    else:
        resultado.insert(0, "Erro, entrada inválida")

def subtrair():
    resultado.delete(0, tk.END)
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    if validar_numero(num1) and validar_numero(num2):
        resultado.insert(0, float(num1) - float(num2))
    else:
        resultado.insert(0, "Erro, entrada inválida")

def multiplicar():
    resultado.delete(0, tk.END)
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    if validar_numero(num1) and validar_numero(num2):
        resultado.insert(0, float(num1) * float(num2))
    else:
        resultado.insert(0, "Erro, entrada inválida")

def dividir():
    resultado.delete(0, tk.END)
    num1 = entry_num1.get()
    num2 = entry_num2.get()
    if validar_numero(num1) and validar_numero(num2):
        num2_float = float(num2)
        if num2_float != 0:
            resultado.insert(0, float(num1) / num2_float)
        else:
            resultado.insert(0, "Erro, Divisão por 0")
    else:
        resultado.insert(0, "Erro, entrada inválida")

# Criando a janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.configure(bg='lightblue')  # Cor de fundo da janela

# Entradas
entry_num1 = tk.Entry(janela, bg='white', fg='black')
entry_num1.grid(row=0, column=1)
entry_num2 = tk.Entry(janela, bg='white', fg='black')
entry_num2.grid(row=1, column=1)

# Labels
tk.Label(janela, text="Número 1:", bg='lightblue', fg='black').grid(row=0, column=0)
tk.Label(janela, text="Número 2:", bg='lightblue', fg='black').grid(row=1, column=0)

# Botões
tk.Button(janela, text="Adicionar", command=adicionar, bg='green', fg='white').grid(row=2, column=0)
tk.Button(janela, text="Subtrair", command=subtrair, bg='orange', fg='white').grid(row=2, column=1)
tk.Button(janela, text="Multiplicar", command=multiplicar, bg='blue', fg='white').grid(row=3, column=0)
tk.Button(janela, text="Dividir", command=dividir, bg='red', fg='white').grid(row=3, column=1)

# Resultado
resultado = tk.Entry(janela, bg='white', fg='black')
resultado.grid(row=4, column=0, columnspan=2)

tk.Label(janela, text="Resultado:", bg='lightblue', fg='black').grid(row=4, column=2)

# Inicia o loop da interface
janela.mainloop()