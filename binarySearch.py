import timeit
start_time = timeit.default_timer()

def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    
    # while the range isn't empty
    while left <= right:
        # integer division rounds down
        middle = (left + right) // 2
        value = lst[middle]
        
        if value == target:
            # found it!
            return middle
        elif value < target:
            # too small, shrink the left boundary
            left = middle + 1
        else:
            # too big, shrink the right boundary
            right = middle - 1
    
    # if the loop ends, the range is empty, so target was not found
    return -1

ls = [1,2,3,4,5,6,7,8,9]

# print(binary_search(ls,5))
# elapsed = timeit.default_timer() - start_time
# print(elapsed)


class User:
    def __init__(self, id_number, name):
        self.id_number = id_number
        self.name = name
    def __repr__(self):
        fmt = 'User({!r}, {!r})'
        return fmt.format(self.id_number, self.name)

users = [
    User(12, 'Waylon Dalton'),
    User(15, 'Justine Henderson'),
    User(20, 'Abdullah Lang'),
    User(28, 'Marcus Cruz'),
    User(45, 'Thalia Cobb'),
    User(46, 'Mathias Little'),
    User(51, 'Eddie Randolph'),
    User(60, 'Angela Walker'),
    User(63, 'Lia Shelton'),
    User(72, 'Hadassah Hartman'),
    User(78, 'Joanna Shaffer'),
    User(95, 'Jonathon Sheppard')
]

# for val in enumerate(users):
#     print (val)


# while(True):
#     x = 0
#     if (x <= int(users.count)):
#         print(users[x])
#         x += 1
#     else:
#         break




#  for x in users:
#      print(users[x])
#     x+=1
# for key, value in d.items():
print(users[1])