popPaisA = 80000
popPaisB = 200000
anos = 0

while not popPaisA == popPaisB:
    popPaisA = popPaisA + (popPaisA*0.03)
    popPaisB = popPaisB + (popPaisB * 0.015)
    anos +=1

print(anos)