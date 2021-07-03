# s = {1, "1",1.0}
# print(s)

# l1 = ["Mandeep", "Manoj","Mohan","Madhu", "Sissya"]
# i=0
# while i < len(l1):
#     if l1[i].startswith("M"):
#         print(f"hell {l1[i]}")
#     i = i+1

# for i in range(3):
#     print("*", end="")
#     print("*" if((i+1)%2) == 1 else " ", end="")
#     print("*")

def recursive_sum(num):
    if num == 1:
        return 1
    total = num + recursive_sum(num-1)
    return total
print(recursive_sum(5))
