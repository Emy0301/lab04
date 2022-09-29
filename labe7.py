def computegrade(grade):
    if(grade >= 0.9 and grade <= 1.0):
        grade = "Sobresaliente"
    elif(grade >= 0.8 and grade <0.9):
        grade = "Notable"
    elif(grade >= 0.7 and grade <0.8):
        grade = "Bien"
    elif (grade >= 0.6 and grade <0.7):
        grade = "Suficiente"
    elif (grade >= 0 and grade <0.6):
        grade = "Insuficiente"
    else:
        grade = "Puntuación incorrecta"
    return grade

try:
    score = float (input("Ingrese la calificación (0.01 - 1.00):"))
    grade = computegrade (score)
    print (grade)

except:
    print("Puntuación incorrecta")


    
