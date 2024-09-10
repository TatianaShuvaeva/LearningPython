def hallo(name="Python") -> str:    
	def gruss():        
		return " gruss"    
	def willkommen():        
		return " willkommen"   
		
	if name == "Python":        
		return name + gruss()    
	else:        
		return name + willkommen()
		
p = hallo()

print(p)
p = hallo("Java")
print(p)