#A game named "Meow" in Nepali where a group a people make a circle and has to begin saying numbers. The catch is
#whenever there arrives a number which is a multiple of 3 or has 3 in it, He/she has to say "Meow". If not, he/she is out.
#Here is simple coding for the same.
def check_number(num):
  
  if num % 3 == 0 or '3' in str(num):
    return "Meow"
  else:
    return num


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Iterate over the numbers in the range
for i in range(start, end+1):
  print(check_number(i))
