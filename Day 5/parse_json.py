# parsing is making something (more) understandable. so makes json more understandable.
# json.loads converts json string into python dictionary
# open = opens up a file , then give the file you want to open
# .read = reading the contents
# value is a new variable and then insert name

import json
parsed_json = json.loads(open('example_json.json').read())
print(type(parsed_json))
value = parsed_json["name"]
print(value)

