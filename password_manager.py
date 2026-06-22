
print("=== PASSWORD MANAGER ===")
print("Welcome")

master_pin = input("Create Master PIN: ")

print("Select one of the options bellow")
passwords = []
next_id = 0

while True:
  print("1. Add password")
  print("2. View passwords")
  print("3. Search password")
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
    if len(passwords) == 0:
      print("No data")
    else:  
      for details in passwords:
        print("ID: " , details["id"])
        print("Website: " , details["website"])
        print("Name: " , details["username"])
        print("password: *********")

  elif choice == "3":
    print("1. Search by ID")
    print("2. Search by Website")
    print()
    search = input("Search by: ")
    if search == "1":
      passwrd = input("Enter password ID: ")
      found = False
      for details in passwords:
        if details["id"] == passwrd:
          found = True
          print("Found")
          print("ID: " , details["id"])
          print("Website: " , details["website"])
          print("Name: " , details["username"])
          print("Password: *******")
        else:
          print("No password record")
      
    elif search == "2":
      for details in passwords:
        search_website = input("Enter wedsite: ")
        found = False
        matches = []
        count = 0
        for details in passwords:
          if details["website"] == search_website:
            found = True
            matches.append(details["website"])
            if len(matches) == 0:
              print("Website not found")
            elif len(matches) == 1:
              print("ID: " , details["id"])
              print("Website: " , details["website"])
              print("Name: " , details["username"])
              print("Password: ******")
            elif len(matches) > 1:
              print("Accounts found: ")
              for account in matches:
                count += 1
                print(account["username"])
                selection = input("Select account: ")
                if selection > 1 and selection <= len(matches):
                  matches[selection - 1]
                  print("ID: " , account["id"])
                  print("Website: " , account["website"])
                  print("Name: " , account["name"])
                  print("Password: ******")
          if not found:
            print("Account number not available")
            print("Only" , len(matches), "accounts are available")

  elif choice == "8":
    print("See you later") 
    break
