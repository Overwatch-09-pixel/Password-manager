
print("=== PASSWORD MANAGER ===")
print("Welcome")

master_pin = input("Create Master PIN: ")

print("Select one of the options bellow")
passwords = []
next_id = 0

while True:
  print("1. Add password")
  print("8. Exit")

  choice = input("Selected choice: ")

  if choice == "1":
    next_id += 1
    user_website = input("Enter website: ")
    user_name = input("Enter username: ")
    user_password = input("Enter password: ")

    details = {
      "ID" : next_id,
      "website": user_website,
      "password": user_password
    }
    passwords.append(details)
    print("Details added successfully")
    print(f"Student ID: {next_id}")

  elif choice == "8":
    print("See you later")
    break
