from django.test import TestCase
nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
email = input("Digite seu E-mail: ")

emailInvalido = 0

if email.find("@") == 0 or email.find("@") == len(email) -1:
    print("E-mail invalido")
    emailInvalido = 1
