from datetime import datetime
import database

def get_date() -> str:
    now = datetime.now()
    date = now.strftime("%d%m%Y")
    return date

def calculate_monthly_spending() -> list[float]:
    payAmount = float(input("Enter the amount for your paycheck: "))
    NEEDS = 0.50
    WANTS = 0.30
    SAVINGS = 0.20

    final_n = payAmount * NEEDS
    final_w = payAmount * WANTS 
    final_s = payAmount * SAVINGS
    
    print(f"Your pay is: {payAmount}")

    return [final_n, final_w, final_s]

def menu():
    isRunning = True
    print("1. List all records\n2. New Input\n3. Update Record\n4. Delete Record\n5. DisplayVisualization\n6. Quit")

    while isRunning:
        userOption = int(input("What would you like to do? "))
        match userOption:
            case 1:
                database.list_all_records()
                break
            case 2:
                database.insert_data()
                break
            case 3:
                print("Update record")
                break
            case 4: 
                print("Delete record")
                break
            case 5:
                print("Display visualization")
                break
            case 6:
                print("Quit")
                isRunning = False
                break;
            case _:
                print("Please choose an option!")

def main():
    print("Welcome to your personal financial planner!")
    menu()

if __name__ == "__main__":
    main()
