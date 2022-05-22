while True:
  peso = input("qual seu peso? ").replace(",",".")
  altura = input("qual sua altura? ").replace(",",".")

  try:
    Teste = float(peso)/2
    Teste = float(altura)/2
  except:
    print("Aceitamos apenas dígitos")
  else:
    peso=float(peso)
    altura=float(altura)
    break

imc  = altura*altura
imc_total = peso/imc

if imc_total <= 25:
  print(f"uau, você está no peso ideal: {str(imc_total)[:4]}")
else:
  print(f"nossa, você está um pouco acima do peso: {str(imc_total)[:4]}")