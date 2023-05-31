my_argu= input("my argument :")

my_argu = my_argu.casefold()

rev_str = reversed(my_argu)

if list(my_argu) == list(rev_str):
   print("true")
else:
   print("false")

