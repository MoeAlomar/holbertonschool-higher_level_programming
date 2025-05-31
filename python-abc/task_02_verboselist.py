#!/usr/bin/python3
"""VerboseList class that extends the built-in list class.

This module provides a VerboseList class that prints notification messages
whenever items are added or removed from the list.
"""


class VerboseList(list):
    def append(self, item):
        """Add an item to the end of the list with notification.

        Args:
            item: The item to be added to the list.
        """
        super().append(item)
        print(f"Added [{item}] to this list.")

    def extend(self, iterable):
        """Extend the list with items from an iterable with notification.

        Args:
            iterable: An iterable object containing items to add to the list.
        """
        items_to_add = list(iterable)
        super().extend(items_to_add)
        print(f"Extended the list with [{len(items_to_add)}] items.")
    
    def remove(self, item):
        """Remove the first occurrence of an item from the list with notification.

        Args:
            item: The item to be removed from the list.
            
        Raises:
            ValueError: If the item is not found in the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        """Remove and return an item at the given index with notification.

        Args:
            index (int, optional): The index of the item to remove. 
                                 Defaults to -1 (last item).

        Returns:
            The item that was removed from the list.
            
        Raises:
            IndexError: If the list is empty or index is out of range.
        """
        if len(self) == 0:
            raise IndexError("pop from empty list")

        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop.(index)
    
print("Testing VerboseList:")
print("=" * 30)

# Create a VerboseList instance
vlist = VerboseList()

# Test append method
print("\n1. Testing append:")
vlist.append("apple")
vlist.append("banana")
vlist.append(42)
print(f"Current list: {vlist}")

# Test extend method
print("\n2. Testing extend:")
vlist.extend(["cherry", "date"])
vlist.extend([1, 2, 3])
print(f"Current list: {vlist}")

# Test remove method
print("\n3. Testing remove:")
vlist.remove("banana")
vlist.remove(42)
print(f"Current list: {vlist}")

# Test pop method
print("\n4. Testing pop:")
popped_item = vlist.pop()  # Pop last item
print(f"Returned item: {popped_item}")
popped_item = vlist.pop(0)  # Pop first item
print(f"Returned item: {popped_item}")
print(f"Final list: {vlist}")

# Test edge cases
print("\n5. Testing edge cases:")
try:
    vlist.remove("nonexistent")
except ValueError as e:
    print(f"Error: {e}")

# Empty the list and try to pop
vlist.clear()
try:
    vlist.pop()
except IndexError as e:
    print(f"Error: {e}")