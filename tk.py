import tkinter as tk
from tkinter import messagebox

def calcular_digito_verificador(cpf_parcial):
    soma = 0
    multiplicador = len(cpf_parcial) + 1
    
    for digito in cpf_parcial:
        soma += int(digito) * multiplicador
        multiplicador -= 1

    resto_divisao = soma % 11
    if resto_divisao < 2: 
        return '0'
    else: 
        return str(11 - resto_divisao)

def verificar_cpf(cpf):
    cpf = cpf.replace(' ', '').replace('.', '').replace('-', '')

    if len(cpf) != 11 or not cpf.isdigit(): 
        return False
        
    cpf_parcial = cpf[:9]

    digito1 = calcular_digito_verificador(cpf_parcial) 
    cpf_parcial += digito1

    digito2 = calcular_digito_verificador(cpf_parcial) 
    cpf_calculado = cpf_parcial + digito2
        
    return cpf == cpf_calculado

def verificar_cpf_interface(): 
    cpf = entry_cpf.get()

    if verificar_cpf(cpf):
        messagebox.showinfo("Resultado", "CPF válido!")
    else:
        messagebox.showwarning("Resultado", "CPF inválido!")

# Configuração da interface gráfica

root = tk.Tk()
root.title("Verificador de CPF")

label_instrucao = tk.Label(root, text="Digite o CPF (apenas números):")
label_instrucao.pack()

entry_cpf = tk.Entry(root)
entry_cpf.pack()

button_verificar = tk.Button(root, text="Verificar", command=verificar_cpf_interface)
button_verificar.pack()

root.mainloop()
