"""
CIS 122 Assignment 08
Name: Ohm Sabpisal
Credit: N/A
Class: CIS 122
Date: December 6, 2019
Description: This project is the ultimate test of human capability in 5 hours.
"""

run = True
#global user_input_group_name # Initialize key_list in order for this list to be used as the value of the user_input_group_name dictionary which is inside the dictionary_for_groups dictionary.


# Part 1: Required Function:
def create_group(user_input_group_name):  # Creates a new group and group properties.
    global the_group_name
    the_group_name = user_input_group_name
    if len(user_input_group_name) == 0:
        exit
    elif user_input_group_name != 0:
        """
        Name of the key inside the dictionary_for_groups 
        dictionary.
        """
        dictionary_for_groups[user_input_group_name] = {}
        """
        Create a new dictionary in the dictionary_for_groups. 
        The key of this dictionary will be called the value of
        the user_input_group_name_variable.
        """
        keys_list = []
        dictionary_for_groups[user_input_group_name]['_data_'] = {}
        while True:
            user_input_field_name = input("Enter field name (empty to stop): ").strip()
            if len(user_input_field_name) == 0:
                break
            elif len(user_input_field_name) != 0:
                keys_list.append(user_input_field_name)
                dictionary_for_groups[user_input_group_name]['_data_'][user_input_field_name] = ''

                """        
                Add the field name into the list which is a value 
                of the user_input_group_name dictionary which is 
                inside the dictionary_for_groups dictionary.
                """
        dictionary_for_groups[user_input_group_name]['_keys_'] = keys_list
        """
        Set a value of the key named '_keys_' which 
        inside of the user_input_group_name dictionary.
        """
        print(dictionary_for_groups)

# Part 7: List Groups
def list_groups():  # List group names and numbers of properties.
    print("** List of Groups **")
    for key, value in dictionary_for_groups.items():
        current_key = key
        print(key.title() + " : " + str(len(value['_keys_'])) + " properties " + str(value['_keys_']))

# Part 8: Add Group Data
def add_group_data(): # Add data to a group to a group for each group property.
    print("** Add group data **")
    print("** List of Groups **")
    for key, value in dictionary_for_groups.items():
        current_key = key
        print(key.title() + " : " + str(len(value['_keys_'])) + " properties " + str(value['_keys_']))
    group_to_add_data = input("Enter group (empty to cancel): ")
    for properties in dictionary_for_groups[group_to_add_data]['_keys_']:
        user_property_replacement = input("Enter " + properties + ": ")

# Part 9: List Data for Group
def list_group_data(): # List all data for a group.
    print("** List of group data**")
    print("** List of Groups **")
    #user_list_group_data = input("Enter group name (empty to cancel): ")
    user_0 = dictionary_for_groups["Songs"]["_data_"][0]
    print(user_0)
    #for key, value in user_0.items():
     #   print(key)

# Part 2: Group Variable
dictionary_for_groups = {

}

# Part 3: Primary Input Loop
print(">> Welcome to Group Manager <<")
print("This program creates groups with dynamic properties\n")

while run:
    user_prompt = input("Command (empty or X to quit, ? for help): ").strip()
    user_prompt = user_prompt.strip()
    user_prompt = user_prompt.upper()
    if len(user_prompt) == 0:
        run = False
    elif (user_prompt == 'X'):
        run = False
    elif user_prompt == '?':
    # Part 4: Help Command
        print('?: list commands\n' +
              'C: Create a new group\n' +
              'G: List groups\n' +
              'A: Add data to a group\n' +
              'L: List data for a group\n' +
              'X: Exit\n')

    # Part 6: Create New Group
    if (user_prompt == 'C'):
        user_input_group_name = input("Enter group name (empty to cancel): ").strip()
        create_group(user_input_group_name)
    # Part 7: List Group
    if (user_prompt == 'G'):
        list_groups()
    # Part 8: Add Group Data
    if (user_prompt == 'A'):
        add_group_data()
    # Part 9: List Data for Group
    if (user_prompt == 'L'):
        list_group_data()


print(dictionary_for_groups)
