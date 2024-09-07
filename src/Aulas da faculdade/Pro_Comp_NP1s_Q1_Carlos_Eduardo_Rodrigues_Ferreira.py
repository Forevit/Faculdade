alunos = []

num_alunos = int(input("Digite o número de alunos: "))
for i in range(num_alunos):
    nomes = input("Digite o nome do Aluno:")
    curso = input("Digite o curso do Aluno:")
    disciplina = input("Digite a cadeira do Aluno: ")
    NotObj1 = float(input("Digite a Nota Objetiva da NP1: "))
    NotSubj1 = float(input("Digite a Nota Subjetiva da NP1:"))
    NotObj2 = float(input("Digite a nota Objetiva da NP2:"))
    NotSubj2 = float(input("Digite a nota Subjetiva da NP2:"))

    NP1 = (float(NotObj1) + float(NotSubj1)) / 2
    NP2 = (float(NotObj2) + float(NotSubj2)) / 2

    if NP1 <= 4:
        status_NP1 = "Aluno Reprovado"
    elif NP1 > 4 and NP1 < 7:
        status_NP1 = "Aluno em Recuperação"
    else:
        status_NP1 = "Aluno Aprovado"

    if NP2 <= 4:
        status_NP2 = "Aluno Reprovado"
    elif NP2 > 4 and NP2 < 7:
        status_NP2 = "Aluno em Recuperação"
    else:
        status_NP2 = "Aluno Aprovado"

    aluno = {
        "nome": nomes,
        "curso": curso,
        "disciplina": disciplina,
        "NP1": NP1,
        "status_NP1": status_NP1,
        "NP2": NP2,
        "status_NP2": status_NP2
    }
    alunos.append(aluno)

def calcular_media_final(NP1, NP2):
    return (NP1 + NP2) / 2

for aluno in alunos:
    print(f"Aluno: {aluno['nome']}")
    print(f"Curso: {aluno['curso']}")
    print(f"Disciplina: {aluno['disciplina']}")
    print(f"NP1: {aluno['NP1']}")
    print(f"NP2: {aluno['NP2']}")
    print(f"Status NP1: {aluno['status_NP1']}")
    print(f"Status NP2: {aluno['status_NP2']}")
    print(f"Media Final: {calcular_media_final(aluno['NP1'], aluno['NP2'])}")
    print("------------------------")