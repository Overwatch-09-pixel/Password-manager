
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
    print(f"Password ID: {next_id}")

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
      passwrd = int(input("Enter password ID: "))
      found = False
      for details in passwords:
        if details["id"] == passwrd:
          found = True
          print("Found")
          print("ID: " , details["id"])
          print("Website: " , details["website"])
          print("Name: " , details["username"])
          print("Password: *******")
          break
      if not found:
        print("No password record")
      
    elif search == "2":
      search_website = input("Enter website: ")
      matches = []
      for details in passwords:
          if details["website"] == search_website:
            matches.append(details)
      if len(matches) == 0:
          print("Website not found")
      elif len(matches) == 1:
          details = matches[0]
          print("ID: " , details["id"])
          print("Website: " , details["website"])
          print("Name: " , details["username"])
          print("Password: ******")
      else:
          print("Accounts found:")
          count = 1
          for account in matches:
            print(count, "." , account["username"])
            count += 1
          try:
              selection = int(input("Select account: "))
              if 1 <= selection <= len(matches):
                chosen = matches[selection - 1]
                print("ID: " , chosen["id"])
                print("Website: " , chosen["website"])
                print("Name: " , chosen["username"])
                print("Password: ******")
              else:
                print("Account number not available")
                print("Only" , len(matches), "accounts are available")
          except ValueError:
            print("Invalid input")

  elif choice == "4":
    password_id = int(input("Password ID: "))
    found = False
    for details in passwords:
      if password_id == details["id"]:
        found = True
        for r in range(3):
          PIN = input("Enter Master PIN: ")
          attempts_left = 2-r
          if PIN != master_pin:
            print("incorrect! try again\nAttempts left" , attempts_left)
          elif PIN == master_pin:
            print("Password: " , details["password"])
      else:
        print("Wrong PIN\nReturning to menu")

  elif choice == "8":
    print("See you later") 
    break
