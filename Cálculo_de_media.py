def resultado():
  resultado = float((parcial + bimestral + qualitativa)/3)
  return resultado

def notas():
  parcial = float(input("digite a nota da parcial: "))
  bimestral = float(input("digite a nota da bimestral: "))
  qualitativa = float(input("digite a qualitativa: "))
  faltas = float(input("digite seu número de faltas: "))
  return [parcial, bimestral, qualitativa, faltas]

while True:

  nome = input("digite o nome do aluno: ")
  materia = input("digite sua materia: ")
 
  notas2 = notas()
  if notas2[0] > 10 or notas2[1] > 10 or notas2[2] > 10:
    print("impossivel está nota existir")
    continue
  if notas2[0] < 0 or notas2[1] < 0 or notas2[2] < 0:
    print("impossivel está nota existir")
    continue

  if resultado() >= 6 and faltas <= 25:
    print("aprovado")
    print("você passou de ano")
  elif faltas > 25:
    print("ele foi reprovado de forma imediata")
    print("lembre de chama-lo pra recuperação")
  else:
    print("reprovado")
    print("nos vemos proxima semana na recuperação")
    
  pergunta = input("deseja continuar? ").capitalize()

  if pergunta == "Sim":
   continue
  elif pergunta == "Não":
    break
  else:
    print("opção inexistente")
