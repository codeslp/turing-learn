a_set_len = int(input())
a = set(map(int, input().split()))

num_other_sets = int(input())

for i in range(num_other_sets):
    method_info = input().split()
    set_method, new_set_len = str(method_info[0]), int(method_info[1])
    new_set = set(map(int, input().split()))
    getattr(a, set_method)(new_set) # this will evaluate the string that is in set method. 
                                    # You can do this more readably with exec() or eval(), 
                                    # but these are both considered to be highly insecure in practice, 
                                    # because they will execute anything

print(sum(a))