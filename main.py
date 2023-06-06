import pickle

def load_data():
    try:
        with open('data.pickle', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}
    
def save_data(data):
    with open('data.pickle', 'wb') as file:
        pickle.dump(data, file)

def CreateNote():
    user = load_data()

    name = input('Enter your name -> ')
    note = input('Enter your note -> ')
    
    question = input('Do you want to make a note? ')
    if question.lower() == 'yes':
        user[name] = note
        save_data(user) 
    else:
        print('Bye!')

def ChangeNote():
    user = load_data()

    name = input('Enter your name -> ')
    note = input('Enter your note -> ')
    if name in user and user[name] == note:
        question = input('Do you want to change your note? ')
        if question.lower() == 'yes':
            new_note = input('New note -> ')
            user[name] = new_note
            save_data(user)
        else:
            print('Bye!')
    else:
        print('Error!')

def RemoveNote():
    user = load_data() 

    name = input('Enter your name -> ')
    note = input('Enter your note -> ')

    if name in user and user[name] == note:
        question = input('Do you want to exit the database? ')
        if question.lower() == 'yes':
            del user[name]
            save_data(user)
        else:
            print('Bye!')
    else:
        print('Error!')

def PrintAll():
    user = load_data()
    for i, j in user.items():
        print(f"name: {i} and note {j}")

def main():
    while True:
        print("*1* - CreateNote\n*2* - ChangeNote\n*3* - RemoveNote\n*4* - PrintAll\n*0* - exit")         
        check = int(input("-> "))
        if check == 1:
            CreateNote()
        if check == 2:
            ChangeNote()
        if check == 3:
            RemoveNote()
        if check == 4:
            PrintAll()
        elif check == 0:
            break

main()
