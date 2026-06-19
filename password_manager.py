
print("=== PASSWORD MANAGER ===")
print("Welcome")

master_pin = input("Create Master PIN: ")

print("Select one of the options bellow")
passwords = []
next_id = 0

while True:
  print("1. Add password")
  print("2. View password")
  print("8. Exit")

  choice = input("Selected choice: ")

  if choice == "1":
    next_id += 1
    user_website = input("Enter website: ")
    user_name = input("Enter username: ")
    user_password = input("Enter password: ")

    details = {
      "id" : next_id,
      "website": user_website,
      "username": user_name,
      "password": user_password
    }
    passwords.append(details)
    print("Details added successfully")
    print(f"Student ID: {next_id}")

  elif choice == "2":
    for details in passwords:
      if len(passwords) == 0:
        print("No data")
      else:
        print("ID: " , details["id"])
        print("Website: " , details["website"])
        print("Name: " , details["username"])
        print("password: *********")

  elif choice == "8":
    print("See you later")
    break

