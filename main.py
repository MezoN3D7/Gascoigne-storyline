def a():#press enter to continue
 input('')
 
 
def h():# for the choices yeas and no
 print('(1)Yes')
 print('(2)No')
 
def g2():
 print("Do you want to go back to the little girl's house" )
 h()
 k=int(input(''))
 if k==1:
   print("You decide to go bac to the little girl's house")
   a()
   print('You see the lights in the house turned on again')
   a()
   print('There is another girl')
   a()
   print('"Have you seen my sister?"')
   a()
   print('"Oh, how did this happen... Why would she ever go outside?"')
   a()
   print('It sounds like she went mad')
   a()
   print('The next time you came back to check on her she had alredy commited suicide')
 else:
   print('You continued your journey')
 
 
 
print('"Ahh, youve found yourself a hunter"')
a()
print('You suddenly wake up in this place called Yharnam.')
a()
print('People no longer live here, the only one that still roam in this town are people turned into beasts.')
a()
print('You are to hunt all of them.')
a()
print('After hunting the beasts, you encounter a house with its lights on.')
a()
print('There is a little girl')
print('Talk to the girl??') #choice 1
h()
 
 
b=int(input())
if b==1:
 print('"Who... are you? I dont know your voice, but I do know that smell... Are you a hunter?"')
 a()
 print('"Then please, will you look for my mum?" ')
 a()
 print('"Daddy never came back from the hunt and she went to find him, but now she’s gone too I’m afraid. I’m all alone, and scared."')
 a()
 print('Will you help her??')
 h()
 d=int(input(''))
 if d==1:
   print('"Really?"')
   a()
   print('"Oh, thank you!"')
   a()
   print('"My m-mum wears a red jeweled brooch. It’s so big and.. and beautiful. You won’t miss it."')
   a()
   print('"Oh, I mustn’t forget... If you find my mum, give her this musicbox."')
   a()
   print(' SMALL MUSICBOX ADDED TO THE INVENTORY')
   a()
   print('"It plays one of daddy’s favorite songs. And when daddy forgets us, we play it for him so he remembers. Mum’s so silly, running off without it!"')
   a()
   print('"Please be careful out there."')
 if d==2:
   print('Oh, alright.')
   a()
   print('"Well, t-hanks miss hunter for talking, at least. Take care on your hunt."')
   a()
   print('"Please be careful out there."')
   a()
 
if b==2:
 print('Your journey continues')
a()
 
print('Looking for the beasts, you enter a tomb.')
a()
print('There is another man killing the beasts')
a()
print('He is wearing a black hat and carrying an axe')
a()
print('Father Gascoigne : "...Beasts all over the shop... Youll be one of them, sooner or later..."')
a()
print('Will you attack him?')
h()
d=int(input())
if d==1:
 mg1=str(input('Type "haab" to attack : '))
 if mg1=="haab":
   a()
   print('Prey slaughtered')
   print('You killed Father Gascoigne')
   a()
 else:
   print('YOU DIED')
 print('You find a dead body near him. Its of a woman')
 a()
 print('She is wearing a Red Brooch')
 print('You took the Red brooch')
 a()
 
 print('Do you wanna continue the Journey?')
 h()
 e=int(input(''))
 if e==1:
   print('You go to check if the girl is still there')
   a()
   print('"Hello, mister hunter."')
   a()
   print('"Still can’t find my mum?"')
   a()
   print('"Okay. I can wait. But… isn’t there something I can do?"')
   a()
   print('"Maybe mum and dad are stuck out there waiting for me to come and find them."')
   a()
   print('Will you give her the Red Brooch?')
   h()
   f=int(input(""))
   if f==1:
     print('Mister hunter? Was it really her? Mummy… mummy… Don’t leave me alone… Mum... Come home... I’m alone… I’m scared… It’s not fair')
   if f==2:
     print('"Yes, I see. I can wait. I won’t be afraid. I know… I do. The morning always comes."')
     a()
     print('You know of two places where you can send her')
     a()
     print('The first place is Oedeon Chapel')
     print('Its a place owned by a blind creepy looking guy who claims that the place is safe for other people')
     a()
     print("The second one is Iosfeka's clinic")
     print('Its run by a nurse named Iosefka, she seems really nice and she is the one who treated you when you were hurt')
     a()
     print('What do you tell her?')
     print('(1)Go to Oeeon Chapel')
     print("(2)Go to Iosefka's clinic")
     print('(3)Stay at home')
     i=int(input(''))
     if i==1:
       print('"Yes, okay! Thank you mister hunter!"')
       a()
       print('"I love you almost as much as mum and dad."')
       a()
       print('A day later')
       print('She still isnt in the odeon chape')
       a()
       print('You decided to go look for her')
       a()
       print("Apparently she left for Odeon Chapel but didn't reach there")
       a()
       print('On your way you find a giant pig and next to it a dead body')
       a()
       print('The body has the same Red Jeweled Brooch you gave to that girl')
       a()
       print('The girl is dead')
       a()
       g2()
 
 
 
     if i==2:
       print('"Yes, okay! Thank you mister hunter!"')
       a()
       print('"I love you almost as much as mum and dad."')
       print("You go to Iosefka's clinic to meet her")
       a()
       print('Iosefka : "Oh, thank goodness you came....Be a dear, find me some more."  ')
       a()
       print('You feel like something is not rightwith Iosfeka')
       print('Will you break in to meet the girl?')
       h()
       j=int(input(''))
       if j==1:
         print('You entered the clinic')
         a()
         print('You see a woman in white clothes experimenting on a body of an blue alien')
         a()
         print('She is Isofeka and tries to kill you')
         a()
         print('But you overpower her and kill Isofeka')
         a()
         print('But you couldnt find the girl anywhere')
         a()
         g2()
       if j==0:
         print('You continued your journey')
 
 
 
 
     if i==3:
        print('"Yes, I see. I can wait. I won’t be afraid. I know… I do. The morning always comes."')
        print('Few days later you come to check on her,')
        a()
        print('The lights were closed and the window was broken with some drops of blood')
        a()
        print('And she is not there')
 
 
 if e==2:
   print('Thank you for playing')
   a()
   print('Its not the end tho') 
 
 
elif d==2:
 print('Gascoigne came charging at you with his axe and killed you')
 a()
 print('YOU DIED')
 
 

