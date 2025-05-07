import csv

FILENAME = "contacts.csv"

def load_contacts():
    """Read contacts from CSV into a dict (called once at start)."""
    contacts = {}
    try:
        with open(FILENAME, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contacts[row["Name"]] = row["Phone"]
        print(f"Loaded {len(contacts)} contacts.")
    except FileNotFoundError:
        # If file not found, start empty
        print("No contacts file found.")
    return contacts

def display_contacts(contacts):
    """Show all contacts currently in memory."""
    if not contacts:
        print("No contacts to show.")
    else:
        print("\nYour contacts:")
        for name, phone in contacts.items():
            print(f"  {name}: {phone}")

def add_and_save_contact(contacts):
    """Ask for a new contact, add it, then immediately write CSV."""
    name = input("Enter new contact name: ").strip()
    if not name:
        print("Name can’t be empty.")
        return
    phone = input("Enter phone number: ").strip()
    if not phone:
        print("Phone can’t be empty.")
        return

    # Add to in‑memory dict
    contacts[name] = phone
    print(f"Added {name} → {phone}")

    # Now save entire dict back to CSV
    with open(FILENAME, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["Name", "Phone"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for n, p in contacts.items():
            writer.writerow({"Name": n, "Phone": p})
    print("Contacts saved")

def menu():
    print("""
Contact Book
1. View contacts
2. Add a contact
3. Exit
""")

def main():
    # Auto-load once at start
    contacts = load_contacts()

    while True:
        menu()
        choice = input("Choose (1–3): ").strip()
        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            add_and_save_contact(contacts)
        elif choice == "3":
            print("Thank u")
            break
        else:
            print("Invalid choice—enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
1