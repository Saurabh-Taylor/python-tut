full_dot = '●'
empty_dot = '○'
def getDots(state):
    full_system = 10
    return (full_dot * state + empty_dot * (full_system - state))
    
def create_character(character_name, strength, intelligence, charisma):

    if not isinstance(character_name, str):
        return 'The character name should be a string'

    if not character_name:
        return 'The character should have a name'

    if (len(character_name.strip()) != len(character_name)):
        return 'The character name should not contain spaces'

    if len(character_name) > 10:
        return 'The character name is too long'

    if (type(strength) != int or type(intelligence) != int or type(charisma) != int):
        return 'All stats should be integers'

    if (strength < 1 or intelligence < 1 or charisma < 1):
        return 'All stats should be no less than 1'

    if (strength > 4 or intelligence > 4 or charisma > 4):
        return 'All stats should be no more than 4'

    if (strength + intelligence + charisma) <= 7:
        return 'The character should start with 7 points'

    return f"""{character_name}
STR {getDots(strength)}
INT {getDots(intelligence)}
CHA {getDots(charisma)}"""
    
   
    
app = create_character("sa", 2, 2, 3)
print(app)



# total_system = 10
#     left_strength =  total_system - strength
#     left_intelligence =  total_system - intelligence
#     left_charisma =  total_system - charisma
#     print(left_strength)
#     print(left_intelligence)
#     print(left_charisma)
    
#     for x in range(strength):
#         global variable
#         variable += full_dot
       
#     print(variable)