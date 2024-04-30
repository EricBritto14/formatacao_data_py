from datetime import datetime, date
from http.client import HTTPException

# data_hoje = date.today()

# data_cad_str = input("Digite a data: ")
# data_cad = datetime.strptime(data_cad_str, '%d/%m/%Y')

# def validar_data(data_hoje, data_cad):
#     try:
#         print("O que ta vindo", data_hoje, data_cad)
#         # Convertendo data_hoje para datetime
#         data_hoje = datetime.combine(data_hoje, datetime.min.time())
#         print("Como fica: ", data_hoje)
        
#         if data_hoje >= data_cad:            
#             return data_hoje.strftime('%d/%m/%Y')
#         else:
#             return "Data menor que a data de cadastro, inválida!"
#     except Exception as e:
#         return str(e)


def validar_data(data_val):
    try:
        data_hoje = date.today()
        data_valF1 = datetime.strptime(data_val, '%d/%m/%Y').date()
        print("Data de hoje como tá: ", data_hoje)
        print("Data validada como tá: ", data_valF1)
        #data_valF = data_valF1.strftime('%d/%m/%Y')
        if data_valF1 >= data_hoje:
            return data_valF1.strftime('%d/%m/%Y')
        else:
            return "Data de validade menor que a data de hoje!"
    except Exception as e:
        str(e)

data_val = "11/04/2004"
print(validar_data(data_val))