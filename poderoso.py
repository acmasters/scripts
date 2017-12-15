restaurantes = ['Habibs', 'Barbacoa','Palacio das pizzas','Ragazzo', 'McDonalds','Burger King']

for restaurante in restaurantes:
	if 'Barbacoa' in restaurante:  
		print("O restaurante " + restaurante + " eh muito caro!!!")
	elif 'Habibs' in restaurante:
		print("O restaurante " + restaurante + " serve comida arabe") 
	elif 'McDonalds' in restaurante:
		print("O restaurante " + restaurante + " serve fast food") 
	else:
		print("O restaurante " + restaurante + " serve rodizio de pizzas")	
              
              
