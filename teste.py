import csv
notas = [5.95, 9.72, 6.8, 5.4, 6.92, 6.85, 9.97, 6.42, 9.51, 7.9, 1.86, 8.9, 8.31, 9.47, 5.51, 3.87, 6.99, 4.35, 5.52, 1.58, 6.43, 7.21, 1.65, 6.43, 9.18, 6.75, 2.59, 9.08, 1.94, 3.7, 5.08, 8.27, 7.3, 5.06, 6.41, 8.23, 6.47, 9.93, 7.04, 9.51, 5.94, 8.16, 3.72, 1.2, 8.36, 9.75, 7.3, 8.22, 2.96, 4.36, 7.33]

with open("notas.csv","w") as TextodeNotas:
    for i in range(1,len(notas)):
        csv.writer(TextodeNotas,lineterminator="\n").writerow((f'Nota do aluno {i}',notas[i]))        
    