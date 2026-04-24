# bubble sort
tinggi = [150, 170, 155, 160, 145]
n = len(tinggi)
for i in range(n):
    for j in range(0, n-i-1):
        if tinggi[j] > tinggi[j+1]:
            tinggi[j], tinggi[j+1] = tinggi[j+1], tinggi[j]
print(f"Hasil Akhir: {tinggi}")
