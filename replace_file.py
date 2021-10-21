import os

# file name
file = "original_file.json"

with open(file) as json_file:
    data = json.load(file)

os.remove(file)

out_file = open(file, 'a')
out_fiile.writelines('all clean')
out_file.close()