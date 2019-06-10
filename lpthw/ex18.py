def print_two(*args):
    arg_one, arg_two = args
    print(f"One : {arg_one}, and two is: {arg_two}")

def print_to_two(arg1, arg2, arg3):
    print("ONE, TWO, THREE, GO, {},{},{}".format(arg1, arg2, arg3))
    print("ONE, TWO, THREE, GO, {},{}".format(arg1, arg2) + ",{}")
    print(f"ONE, TWO, THREE, GO, {arg3},{arg1}")

def print_None(arg11):
    print(f"There is nothing here: {arg11}, ")

# print_to_two(245, 90, 100)
print_None()