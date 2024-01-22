def comprova_signe(num: int)->int:
  """Aquesta funció sereix per veure si el numero es positiu,negtiu o es 0."""
  resultat = 0 #Iniciem la variable amb 0.

  if(num>0): #Provem si el numero es mes grant que 0
     resultat = 1

  elif(num==0): #Provem si el numero es igual a 0
      resultat = 0
  else: #Provem si el numero es mes petit que 0
     resultat = -1

  return resultat
