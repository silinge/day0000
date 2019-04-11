types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"

y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
hilarious_ture = True
Is_number_ok =250364189546
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))
#see whtat .format do here
print("Hello, .format {}, {}".format("firstplace", "second one"))
print("I want put a true here, {}".format(hilarious_ture))
print("can I add a real number? see {}".format(Is_number_ok))
# print(f"what if make f_string and .format in one blank? {types_of_people},".format("is this ok"))
#fstring work at first .format have no place here.
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)