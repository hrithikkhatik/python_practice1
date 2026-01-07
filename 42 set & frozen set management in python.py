user_ids = {1, 2, 4, 0}
print(user_ids,type(user_ids))
user_ids.add(-1)
print(user_ids)

system_group_A = frozenset({10, 20, 30})
system_group_B = frozenset({10, 50, 100, 200})
print(system_group_A,type(system_group_A))
print(system_group_B,type(system_group_B))
try:
    system_group_A.add(40)
except:
    print("frozen set cant add value")

system_group_A = frozenset({10, 20, 30})
system_group_B = frozenset({10, 50, 100, 200})
common_groups = system_group_A & system_group_B
print(common_groups)

all_groups = system_group_B | system_group_A
print(all_groups)

print(system_group_A - system_group_B)
print(system_group_B - system_group_A)



