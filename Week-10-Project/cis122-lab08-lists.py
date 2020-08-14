import random

def gen_random_integer_list(num, start_range = 1, end_range = 100, sort_list = 'N'):
   t = []
   if num <= 0:
      print('num must be > 0')
   elif not isinstance(num, int):
      print('num must be an integer')
   elif not isinstance(start_range, int) or not isinstance(end_range, int):
      print('start_range and end_range must be integers')
   else:
      for i in range(num):
         r = random.randint(start_range, end_range)
         t.append(r)

      if sort_list.upper() == 'Y':
         t.sort()

   return t




t = gen_random_integer_list(100)

def get_high_score(list_input):
    isList = isinstance(list_input, list)
    if isList is True:
        if not list_input:
            print("List is empty")
            return 0
    if isList is False:
        print("List argument expected")
        return -1

