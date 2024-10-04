- **Developer**: Nalin

## Design of `constructor()` method

 - Define a constructor `init` with `self` being the current instance of the class.
 - The constructor `init`has two parameters `programmers` and `languages` of the datatype `list`.
 - Initialize the instance variables `self.languages` and `self.programmers` with empty dictionaries.
 - Define a local variable `index` of the datatype `int`.
 - Initalize the variable `index` with zero.
 - Use the `for loop` to iterate through the list `programmers` with the iterator variable as `programmer` (of datatype `string`).
    - Assign element at `index` of the list `languages` to the dictionary `self.programmers` with the iterator `programmer` being the key.
    - Use another `for loop` to iterate through the sublist `languages[index]` with `language`(of datatype `string`) as the iterator.
        - Check if the iterator `language` is in the dictionary `self.languages`.
            - If `language` is not present in the dictionary `self.languages` then assgin an empty list as value to the dictionary `self.languages` with the key as `language`(`self.languages[language]`)
        - Now add the name of the programmer to the empty list assigned to `self.languages[language]` by typecasting the `string` represented by the iterator `programmer` into a list.
    - Increment the value of the local variable `index` by 1.


## Design of `find_languages()` method

- Define a method `find_languages` with two parameters.
- The first parameter being `self` of datatype class instance and `programmer` of datatype `string` representing the programmer.
- Define a variable `list_of_languages`.
- Assign the languages list associated with the key `programmer` in the dictionary `self.programmers` to the variable `list_of languages`.
- Return `list_of_lanaguages`.

## Design of `find_programmers()` method

- Define  a method `find_programmers` with two parameters.
- The first parameter being `self` of datatype class instance and `language` of datatype `string` representing the programming language.
- Define a variable `list_of_programmers`.
- Assign the programmers list associated with the key `language` in the dictionary `self.languages` to the variable `list_of_programmers`.
- Return `list_of_programmers`.