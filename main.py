#REMOVE PASS AND FIX THE FUNCTION
def sum_of_products(list1, list2):
    list1 = list1.split()
    list2 = list2.split()
    if len(list1) == len(list2):
        total = 0
        for num in range(len(list1)):
            mult = int(list1[num]) * int(list2[num])
            total += mult
        print(total)
    else:
        print('error')

if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    inp1 = input()
    inp2 = input()
    sum_of_products(inp1, inp2)