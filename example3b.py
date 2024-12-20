# The IN operator
# This example shows the use of the in operator with a list/tuple of literal values

friends = ["Christine","Richard","Angela","Sandra"]

while True:
  print(f"The list contains {friends}")
  x = input("Enter a name to look for")
  if x in friends:
    print(f"{x} is in the list of friends")
  print("\n\n")
