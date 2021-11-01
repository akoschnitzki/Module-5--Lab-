#Name- Alexander Koschnitzki
#Date - 10-28-21
#CSS- 225

for i in range(0,51):
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
        continue
    elif i % 3 == 0:
        print("Divisible by three")
        continue
    elif i % 5 == 0:
        print("Divisible by five")
        continue
    print(i)

# What this program does is that it is able to sort all the
# numbers that are divisible by five, divisible by three and
# divisible by both of them. It is able to print them on their own
# lines. You can be able to change the range to be able to get more
# outcomes for this program.