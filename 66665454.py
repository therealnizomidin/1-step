class SodaMachine:
    def __init__(self):
        self.sodas = {
            'Cola': 1.50,
            'Root Beer': 1.75,
            'Lemonade': 1.25,
            'Orange Soda': 1.50
        }
        self.coins = {
            'Penny': 0.01,
            'Nickel': 0.05,
            'Dime': 0.10,
            'Quarter': 0.25
        }

    def display_menu(self):
        print("Available sodas:")
        for soda, price in self.sodas.items():
            print(f"{soda}: ${price:.2f}")

    def get_soda_choice(self):
        choice = input("Enter the name of the soda you want: ").strip()
        if choice in self.sodas:
            return choice
        else:
            print("Invalid choice. Please select again.")
            return self.get_soda_choice()

    def get_payment(self):
        total = 0
        print("Insert coins. Type 'done' when finished.")
        while True:
            coin = input("Enter coin (Penny, Nickel, Dime, Quarter): ").strip().capitalize()
            if coin == 'Done':
                break
            elif coin in self.coins:
                total += self.coins[coin]
            else:
                print("Invalid coin. Please try again.")
        return total

    def process_transaction(self, soda, payment):
        price = self.sodas[soda]
        if payment >= price:
            change = payment - price
            print(f"Dispensing {soda}.")
            if change > 0:
                print(f"Returning change: ${change:.2f}")
            return True
        else:
            print(f"Insufficient payment. ${price - payment:.2f} more needed.")
            return False

    def run(self):
        while True:
            self.display_menu()
            soda_choice = self.get_soda_choice()
            payment = self.get_payment()
            if self.process_transaction(soda_choice, payment):
                break

if __name__ == "__main__":
    machine = SodaMachine()
    machine.run()
