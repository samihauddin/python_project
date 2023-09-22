import os
import sys
import yaml

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        yaml.load(file)
        file.close()
        print("YAML is VALID!")
    else:
        print(sys.argv[1] + " not found")

else:
    print("Usage: python check_json.py <file>")