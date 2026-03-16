# empty dictionry
contacts = {}

while True:
    print('\n contact Book App')
    print('1. Create contact')
    print('2. view contact')
    print('3. update contact') 
    print('4. Delete contact') 
    print('5. search contact')
    print('6. count contact')
    print('7. Exit')

    choice = input('Enter your choice =')
    if choice == '1':
        name = input('Enter your name =')
        if name in contacts:
             print(f'contact name {name} already exist!')

        else:
            age = input('Enter age =')
            Email = input('Enter email =')
            Mobile = input('Enter mobile number=')
            contacts[name]= {'age':int(age),'email':Email, 'mobile':Mobile}

            print(f'contact name {name} has been created successfully!')

    elif choice =='2':
        name = input('Enter contact name to view =')

        if name in contacts:
             contact = contacts[name]
             print(f'Name:{name},Age:{age},Mobile number:{Mobile}')
        else:
            print('contact not found!')

    elif  choice =='3':
         name = input('Enter name to update contact =')
         if name in contacts:
            age = input('Enter updated age =')
            Email = input('Enter updated email =')
            Mobile = input('Enter updated mobile number=')
            contacts[name]= {'age':int(age),'email':Email, 'mobile':Mobile}
         else:
             print('contact not found!')

    elif  choice =='4':
        name = input('Enter contact name to delete=')
        if name in contacts:
            del contacts[name]

            print(f'contact name has been deleted successfully!')

        else:
            print('contact not found')

    elif choice == '5':
        Search_name = input('Enter contact name to search =')

        found = False

        for name,contact in contacts.items():
            if Search_name.lower() in name.lower():
                print(f'found-name {name}, Age:{age}, Mobile Number:{Mobile},Email:{Email}')                     
                found = True
                if not found:
                    print('No contact found with that name')


    elif choice == '6':
         print(f'total contacts in your book :{len(contacts)}')  

    elif choice == '7':
        print('Good bye closing the programe')
        break

    else: 
        print('invalid input')                   