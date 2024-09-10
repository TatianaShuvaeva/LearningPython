def hochzaehlen(x): 
	return x + 1
   
def herunterzaehlen(x):  
	return x - 1
	
def rechnen(funktion, x):
    result = funktion(x)    
    return result
	
i = 3
print(f"vorher: {i} nachher: {rechnen(hochzaehlen, i)}")
print(f"vorher: {i} nachher: {rechnen(herunterzaehlen, i)}")