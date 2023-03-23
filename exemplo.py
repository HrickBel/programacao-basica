import pandas as pd

notas = []
med = int()
somaP = int()
somaS = int()

data = pd.read_csv('/home/henrique/python/provaDoHead/exemplo1.csv')
for i in range(0,20):
	aluno = []
	for j in range(0,5):
		aluno.append(data.iat[i,j])
	notas.append(aluno)
for i in range(0,20):
	med = 0
	aluno = notas[i][0]
	for j in range(1,5):
		if i == j:
			somaP += int(notas[i-1][j])
		elif i+j == 4:
			somaS += int(notas[i][j])
		med += int(notas[i][j])
		estado ='aprovado' if (med/4) >= 5 else'reprovado'
	print(f'aluno:{notas[i][0]}\tmedia:{med/4}\testado:{estado}')
print(f'soma diagonal principal:{somaP}\tsoma diagonal secundaria:{somaS}')