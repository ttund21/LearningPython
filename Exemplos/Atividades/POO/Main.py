"""
Questão 1

Escreva uma classe cujos objetos representam alunos matriculados em uma disciplina. Cada objeto
dessa classe deve guardar os seguintes dados do aluno: matrícula, nome, 2 notas de prova.
Escreva os seguintes métodos para esta classe:

Media 6 para ser aprovado

media | calcula a média final do aluno.
final | calcula quanto o aluno precisa para a prova final (retorna zero se ele não for para a final)
"""

class Aluno:
    
    def __init__(self, matricula, nome, nota1, nota2):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        return (self.nota1 + self.nota2) / 2

    @staticmethod
    def final(media):
        pass



a1 = Aluno(220201, "João", 7.5, 5)

print(f"Nome: {a1.nome}\nMatricula: {a1.matricula}\n1ª Nota: {a1.nota1}\n2ª Nota: {a1.nota2}")
print(f"Media geral: {a1.media()}")
print(a1.final())