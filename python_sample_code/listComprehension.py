old_list = [1,2,3,4,5,6,7,8,9,10]
new_list = [x for x in old_list if x>= 5]
newer_list = [x if x <= 7 else None for x in new_list]

print(old_list)
print(new_list)
print(newer_list)