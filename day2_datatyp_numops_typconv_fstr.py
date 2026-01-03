#day2: Data Types, Numeric Operations, Type Conversion, f-Strings
# Data Types
# Strings
name = "Alice"
print(f"Name: {name}, Type: {type(name)}")                      # Alice, <class 'str'>
print(f"First character: {name[0]}")                            # A
print(f"Substring (1-3): {name[1:4]}")                          # lic
print(f"Length of name: {len(name)}")                           # 5
print(f"Uppercase: {name.upper()} Lowercase: {name.lower()}")   # ALICE alice
print(f"Replace 'A' with 'E': {name.replace('A', 'E')}")        # Elice
print(f"Split by 'i': {name.split('i')}")                       # ['Al', 'ce']
print(f"Concatenation: {name + ' Smith'}")                      # Alice Smith
print(f"Repetition: {name * 2}")                                # AliceAlice
print(f"Membership Test: {'A' in name}")                        # True
print(f"Hold of last character: {name[-1]}")                    # e
print()
# Integers
number = 42
print(f"Number: {number}, Type: {type(number)}")                # 42, <class 'int'>
print(f"Addition: {number + 8}")                                 # 50
print(f"Subtraction: {number - 10}")                             # 32
print(f"Multiplication: {number * 2}")                           # 84
print(f"Division: {number / 2}")                                 # 21.0
print(f"Floor Division: {number // 5}")                          # 8
print(f"Modulus: {number % 5}")                                  # 2
print(f"Exponentiation: {number ** 2}")                          # 1764
print()

# Flaoats
"""
Your selection of 'Float' is correct 
because the presence of a decimal point in the number 734,529.678 indicates it is a floating-point value.
Even with the underscore for readability,
the decimal confirms that it isn't a whole number,
qualifying it as a Float.
"""
mystery = 734_529.678
print(f"Mystery number: {mystery}, Type: {type(mystery)}")      # 734529.678, <class 'float'>
print(f"Integer part: {int(mystery)}")                           # 734529
print(f"Addition: {mystery + 0.322}")                            # 734530.0
print(f"Subtraction: {mystery - 0.678}")                         # 734529.0
print(f"Multiplication: {mystery * 2}")                          # 1469059.356
print(f"Division: {mystery / 2}")                                # 367264.839
print(f"Floor Division: {mystery // 1000}")                      # 734.0
print(f"Modulus: {mystery % 1000}")                              # 529.678
print(f"Exponentiation: {mystery ** 2}")                         # 539569682290.784
print()