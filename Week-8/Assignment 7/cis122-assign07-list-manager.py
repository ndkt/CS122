"""
CIS Assignment 7
Name: Ohm Sabpisal
Credit: N/A
Class: CIS 122
Date: 22 NOvember 2019
Credit: N/A
"""
t = []

def cmd_help():
    print("* Available commands *")
    help_list=["Add","Delete","List","Clear"]
    description_list=["Add to list","Delete information","List information","Clear list"]
    for cmds, desc in zip(help_list, description_list):
        pad_left(cmds, 10), print(desc)
    print("Empty to exit")

def cmd_add(t):
    while True:
        data = input("Enter information (empty to stop): ")
        if len(data) == 0:
            break
        else:
            t.append(data)
            print("Added, item count = " + str(len(t)))

def cmd_delete(t):
    while len(t) >= 1:
        for i in t:
            pad_left(str(t.index(i)), 8)#, pad_right(str(i), 2)  
        delete = input("\nEnter a number to delete (empty to stop): ").strip()

        if delete.isdigit():  
            t.pop(int(delete))  

        elif len(delete) == 0:
            break
        else:
            print("Unknown command")
    print("All items deleted")  # print only when list is empty


def cmd_list(t):
    print("List contains " + str(len(t)) + " item(s)")
    for data in t:
        print(data)
def cmd_clear(t):
    total=len(t)
    t.clear()
    print(str(total)+" item(s) removed, list empty")
def get_max_list_item_size(t): pass
   
def pad_string(data, space):
    print(data.ljust(space))
def pad_left(data, space):  
    print(data.ljust(space), end="")
def pad_right(data, space): 
    print(data.rjust(space))


while True:
    cmd= input("Enter a command (? for help): ").strip()
    if len(cmd) == 0:
        break
    if cmd =="?":
        cmd_help()
    if cmd =="add":
        cmd_add(t)
    if cmd =="list":
        cmd_list(t)
    if cmd =="clear":
        cmd_clear(t)
    if cmd =="del":
        cmd_delete(t)