# Summary of PROJETO5.py
The `PROJETO5.py` script is an interactive Python program that allows users to perform various operations on a list. Below is a summary of its functionality:

## Features

1. **Add Item to List**  
   - Users can add an item to the end of the list.

2. **Add Item at Specific Position**  
   - Users can specify a position to insert an item into the list. If the position is invalid, the program offers to insert the item at the end of the list.

3. **Remove Item from List**  
   - Users can remove all instances of a specified item from the list.

4. **Show Entire List**  
   - Displays all items currently in the list. If the list is empty, it notifies the user.

5. **Show Specific Item**  
   - Users can view an item at a specific position in the list.

6. **Check if Item Exists in List**  
   - Checks if a specified item exists in the list and displays its position(s).

## How to Use

- The program runs in a loop, prompting the user to select an operation by entering a number corresponding to the desired action:
  - `0`: Add item to the list.
  - `1`: Add item to the list at a specific position.
  - `2`: Remove item from the list.
  - `3`: Show all items in the list.
  - `4`: Show a specific item from the list.
  - `5`: Check if an item exists in the list.

- To exit the program, press "Enter" without typing anything.

## Example List Operations

- Initial list: `['apple', 'car', 'cat', 'apple', 'dog']`
- Add "banana" to the list: `['apple', 'car', 'cat', 'apple', 'dog', 'banana']`
- Remove "apple" from the list: `['car', 'cat', 'dog', 'banana']`
- Check if "dog" exists: Found at position 3.

## Notes

- The program includes redundant checks and error handling for testing and study purposes.
- Invalid inputs are handled gracefully, with appropriate prompts for the user.

This script is a simple yet effective way to practice list manipulation and user interaction in Python.