import datetime


class Operation:
    def __init__(self):
        self.shopping_basket = {"Jeans": 20,
                                "Shirts": 10,
                                "T-Shirts": 20,
                                "Shoes": 15
                                }
        self.shopping_history = {}
        self.gross_total = 0
        self.total_discount = 0
        self.net_total = 0

    def main_menu(self):
        touch = input('Press Any Key To Return To Main Menu: ')
        self.menu()

    def menu(self):
        print("""
    ----- GBC Shopping Cart -----
            1: Add Items
            2: Delete Items
            3: View Cart
            4: Checkout
            5: EXIT""")

        choice = int(input("\nPlease Select An Option: "))

        while not 1 <= choice <= 5:
            choice = int(input("\nPlease Select An Appropriate Response: "))

        if choice == 1:
            self.add_items()
            self.main_menu()
        elif choice == 2:
            self.delete_item()
        elif choice == 3:
            self.view_cart()
        elif choice == 4:
            self.checkout()
        elif choice == 5:
            exit(0)

    def add_items(self):
        print('\n' + """Please Select:
         1 - Jeans : $20
         2 - Shirts : $10
         3 - T-Shirts : $20
         4 - Shoes : $15
         5 - RETURN TO MAIN MENU""")

        add_to_cart = int(input("\nPlease Select An Option: "))
        while not 1 <= add_to_cart <= 5:
            add_to_cart = int(input("\nPlease Enter A Valid Option: "))

        if add_to_cart == 1:
            quantity = int(input("Enter Quantity: "))
            if not self.shopping_history.get('Jeans'):
                self.shopping_history['Jeans'] = {'Barcode': 1, 'Quantity': int(quantity),
                                                  'Total': int(quantity) * self.shopping_basket['Jeans']}
                self.gross_total += self.shopping_history['Jeans']['Total']
            else:
                self.shopping_history['Jeans']['Quantity'] += int(quantity)
                self.shopping_history['Jeans']['Total'] += (int(quantity) * self.shopping_basket['Jeans'])
                self.gross_total += self.shopping_history['Jeans']['Total']
        elif add_to_cart == 2:
            quantity = int(input("Enter Quantity: "))
            if not self.shopping_history.get('Shirts'):
                self.shopping_history['Shirts'] = {'Barcode': 2, 'Quantity': int(quantity),
                                                   'Total': int(quantity) * self.shopping_basket['Shirts']}
                self.gross_total += self.shopping_history['Shirts']['Total']
            else:
                self.shopping_history['Shirts']['Quantity'] += int(quantity)
                self.shopping_history['Shirts']['Total'] += (int(quantity) * self.shopping_basket['Shirts'])
                self.gross_total += self.shopping_history['Shirts']['Total']
        elif add_to_cart == 3:
            quantity = int(input("Enter Quantity: "))
            if not self.shopping_history.get('T-Shirts'):
                self.shopping_history['T-Shirts'] = {'Barcode': 3, 'Quantity': int(quantity),
                                                     'Total': int(quantity) * self.shopping_basket['T-Shirts']}
                self.gross_total += self.shopping_history['T-Shirts']['Total']
            else:
                self.shopping_history['T-Shirts']['Quantity'] += int(quantity)
                self.shopping_history['T-Shirts']['Total'] += (int(quantity) * self.shopping_basket['T-Shirts'])
                self.gross_total += self.shopping_history['T-Shirts']['Total']
        elif add_to_cart == 4:
            quantity = int(input("Enter Quantity: "))
            if not self.shopping_history.get('Shoes'):
                self.shopping_history['Shoes'] = {'Barcode': 4, 'Quantity': int(quantity),
                                                  'Total': int(quantity) * self.shopping_basket['Shoes']}
                self.gross_total += self.shopping_history['Shoes']['Total']
            else:
                self.shopping_history['Shoes']['Quantity'] += int(quantity)
                self.shopping_history['Shoes']['Total'] += (int(quantity) * self.shopping_basket['Shoes'])
                self.gross_total += self.shopping_history['Shoes']['Total']
        elif add_to_cart == 5:
            self.menu()

        print("Item Successfully Added.")

        self.discount()

    def delete_item(self):
        if self.shopping_history:
            for item in sorted(self.shopping_history):
                print("\nBarcode: " + str(self.shopping_history[item]['Barcode']))
                print("Item: " + item)
                print("Quantity: " + str(self.shopping_history[item]['Quantity']))
                print("Total Amount: " + str(self.shopping_history[item]['Total']))

            removed_item = int(input("\nPlease Enter BARCODE Of Item You Want To Remove or 0 To Return To MAIN MENU: "))
            for item in list(self.shopping_history):
                if removed_item == self.shopping_history[item]['Barcode']:
                    self.gross_total -= self.shopping_history[item]['Total']
                    del self.shopping_history[item]
                    print('{} - Successfully Removed From The List.'.format(item))

                    self.discount()

                    choice = int(input("\nPress 1 To Delete Again or 2 For Main Menu: "))
                    while choice:
                        if choice == 1:
                            self.delete_item()
                        elif choice == 2:
                            self.menu()
                        else:
                            choice = int(input("\nPlease Enter A Valid Input. Press 1 or 2: "))

                elif removed_item == 0:
                    self.menu()

                else:
                    if len(item) != len(self.shopping_history):
                        continue
                    print("Item Not Found.\n")
                    choice = int(input("Press 1 To Try Again or 2 For Main Menu: "))
                    while choice > 0:
                        if choice == 1:
                            self.delete_item()
                        elif choice == 2:
                            self.menu()
                        else:
                            choice = int(input("\nPlease Enter A Valid Input. Press 1 or 2: "))

        else:
            print("\nYour Cart Is Empty.")
            choice = int(input("Press 1 To Add Items or 2 For Main Menu: "))
            while choice:
                if choice == 1:
                    self.add_items()
                elif choice == 2:
                    self.menu()
                else:
                    choice = int(input("\nPlease Enter A Valid Input. Press 1 or 2: "))

    def view_cart(self):
        if self.shopping_history:
            for item in self.shopping_history:
                print("\nBarcode: " + str(self.shopping_history[item]['Barcode']))
                print("Item: " + item)
                print("Quantity: " + str(self.shopping_history[item]['Quantity']))
                print("Total Amount: " + str(self.shopping_history[item]['Total']))
            print("\nGross Total:    " + str(self.gross_total))
            print("Total Discount: " + str(self.total_discount))
            print("Net Total:      " + str(self.net_total))
            view = int(input("\nPress 1 To Checkout Or 2 To Return To The Main Menu: "))
            while view:
                if view == 1:
                    self.checkout()
                elif view == 2:
                    self.menu()
                else:
                    view = int(input("Please Enter A Valid Input 1 or 2: "))

        else:
            print("Your Cart Is Empty.")
            view = input("\nPress Any Key To Return To The Main Menu: ")
            if view:
                self.menu()

    def checkout(self):
        now = datetime.datetime.now()
        if self.shopping_history:
            file = open('Receipt.txt', 'w+')
            file.write("----- GBC Online Shopping -----")
            file.write("\n" + now.strftime("\t%Y-%m-%d\t   %H:%M:%S\t"))
            for item in self.shopping_history:
                file.write("\n\n\t\tBarcode: " + str(self.shopping_history[item]['Barcode']))
                file.write("\n\t\tItem: " + item)
                file.write("\n\t\tQuantity: " + str(self.shopping_history[item]['Quantity']))
                file.write("\n\t\tTotal Amount: " + str(self.shopping_history[item]['Total']))
            file.write("\n\n\t\tGross Total: " + str(self.gross_total))
            file.write("\n\t\tTotal Discount: " + str(self.total_discount))
            file.write("\n\t\tNet Total: " + str(self.net_total))
            print("Your Receipt Has Been Successfully Saved.")
            file.close()
            exit(0)

        else:
            print("Your Cart Is Empty.")
            self.main_menu()

    def discount(self):
        if len(self.shopping_history) == 2:
            self.total_discount = (self.gross_total / 10)
            self.net_total = self.gross_total - self.total_discount
        elif len(self.shopping_history) == 3:
            self.total_discount = (self.gross_total / 15)
            self.net_total = self.gross_total - self.total_discount
        elif len(self.shopping_history) == 4:
            self.total_discount = (self.gross_total / 25)
            self.net_total = self.gross_total - self.total_discount
        else:
            self.net_total = self.gross_total

op = Operation()
op.menu()