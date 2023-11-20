AGENDA = {}
AGENDA["carlos"] = {
  "tell":" 9999-4675",
  "email":" carlos@email.com",
  "endereco": "Av. 1",
}

AGENDA["joao"] = {
  "tell":" 9769-4675",
  "email":" joao@email.com",
  "endereco": "Av. 2",
}

def mostras_contastos():
  for contato in AGENDA:
    print("Nome: ", contato)
    print("Telefone",AGENDA[contato]['tell'])
    print("Email",AGENDA[contato]['email'])
    print("Endereço",AGENDA[contato]['endereco'])
    print('----------------------')
  
mostras_contastos()
