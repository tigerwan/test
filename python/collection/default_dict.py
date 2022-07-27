from collections import defaultdict
# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"

# Defining the dict
d = defaultdict(def_value)  # if key doos not existing, return default_value() response
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])


x = defaultdict(list)       # if key does not exist, return []
x['python'].append("awesome")
x['something-else'].append("not relevant")
x['python'].append("language")
print(x['python'])
print(x['nothing'])