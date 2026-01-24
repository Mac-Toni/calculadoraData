from datetime import datetime, timedelta

def mostrar_menu():
    print("\n--- 📅 Menu da Calculadora ---")
    print("1. Diferença entre hoje e uma data")
    print("2. Somar dias a uma data")
    print("3. Sair")
    return input("Escolha uma opção: ")

def calcular():
    while True:
        opcao = mostrar_menu()
        
        if opcao == '1':
            data_str = input("Digite a data futura (dd/mm/aaaa): ")
            try:
                data_alvo = datetime.strptime(data_str, "%d/%m/%Y")
                hoje = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                diferenca = (data_alvo - hoje).days
                print(f"👉 Diferença: {diferenca} dias.")
            except ValueError:
                print("❌ Formato inválido! Use dd/mm/aaaa.")

        elif opcao == '2':
            dias = int(input("Quantos dias quer somar? "))
            hoje = datetime.now()
            nova_data = hoje + timedelta(days=dias)
            print(f"👉 Daqui a {dias} dias será: {nova_data.strftime('%d/%m/%Y')}")

        elif opcao == '3':
            print("Até logo! 👋")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    calcular()