import pyttsx3
import random

engine = pyttsx3.init()

engine.setProperty('rate', 120)
engine.setProperty('volume', 3.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# speak('WELCOME TO TRUTH AND DARE')
# print('THE RULES OF THIS GAME ARE SIMPLE. SAY THE TRUTH AND DO THE DARE AND YOU MAY LEAVE, ELSE, YOU, DIEEE😈😈')
# speak('THE RULES OF THIS GAME ARE SIMPLE. , , SAY THE TRUTH AND DO THE DARE AND YOU MAY LEAVE, ELSE, YOU, DIE')

licence = """ The terms and condition states that:
            This app may contain some Horrific content and may cause some cases of truama on the brain
  By accepting the terms and condition you hereby accept that you are a legal citizens and that you are 18yrs and above of age
     """


from response import responses

def start_game():
    print('welcome to the game of doom🤡🤡')
    # speak('welcome to the game of doom')
    # speak('how many players are playing')
    users = []
    num_of_users = (int(input("How many users do you want to create? ")))
    for i in range(num_of_users):
  
        name = input("Enter the name of user " + str(i+1) + ": ")
        users.append(name)
    speak(f"{num_of_users} users has been created succesfully")     
    print(f" {num_of_users} users has been created succefully")
    while True:
        for i, user in enumerate(users):
            print(f"User {i+1}:", user)
        print(" ")
        for user in users:
            speak("it's " + user +"'s turn")
            print("It's " + user + "'s turn!")
            
            # question = random.choice(questions)
            # print(question)
            response_type = input("Truth or Dare? ")
            response_type = response_type.lower()
            while response_type not in ["truth", "dare"]:
                response_type = input("Please enter Truth or Dare only: ")
                response_type = response_type.lower()
            response = random.choice(responses[response_type])
            # speak(response)
            print(response)
            input('press enter key to continue')
            print("")

print("please read the terms and condition before accisesing this app")
terms =("""  TYPE Y FOR YES IF YOU HAVE ACCEPTED THE TERMS AND CONDITION
        TYPE N/NO OR Q/QUIT IF YOU DONT AGREE 
        TYPE VIEW TO VIEW THE TERMS AND CONDITION """)
print(terms)

while True:
    lic=(input(""))
    if lic == 'view':
        print(licence)
    elif lic == 'n':
        quit()
    elif lic == 'y':
        start_game()
        # print("The game has started")
    else:
        print("""not a command try 
    view - To view the Terms and condition
    n - To quit the game
    y - to start the game""")