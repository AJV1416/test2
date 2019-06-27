start  = '''
You are now playing as Alice from Wonderland, Try and get through all the Disney characters!
'''

keepplaying = "yes"
print(start)

while keepplaying == "yes" or keepplaying =="Yes":
    print("Mickey is your first character, make sure you answer his question to get through")
    userchoice = input("What is my dog's name?")
    if userchoice == "Pluto"or userchoice =="pluto":
        print(" He looks happy and says Great job!")
        keepplaying = "no"
    else: 
        print("That is not correct try again, hint: It's similar to a planet.") 
        

keepplaying = "yes"
while keepplaying == "yes" or keepplaying == "Yes":
    print(" Great job, you've made it to your second character: Daisy Duck ")
    userchoice = input(" Who is her boyfriend?")
    if userchoice == "Donald Duck" or userchoice == "donald duck":
        print("Good job! that is correct.")
        keepplaying = "no"
    else: 
        print("That is not correct try again,") 


        
          


