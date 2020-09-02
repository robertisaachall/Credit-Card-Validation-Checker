import sys 
import re

try:
    inFile = sys.argv[1]
except IndexError as error_msg:
    print("No Arguments were added as test files, stopping script")
    sys.exit()
    
test_file = open(inFile,'r')
test_file_contents = test_file.readlines()

for entries in test_file_contents:
    print("Please enter your card number: " + entries)
    if bool(re.match('^[0-9]+$',entries)):
        credit_card_number = [int(x) for x in str(entries.strip())]
        replacements = 0;
        odd_numbered = 0;
        index = 0;
        if (len(credit_card_number) == 14): 
            for i in credit_card_number:
                if(index % 2 == 0):
                        above_double = i + i
                        if above_double >= 10: 
                            replacements = replacements + ((i + i) - 9)
                            index = index + 1
                        else:
                            index = index + 1      
                            replacements = replacements + (i+i)
                else:
                    index = index + 1
                    
                    odd_numbered = odd_numbered + i
                    continue
            
            if((odd_numbered + replacements) % 10 == 0):
                print("The number is valid")
            else:
                print("The number is not valid")
        else:
            print("Your card number is not long enough ,needs to be 14 numbers")
            print("Your card lenght is:" , len(credit_card_number))
            print("")
    else:
        print("You have entered a letter for your card, cannot contain letters")
        print("")

