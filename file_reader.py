file_path = "/home/cedugenio/python/testes/teste.txt"

with open(file_path) as file_object:
     lines = file_object.readlines()

for line in lines:
    for 'Architecture' in line:
        line.replace('Architecture','Arquitetura')       
    print(len(line.rstrip())) 
