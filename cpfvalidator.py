#dígito das regiões fiscais(definida pelo nono dígito dos CPF verificados)
region = {1:"DF, GO, MS, MT e TO",
            2:"AC, AM, AP, PA, RO e RR",
            3:"CE, MA e PI",
            4:"AL, PB, PE, RN",
            5:"BA e SE",
            6:"MG",
            7:"ES e RJ",
            8:"SP",
            9:"PR e SC",
            0:"RS"}
#função para conferir a veracidade dos dígitos verificadores
def dig(cpf):
    d1 = 0
    d2 = 0
    for x in range(10,1,-1):
        d1 += cpf[10-x]*x
    if(d1%11 <= 1):
        d1 = 0
    else:
        d1 = 11-(d1%11)

    for x in range(10,1,-1):
        d2 += cpf[11-x]*x
    if(d2%11 <= 1):
        d2 = 0
    else:
        d2 = 11-(d2%11)
    

    if(cpf[9:11] == [d1,d2]):
        print(f"CPF válido! Região Fiscal pertence ao(s) Estado(s):{region[cpf[8]]}")
    else:
        print("CPF inválido! Verifique se os dígitos estão corretos")

def read():
    cpf = list(input("Digite o CPF a ser consultado>>>"))
    cpf = [int(num) for num in cpf]
    return cpf

cpf = read()
while(len(cpf) != 11 or len(set(cpf)) == 1):
    print("CPF inválido! Verifique se os dígitos estão corretos")
    cpf = read()

dig(cpf)
