from datetime import datetime, timedelta

# Exemplo de lógica para data antiga
data_input = input("Digite a data (DD/MM/AAAA): ")
dias = int(input("Quantos dias deseja voltar? "))

data_objeto = datetime.strptime(data_input, "%d/%m/%Y")
# Subtraindo os dias para achar a data antiga
data_passada = data_objeto - timedelta(days=dias)

print(f"Há {dias} dias atrás, a data era: {data_passada.strftime('%d/%m/%Y')}")