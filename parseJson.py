# Name: Saumya
# Challenge3 : We have a nested object. We would like a function where you pass in the object and a key and
# get back the value. 

def parse_json_object (json_obj, key):
    keys = key.split('/')
    current_obj = json_obj 
    
    for k in keys:
        if k in current_obj:
            current_obj = current_obj[k]
        else:
            return None
        
    return current_obj

obj1 = {"a": {"b": {"c": "d"}}}
obj2 = {"x": {"y": {"z": "a"}}}

key1 = "a/b/c"
key2 = "x/y/z"

Value1 = parse_json_object(obj1 , key1)
Value2 = parse_json_object(obj2 , key2)

if Value1 is not None:
    print (f"Value for '{key1}' is '{Value1}'")
else:
    print (f"Key '{key1}' is not found in the input json object.")

if Value1 is not None:
    print (f"Value for '{key2}' is '{Value2}'")
else:
    print (f"Key '{key2}' is not found in the input json object.")
