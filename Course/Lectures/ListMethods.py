states = ["CA", "HI", "NY", "MA", "OR", "NV", "AZ"]

print(states)

input("\nPress Enter to continue...")

# len(s) -- Return the length (the number of items) of the object s.
# This is a built-in function that can be used with sequences and other collection
# types.

print("The list {} has {} elements".format(states, len(states)))

input("\nPress Enter to continue...")

if "CA" in states:
  print("California")

input("\nPress Enter to continue...")
  
if "TX" not in states:
  print("No Texas")
  
print(states)

input("\nPress Enter to continue...")

# list.append(elem) -- adds a single element to the end of the list.
# Common error: does not return the new list, just modifies the original.
  
states.append("TX")

print(states)
  
input("\nPress Enter to continue...")

# list.insert(index, elem) -- inserts the element at the given index, shifting
# elements to the right. If index is greater than or equal to current length
# element is added at end

states.insert(1, "WA")

print(states)

input("\nPress Enter to continue...")

# list.extend(list2) adds the elements in list2 to the end of the list.
# Using += on a list is similar to using extend().

states.extend(["NM", "ID"])

print(states)

input("\nPress Enter to continue...")

# list.remove(elem) -- searches for the first instance of the given element and
# removes it (throws ValueError if not present)

states.remove("WA")

print(states)

input("\nPress Enter to continue...")

# list.sort() -- sorts the list in place (does not return it).
# takes optional key and reverse arguments

states.sort()

print(states)

input("\nPress Enter to continue...")

states.sort(reverse=True)

print(states)

input("\nPress Enter to continue...")

# list.reverse() -- reverses the list in place (does not return it)

states.reverse()

print(states)

input("\nPress Enter to continue...")

# list.pop(index) -- removes and returns the element at the given index. Returns the
# rightmost element if index is omitted (roughly the opposite of append()).
# (throws IndexError if empty)

print(states)

lastElement = states.pop()

print(lastElement, "is no longer in the list")

print(states)

input("\nPress Enter to continue...")

anElement = states.pop(3)

print(anElement, "is no longer in the list")

print(states)

input("\nPress Enter to continue...")

anElement = states.pop(-5)

print(anElement, "is no longer in the list")

print(states)

# anElement = states.pop(100)

# lst.clear, lst.copy, del lst[index], lst.count, lst.index
