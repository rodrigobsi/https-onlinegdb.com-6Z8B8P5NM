'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
nota = 100
presenca = 100

if nota < 70 or presenca < 70:
    print("Você não passou")
    if nota < 70:
        print("tente melhorar sua nota")
    if presenca < 70:
        print("você deveria ter ido mais as aulas")
else:
    print("você passou")
    if nota == 100 and presenca == 100:
        print("Aprovado com louvor.")
    elif (nota < 90 and nota > 80) and (presenca <90 and presenca > 80):
        print("Bom trabalho")
        if nota < 75:
            print("Quase que fica reprovado por nota. Tente se dedicar mais as suas notas.")
        if presenca < 75:
            print("Quase que fica reprovado por setença. Tente Comparecer mais às aulas.")