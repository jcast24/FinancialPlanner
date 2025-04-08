def calculate_monthly_spending() -> list[float]:
    payAmount = float(input("Enter the amount for your paycheck: "))
    NECESSITIES = 0.50
    WANTS = 0.30
    SAVINGS = 0.20

    final_n = payAmount * NECESSITIES
    final_w = payAmount * WANTS 
    final_s = payAmount * SAVINGS
    return [final_n, final_w, final_s]

def menu():
    isRunning = True
    print("1. List all records\n2. New Input\n3. Update Record\n4. Delete Record\n5. Quit")

    while isRunning:
        userOption = int(input("What would you like to do? "))
        match userOption:
            case 1:
                print("List all records")
                break
            case 2:
                print("New input")
                break
            case 3:
                print("Update record")
                break
            case 4: 
                print("Delete record")
                break
            case 5:
                print("Quit")
                isRunning = False
                break;
            case _:
                print("Please choose an option!")

def main():
    print("Welcome to your personal financial planner!")
    # menu()

    result = calculate_monthly_spending()
    print(result)

if __name__ == "__main__":
    main()
