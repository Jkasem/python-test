def main():
  '''This is a
  test repository
  to get some Python reps in
  showing the differences from JavaScript'''

  5 % 1 # modulo
  5 ** 2 # exponentation
  True # Boolean primitives have a capital
  not False # negated with not
  # and or - boolean operators are very readable
  1 == 1 # equality
  1 != 1 # inequality
  1 > 2 > 3 # comparison chains

  # is vs ==
  a = [1, 0]
  b = [1, 0]
  b is a            # => False, a and b do not refer to the same object
  b == a            # => True, a's and b's objects are equal

  # Strings are immutable and can be accessed like a list of characters
  "String"[0] #'S'
  len("String") # to find length

  '{1} {0}'.format('one', 'two') # Placeholders can be used to format strings with index. Returns 'two one'.  Also do lots of other things like truncate or add padding.

  # Falsy values
  bool(0)   # => False
  bool("")  # => False
  bool([])  # => False
  bool({})  # => False
  bool(())  # => False

  # Convention is to use lower_case_with_underscores for variable names
  # No declarations only assignment

  # Ternary operator
  'Hello' if 2 > 3 else 'Goodbye'

  # Arrays called stores
  store = [1, 2, 3]
  store.append(4) # add to end with append
  store.pop() #remove with pop
  # Access like an array
  store[-1] # returns last item

  # Slice syntax to get ranges
  store[1:2] # format is [start:end:step]
  store[::2] # get every second entry
  store[::-1] # reverse array

  del store[2] # removes an index
  store.remove(1) # removes first occurance
  store.insert(0, 1)
  store.index(1) # get index
  1 in store # check for an entry

  # Tuples are lists but immutable

  # Dictionarys are like objects
  filled_dict = {"one": 1, "two": 2, "three": 3}
  # Keys must be an immutable type: ints, floats, strings, tuples.
  filled_dict["one"] # Look up values using bracket notation
  filled_dict.update({"four":4}) # add to dictionary
  del filled_dict["one"]  # Removes the key "one" from filled dict

  # Sets are dictionarys but each value must be unique

  # if elif and else
  # for loops to interate over lists
  for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))

  for i in range(4): #range(lower, upper, step)
    print(i)
  # while loops
  # Handle exceptions with a try/except block

if __name__ == "__main__":
  main()