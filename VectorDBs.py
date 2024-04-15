def pick_database():
    print("Choose a database:")
    print("1. Quadrant")
    print("2. Pinecone")
    print("3. ChromaDB")
    print("4. Waeviate")
    
    while True:
        choice = input("Enter the number corresponding to your choice: ")
        if choice in ["1", "2", "3", "4"]:
            choice = int(choice)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    
    if choice == 1:
        return "Quadrant"
    elif choice == 2:
        return "Pinecone"
    elif choice == 3:
        return "ChromaDB"
    elif choice == 4:
        return "Waeviate"

selected_database = pick_database()
print("You have selected:", selected_database)
