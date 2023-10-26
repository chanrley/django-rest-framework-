from rest_framework import serializers


def cpf_valido(numero_do_cpf):
        return len(numero_do_cpf) == 11
    
def nome_valido(nome):
        return nome.isalpha()

def rg_valido(rg):
    if rg == 9:
        return rg
    


    # def validate_celular(self, celular):
    #     if celular < 11:
    #         raise serializers.ValidationError("O celular deve ter 11 digitos")
    #     return celular
    