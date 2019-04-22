my_known_people = ["John", "Rolf", "Anne"]
user_name = input("Enter your name: ")
if user_name in my_known_people:
    print("Hello, I know you!")


if user_name in my_known_people:
    print("Hello {}, I know you!".format(user_name))


if user_name in my_known_people:
    print("Hello {name}, I know you!".format(name=user_name))

"Hello {name}, I know you {}!".format("well", name=user_name)
"Hello {}, I know you {}!".format("John", "well")

#### Exercise

def who_do_you_know():
    people = input("Give me a list of people you know separated by commas: ")
    return [person.strip() for person in people.split(',')]

def ask_user():
    person = input("Give me a name: ")
    if person in who_do_you_know():
        print('You know {}!'.format(person))

ask_user()

# print([n for n in range(10) if n % 2 == 0])
