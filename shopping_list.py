# -*- coding: utf-8 -*-
yes_words = ["yes", "y", "yup", "YES", "Yes"]

no_words = ["no", "n", "nop", "NO", "No"]

while True:
    def ask_yes_or_no_question(question_text):
        answer = raw_input(question_text)
        if  answer in yes_words: #sucht ob answer irgendwo in dieser Liste drin steht!
            return True
        elif answer in no_words:
            return False
        else:
            print "Wrong input! Please enter yes or no!"
    break




def add_item_to_list(item):
    item_to_list = raw_input(item)
    return shopping_list.append(item_to_list)



print "Welcome to your shopping list!"

shopping_list = []

while True:
    answer = ask_yes_or_no_question("Do you want to add an item? (yes/no)\n>> ")
    if answer == True:
        add_item_to_list("What do you want to add?\n>> ")
        "Nice your new list is:"
        for i in range(len(shopping_list)):
            t = i + 1
            print "\n%s. %s\n" % (t, shopping_list[i])
    elif answer == False:
        print "ok Bye Bye"
        break









