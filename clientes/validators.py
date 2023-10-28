from rest_framework import serializers
import re
from validate_docbr import CPF 


 
def cpf_valido(numero_do_cpf):
        cpf = CPF()
        return cpf.validate(numero_do_cpf)

    
def nome_valido(nome):
        return nome.isalpha()

# def rg_valido(rg):
#     if rg == 9:
#         return rg
    
def celular_valido(numero_celular):
    """Verifica se o celular é válido (11 98210-1934)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9{4}]'
    resposta = re.findall(modelo, numero_celular)
    return resposta


    # def validate_celular(self, celular):
    #     if celular < 11:
    #         raise serializers.ValidationError("O celular deve ter 11 digitos")
    #     return celular
    