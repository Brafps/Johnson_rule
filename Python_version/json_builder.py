import json

# Transformando a lista de cinco cachorros em um arquivo json
# Estruturando o arquivo
itens = [    
    {"Id": "1", 
     "Tempo de banho": 5, 
     "Tempo de tosa": 3
     },
    {"Id": "2", 
     "Tempo de banho": 4, 
     "Tempo de tosa": 6
     },
    {"Id": "3", 
     "Tempo de banho": 2, 
     "Tempo de tosa": 4
     },
    {"Id": "4", 
     "Tempo de banho": 9, 
     "Tempo de tosa": 2
     },
    {"Id": "5", 
     "Tempo de banho": 8, 
     "Tempo de tosa": 5
     },
    {"Id": "6", 
     "Tempo de banho": 6, 
     "Tempo de tosa": 2
     }    
]

# Criando o arquivo
file_name = "file_name"
path = "data/" + file_name
with open(path + '.json', 'w') as json_file:
    json.dump(itens, json_file, indent=2)