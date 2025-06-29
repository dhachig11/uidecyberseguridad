
import tkinter as tk
from tkinter import messagebox
import secrets
import string
import pyperclip

# Function to generate a secure password
def generate_password():
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_lowercase = lowercase_var.get()
    include_numbers = numbers_var.get()
    include_special = special_var.get()

    if not (include_uppercase or include_lowercase or include_numbers or include_special):
        messagebox.showwarning("Configuración inválida", "Debe seleccionar al menos un tipo de carácter.")
        return

    characters = ""
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    evaluate_password(password)

# Function to evaluate the strength of the password
def evaluate_password(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    strength = "Débil"
    if length >= 12 and has_upper and has_lower and has_digit and has_special:
        strength = "Fuerte"
    elif length >= 8 and ((has_upper and has_lower) or (has_digit and has_special)):
        strength = "Media"

    strength_label.config(text=f"Fortaleza: {strength}")

# Function to copy the password to the clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copiado", "La contraseña ha sido copiada al portapapeles.")
    else:
        messagebox.showwarning("Sin contraseña", "No hay ninguna contraseña para copiar.")

# Create the main window
root = tk.Tk()
root.title("Generador Seguro de Contraseñas")

# Create and place widgets
tk.Label(root, text="Longitud de la contraseña:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

uppercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Incluir mayúsculas", variable=uppercase_var).grid(row=1, column=0, padx=10, pady=5)

lowercase_var = tk.BooleanVar()
tk.Checkbutton(root, text="Incluir minúsculas", variable=lowercase_var).grid(row=1, column=1, padx=10, pady=5)

numbers_var = tk.BooleanVar()
tk.Checkbutton(root, text="Incluir números", variable=numbers_var).grid(row=2, column=0, padx=10, pady=5)

special_var = tk.BooleanVar()
tk.Checkbutton(root, text="Incluir caracteres especiales", variable=special_var).grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Generar contraseña", command=generate_password).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Contraseña generada:").grid(row=4, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, width=40)
password_entry.grid(row=4, column=1, padx=10, pady=10)

tk.Button(root, text="Copiar al portapapeles", command=copy_to_clipboard).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

strength_label = tk.Label(root, text="Fortaleza: ")
strength_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
