
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
      "ID" : next_id,
      "website": user_website,
      "password": user_password
    }
    passwords.append(details)
    print("Details added successfully")
    print(f"Student ID: {next_id}")

  elif choice == "2":
    for details in passwords:
      print("ID: " , next_id)
      print("Website: " , user_website)
      print("Name: " , user_name)

      passcode = input("Enter safe code to access pasword: ")
      if passcode == master_pin:
        print("Password: " , user_password)
      else:
        print("Wrong code\n Password: ***********")

  elif choice == "8":
    print("See you later")
    break
