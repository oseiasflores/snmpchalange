import requests
import json

# Valores Globais para uso json

login = """
{
    "data": {
    "username":'admin',
    "password":'in.lock.net2040'
    }
}
"""
headers = {
  'Content-Type': 'application/json'
}

#URL BASE
urlbase ='http://192.168.10.1:80'

def verify_snmp():
    # Request para realizar login
    response = requests.post(urlbase + '/cgi-bin/api/v3/system/login', data=login, headers=headers)
    sresponse = str(response)

    # Verificar se logou com sucesso
    if sresponse == '<Response [200]>':
        print("\nLOGIN EFETUADO COM SUCESSO!!!")
        state = True
    else:
        print("Falha no Login: {}".format(response))
        state = False

    if state == True:
        # Armazenar json response
        auth_token = response.json()

        # Filtrando apenas o value token e ajustando o token para uso no novo headers
        toke = auth_token.get('data')
        toke = toke.get('Token')
        tokef = 'Token ' + toke

        # Request para ver se o serviço SNMP esta up/down
        # Este valor eu preferi separar ele em cada função para caso de timeout no login
        # Seja possivel sempre utilizr o ultimo gerado de acordo com cada opção

        services = {
            'Authorization': tokef
        }

        # Forma que eu encontrei para filtrar todo o dict recebido e verificar apenas o estado do snmp
        response = requests.get(urlbase + '/cgi-bin/api/v3/service/snmp/status', headers=services)
        snmp_state = response.json()
        snmp_state = snmp_state.get('data')
        snmp_state = snmp_state.get('snmp')

        if snmp_state == True:
            print("Serviço SNMP Ativo!")
            print("Estado do serviço SNMP: {}".format(snmp_state))
        else:
            print("Serviço SNMP Inativo!")
            print("Estado do serviço SNMP: {}".format(snmp_state))
    else:
        print("Falha ao tentar verificar o estado do Serviço.\n")
        print("Tente novamente..\n")
        #menu()

def enable_snmp():
    # Request para realizar login
    response = requests.post(urlbase + '/cgi-bin/api/v3/system/login', data=login, headers=headers)
    sresponse = str(response)

    # Verificar se logou com sucesso
    if sresponse == '<Response [200]>':
        print("\nLOGIN EFETUADO COM SUCESSO!!!")
        state = True
    else:
        print("Falha no Login: {}".format(response))
        state = False

    if state == True:
        # Armazenar json response
        auth_token = response.json()

        # Filtrando apenas o value token e ajustando o token para uso no novo headers
        toke = auth_token.get('data')
        toke = toke.get('Token')
        tokef = 'Token ' + toke

        # Request para ver se o serviço SNMP esta up/down
        # Este valor eu preferi separar ele em cada função para caso de timeout no login
        # Seja possivel sempre utilizr o ultimo gerado de acordo com cada opção

        services = {
            'Content-Type': 'application/json',
            'Authorization': tokef
        }
        values = """
            {
                "data": {
                    "snmp": true,
                    "community": "public",
                    "port": "161",
                    "location": "Right here, Right now",
                    "contact": "example@example.org",
                    "name": "Wireless Repeater",
                    "wan_access": true
                }
            }
        """

        # Retorna um response 204 sem content
        response = requests.put(urlbase + '/cgi-bin/api/v3/service/snmp', data=values, headers=services)
        response = str(response)

        if response == '<Response [204]>':
            print("\nServiço SNMP Ativado!")
            print("\nSalvando configurações em Flash!")
            
            # Retorna um response 204 sem content
            response = requests.post(urlbase + '/cgi-bin/api/v3/system/apply', headers=services)
            config_state = response.json()
            #print(config_state)
            config_state = config_state.get('data')
            config_state = config_state.get('success')

            if config_state == True:
                print("\nGravado em Flash!")
            else:
                print("\nConfigurações não aplicadas...")
                print("Retornando ao menu de opções!\n")
        
        else:
            print("Serviço SNMP Inativo!")
            print("Falha ao tentar habilitar o  serviço.\n")
            print("Tente novamente..\n")
        
    else: 
        print("\nOcorreu um erro inesperado...")
        print("\nRetornando ao menu de opções!")

def disable_snmp():
    # Request para realizar login
    response = requests.post(urlbase + '/cgi-bin/api/v3/system/login', data=login, headers=headers)
    #print("Reposta de Login: {}".format(response))
    sresponse = str(response)

    # Verificar se logou com sucesso
    if sresponse == '<Response [200]>':
        print("\nLOGIN EFETUADO COM SUCESSO!!!")
        state = True
    else:
        print("Falha no Login: {}".format(response))
        state = False

    if state == True:
        # Armazenar json response
        auth_token = response.json()

        # Filtrando apenas o value token e ajustando o token para uso no novo headers
        toke = auth_token.get('data')
        toke = toke.get('Token')
        tokef = 'Token ' + toke

        # Request para ver se o serviço SNMP esta up/down
        # Este valor eu preferi separar ele em cada função para caso de timeout no login
        # Seja possivel sempre utilizr o ultimo gerado de acordo com cada opção

        services = {
            'Content-Type': 'application/json',
            'Authorization': tokef
        }
        values = """
            {
                "data": {
                    "snmp": false,
                    "community": "public",
                    "port": "161",
                    "location": "Right here, Right now",
                    "contact": "example@example.org",
                    "name": "Wireless Repeater",
                    "wan_access": true
                }
            }
        """

        # Retorna um response 204 sem content
        response = requests.put(urlbase + '/cgi-bin/api/v3/service/snmp', data=values, headers=services)
        response = str(response)

        if response == '<Response [204]>':
            print("\nServiço SNMP Desativado!")
            print("\nSalvando configurações em Flash!")
            
            # Retorna um response 204 sem content
            response = requests.post(urlbase + '/cgi-bin/api/v3/system/apply', headers=services)
            config_state = response.json()
            #print(config_state)
            config_state = config_state.get('data')
            config_state = config_state.get('success')

            if config_state == True:
                print("\nGravado em Flash!")
            else:
                print("\nConfigurações não aplicadas...")
                print("Retornando ao menu de opções!\n")
        
        else:
            print("Serviço SNMP ainda esta Ativo!")
            print("Falha ao tentar desabilitar o  serviço.\n")
            print("Tente novamente..\n")
        
    else: 
        print("\nOcorreu um erro inesperado...")
        print("\nRetornando ao menu de opções!")

def menu():
    while True:
        print("")
        print("Escolha uma opção:")
        print("Verificar se o Serviço SNMP esta ativo: 1")
        print("Habilitar o Serviço SNMP: 2")
        print("Desabilitar o Seviço SNMP: 3")
        print("Fechar o Programa: 4")
        option = input("Opção: ")

        if option == "1":
            verify_snmp()

        elif option == "2":
            enable_snmp()

        elif option == "3":
            disable_snmp()

        elif option == "4":
            print("\nPrograma encerrado.\n")
            break
        else:
            print("\nOpção Invalida!\n")
            print("\nDigite uma opção valida!\n")

print("\nPrograma para habilitar, desabilitar e verificar estado do Serviço SNMP.")
print("By: Oséias Flores\n")
menu()
