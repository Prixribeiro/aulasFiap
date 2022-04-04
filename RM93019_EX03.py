'''3 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.

Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte padrão:

VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.'''

aluno = 50
nota_aluno_impar = 0
nota_aluno_par = 0

for aluno in range(1,50,2):
        print("####VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES####")
        nota_impar= float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(aluno)))
        nota_aluno_impar = nota_aluno_impar + nota_impar



for aluno in range(2,51,2):
        print("****VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES****")
        nota_par= float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(aluno)))
        nota_aluno_par = nota_aluno_par + nota_par

media_aluno_impar = nota_aluno_impar / 25
media_aluno_par = nota_aluno_par / 25

print("A média de notas dos alunos ímpares é {:.2f}".format(media_aluno_impar))
print("A média de notas dos alunos pares é {:.2f}".format(media_aluno_par))

if media_aluno_impar > media_aluno_par:
    print("OS ALUNOS ÍMPARES TIVERAM A MAIOR MÉDIA DA SALA COM {:.2f}".format(media_aluno_impar))
else:
    print("OS ALUNOS PARES TIVERAM A MAIOR MÉDIA DA SALA COM {:.2f}".format(media_aluno_par))