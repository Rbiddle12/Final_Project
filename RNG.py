'''This file checks if the code is accurate'''

def monster(monster_num, total_encounters):
    '''Fill in with a brief description of what this function is for and how it should be used.

    Args:
        The arguments are the name of a monster and which number is assigned to them

     Returns:
       If a number is called then it returns a name of a monster
     Examples:
        If Monster (2)
        returns "Dragon"
        If Monster (1)
        returns "Giant Monkey"
    '''

    if monster_num == 1 and total_encounters == 0:
        return "Angry Monkey"
    if monster_num == 2 and total_encounters == 0:
        return "Lizard"
    if monster_num == 3 and total_encounters == 0:
        return "Walking Plant"
    if monster_num == 4 and total_encounters == 0:
        return "Giant Hawk"

    if monster_num == 1 and total_encounters == 1:
      return "Rampaging Ape"
    if monster_num == 2 and total_encounters == 1:
      return "Flaming Lizard"
    if monster_num == 3 and total_encounters == 1:
      return "Man-Eating Plant"
    if monster_num == 4 and total_encounters == 1:
      return "Storm Eagle"           


def attack(num):
    '''Fill in with a brief description of what this function is for and how it should be used.
     Args:
         The argument is the attack of the character and it's an integer

     Returns:
         If the Attack is between 1 thru 4, including 1 and 4, It'll return 20 - 50

     Examples:
         Attack (2)
         return 30
         Attack (4)
         return 50
    '''
    if num == 1:
        return 20
    if num == 2:
        return 30
    if num == 3:
        return 40
    if num == 4:
        return 50


def Monster_Attack(num):
    '''Fill in with a brief description of what this function is for and how it should be used.
       Args:
           Any integer between 1 and 4, including 1 and 4, 

       Returns:
           If the num is 1 thru 4, it'll return 50-80

       Examples:
           Monster_Attack(1) = 50
           Monster_Attack(3) = 70
    '''
    if num == 1:
        return 50
    if num == 2:
        return 60
    if num == 3:
        return 70
    if num == 4:
        return 80

