def display_menu():
    print("\n🛒 Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"✅ '{item}' added to the shopping list.")
            else:
                print("⚠️ You entered an empty item. Please try again.")

        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"❌ '{item}' removed from the shopping list.")
            else:
                print(f"⚠️ Item '{item}' not found in the shopping list.")

        elif choice == '3':
            if shopping_list:
                print("\n📋 Your Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("🗒️ Your shopping list is currently empty.")

        elif choice == '4':
            print("👋 Goodbye! Happy shopping!")
            break

        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
