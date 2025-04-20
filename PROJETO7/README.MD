## CREATING, READING AND WRITING FILES

A simple program to allow the user to create folders, create and override text on .txt files, and check the text on .txt files.

For programs such as this that allow the user to create folders and files, a validate function is useful to make sure the user is not using any characters that are prohibited by the OS. Since we are coding in Windows, we prohibit the following:

```python
def validate(c):
    prohibited = '<>:"/\\|?*'
    if any(character in c for character in prohibited):
        print('Invalid name.')
        main_menu()
```
**NOTE**: the term "character" is just a variable to hold the characters in the strings, and doesn't have any meaning by itself. The program knows that we want to sweep every character of "c" to see if there are any "prohibited" because the "in" operation **iterates** on the variable. "c" and "prohibited" are strings, and **strings are iterable**, same as lists, tuples etc, but instead of iterating item by item, strings are checked character by character. The **any** function just returns True or False based on the condition.

