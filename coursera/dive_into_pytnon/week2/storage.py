import argparse
import os
import json
import tempfile

def wd(my_dict, key, value):
    if key in my_dict:
        try:
            my_dict[key].append(value)
        except AttributeError:
            my_dict[key]= [my_dict[key],value]
    else:
        my_dict[key] = value

parser = argparse.ArgumentParser()
parser.add_argument("-k","--key")
parser.add_argument("-v","--value")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if os.path.isfile(storage_path) == True:

    if args.value is not None:
        with open(storage_path, 'r') as read_file:
            m = json.load(read_file)
            wd(m, args.key, args.value)
        with open(storage_path, 'w') as write_file:
            json.dump(m, write_file)

    else:
        try:
            with open(storage_path, 'r') as read_file:
                m = json.load(read_file)
                if type(m[args.key]) is not str :
                    print(', '.join(m[args.key]))
                else:
                    print(m[args.key])
        except:
            print("")
else:
    dicti = {}
    with open(storage_path, 'w') as write_file:
        json.dump(dicti,write_file)
    with open(storage_path, 'r') as read_file:
        m = json.load(read_file)
        wd(m, args.key, args.value)
    with open(storage_path, 'w') as write_file:
        json.dump(m, write_file)
    if args.value is None:
        print("")
