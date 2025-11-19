def main_menu():
    print(f"welcome {user}")
    print(f'''
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                            -MAIN MENU-

          1. Print Statements
          2. Variables
          3. Operators
          4. Conditionals
          5. Loops
          6. Lists
          7. Functions
          0. Exit

    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
          ''')
    
def print_statements():
    print('''
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        -Print Statements-
          
          1. Simple Printing
          2. Concatenate Printing
          3. Back to Menu

    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
          ''')
    
def simple_printing():
    print('''
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                        -Simple Printing-
          In order to print something in python, we use the
          print() function. print() is a function which is
          used to display our outputs. It is the most common
          function that we use in python. It's also the first
          code that we wrote which is the print("Hello World")

          Input:
            print("Hello World!")
            print("Information Technology")
            print("BSIT-1A")
          
          Output:
            Hello World!
            Information Technology
            BSIT-1A

    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
          ''')
    
def concatenate_printing():
    print('''
    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                    -Concatenate Printing-
          Concatenate is a term of combining two or more varible
          like str, int, or list. In order to combine them, we
          have to use "+" or ",".

          For example,
            Input:
                str1 = "Hello"
                str2 = "World"
                str3 = "GodisGood"
          
                conc = str1 + str2 + str3
          
            Output:
                HelloWorldGodisGood
          
          Do note that if you use "+" it will provide no space
          unlike "," which can give space between your variables

    =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
          ''')
    
user = input("Please state your name : ")
while True:
    main_menu()
    choice = input("Choose your destination : ")
    if choice == "1":
        while True:
            print_statements()
            choice = input("Choose your destination : ")
            if choice == "1":
                simple_printing()
            elif choice == "2":
                concatenate_printing()
            elif choice == "3":
                break
            else:
                print("Invalid Input!")
                continue
