"""
x = ((17 to_the_power_of 39) to_the_power_of 11)

Now take every 33rd digit of x, starting with the first (most significant), and stick them together. That's your answer. 
"""


potencia = str((17**39)**11)
i = 0
salida = ""
while i < len(potencia):
    salida += potencia[i]
    i += 33
    
print salida
