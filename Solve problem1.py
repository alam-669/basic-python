def is_palindrome(my_argu):
   my_argu = my_argu.casefold()
   rev_str = reversed(my_argu)
   return list(my_argu) == list(rev_str)


def main():
   user_input = input("Enter a string: ")
   result = is_palindrome(user_input)
   print(result)




