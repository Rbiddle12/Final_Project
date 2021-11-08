
from random import randint
from RNG import  monster, attack, Monster_Attack

# Write all of your code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

monster_encounter = 0
encounters = 1
HP = 150
Monster_HP = 0

# gear = ["Iron Sword", "Iron Shield"]
# print((", ".join(map(str,gear))))
# weapon =input("Pick a Weapon: ")

# if encounters == 0:
#     monster_encounter = randint(1,4)
#     print("You ran into a " + monster(monster_encounter, encounters ))

# while HP > 0 and Monster_HP > 0:
  
 
#   print("-----------")
#   print("YOUR TURN")
#   print("-----------")

#   action = input(" Attack or Defend? ") 
 
#   if weapon == "Iron Sword" or weapon == "Sword" and action == "Attack" or action == "attack":
#     Damage = attack(randint(1, 4))
#     Monster_HP -=  Damage*1.25
#     print(f"Dealt {Damage*1.25}")

#   elif action == "Attack" or action == "attack":
#     Damage = attack(randint(1, 4))
#     Monster_HP -=  Damage
#     print(f"Dealt {Damage}")  


#   print("-----------")
#   print("MONSTER'S TURN")
#   print("-----------")


#   if action == "Defend" or action == "defend" and weapon == "Iron Shield" or weapon == "Shield":
#     Monster_Damage = Monster_Attack(randint(1,4))/2.5
#     HP -= (Monster_Damage)
#     print(f"Monster Dealt {Monster_Damage}")
#     print(f"Current HP {HP}")
  
#   elif action == "Defend" or action == "defend":
#     Monster_Damage = Monster_Attack(randint(1,4))/2
#     HP -= (Monster_Damage)
#     print(f"Monster Dealt {Monster_Damage}")
#     print(f"Current HP {HP}")

#   elif Monster_HP == 0 or Monster_HP < 0:
#     print("The " + monster(monster_encounter, encounters) + " Has Been Slain")  
#     encounters += 1
    
#   elif Monster_HP > 0 and action == "Attack" or action == "attack": 
#     Monster_Damage = Monster_Attack(randint(1,4))
#     HP -=  (Monster_Damage)
#     print(f"Monster Dealt {Monster_Damage}")
#     print(f"Current HP {HP}")

#   else:
#     print(monster(monster_encounter, encounters) + " Was Confused By Something")
  

#   if HP <= 0 and HP > -20:
#     print("You Were Slain by " + monster(monster_encounter, encounters))

#   if HP < -20:
#     print("You Got Bodied by " + monster(monster_encounter, encounters))


# if HP <= 0:
#   print("-----------")
#   print("You Lose")
#   print("-----------")

# else:
#   print("-----------")
#   print("You Win")
#   print("-----------")

gear = ["Greatsword", "Giant Shield", "Crossbow"]

if Monster_HP <= 0:
  print("The slain monster dropped some gear")
  print((", ".join(map(str,gear))))
  weapon =input("Pick a Weapon: ") 
  HP = 300
  Monster_HP = 200

if encounters == 1:
    monster_encounter = randint(1,4)
    print("You ran into a " + monster(monster_encounter, encounters))  


while HP > 0 and Monster_HP > 0:
  
  dodge = randint(1,2)

  print("-----------")
  print("YOUR TURN")
  print("-----------")

  action = input(" Attack or Defend? ") 
 
  if weapon == "Greatsword" or weapon == "Sword" and action == "Attack" or action == "attack":
    Damage = attack(randint(1, 4))*1.5
    Monster_HP -=  Damage
    print(f"Dealt {Damage}")

  elif weapon == "Crossbow" or weapon == "Bow" and action == "Attack" or action == "attack":
    Damage = attack(randint(1, 4))*1.3
    Monster_HP -=  Damage
    print(f"Dealt {Damage}")
    dodge_chance = randint(1,2)

  elif action == "Attack" or action == "attack":
    Damage = attack(randint(1, 4))*1.25
    Monster_HP -=  Damage
    print(f"Dealt {Damage}")      


  print("-----------")
  print("MONSTER'S TURN")
  print("-----------")


  if action == "Defend" or action == "defend" and weapon == "Giant Shield" or weapon == "Shield":
    Monster_Damage = Monster_Attack(randint(1,4))*1.25
    HP -= (Monster_Damage)/3
    print(f"Monster Dealt {Monster_Damage/3}")
    print(f"Current HP {HP}")
  
  elif action == "Defend" or action == "defend":
    Monster_Damage = Monster_Attack(randint(1,4))*1.25
    HP -= (Monster_Damage)/2
    print(f"Monster Dealt {Monster_Damage/2}")
    print(f"Current HP {HP}")
  
  elif dodge == dodge_chance and Monster_HP > 0:
    print("You dodged the "+ monster(monster_encounter, encounters)+ "'s attack")

  elif Monster_HP == 0 or Monster_HP < 0:
    print("The " + monster(monster_encounter, encounters) + " Has Been Slain")
    encounters += 1 
    

  elif Monster_HP > 0 and action == "Attack" or action == "attack": 
    Monster_Damage = Monster_Attack(randint(1,4))*1.25
    HP -=  (Monster_Damage)
    print(f"Monster Dealt {Monster_Damage}")
    print(f"Current HP {HP}")

  
  else:
    print(monster(monster_encounter, encounters) + " Was Confused By Something")
  

  if HP <= 0 and HP > -20:
    print("You Were Slain by " + monster(monster_encounter, encounters))

  if HP < -20:
    print("You Got Bodied by " + monster(monster_encounter, encounters))  

if HP <= 0:
  print("-----------")
  print("You Lose")
  print("-----------")

else:
  print("-----------")
  print("You Win")
  print("-----------")    