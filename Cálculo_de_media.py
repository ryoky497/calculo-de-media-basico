nome = input("digite o nome do aluno: ")
materia = input("digite sua materia: ")
parcial = float(input("digite a nota da parcial: "))
bimestral = float(input("digite a nota da bimestral: "))
qualitativa = float(input("digite a qualitativa: "))
faltas = float(input("digite seu número de faltas: "))


mediadobimestre1 = float((parcial + bimestral + qualitativa)/3)

if mediadobimestre1 >=6 and faltas <= 25:
  print("aprovado")
  print("você passou de ano")
elif faltas > 25:
  print("você foi reprovado de forma imediata")
  print("nos vemos novamente proximo ano")
else:
  print("média insuficiente")
  print("nos vemos proxima semana na recuperação")
