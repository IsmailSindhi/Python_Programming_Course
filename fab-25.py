# # write a pyhton fuction which takes there number as parameters and return the gretest of all

# # test the following functions for practice
# def greater(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# # m = greater(10, 6, 11)
# # print(m)
# # ____________________________________________________
# def greatest(a,b,c):
#     m = max(a,b,c)
#     return m

# # ____________________________________________
# def greatest_of_all(*args):
#     m = max(args)
#     return m
# a = greatest_of_all(1,2,4,5,6,5,6)
# print(a)

# a = greatest_of_all(1,2,4,5)
# print(a)
# # ___________________________________________


# # * multiplication in terms of numbers
# # *agrgs /// in fuctions
# def add(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
# a = add(1,2,3,4,5,7)
# print(a)
# # ___________________________________
def test(a,b,*args):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f'args = {args}')
test(1,2,3,4,5,7)












