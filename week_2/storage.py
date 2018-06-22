import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--key', help='add key')
parser.add_argument('--value', help='add value')

args = vars(parser.parse_args())


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if not os.path.exists(storage_path):
    open(storage_path, 'w')

if args['value'] is None and args['key'] is not None:
    with open(storage_path, 'r') as f:
        tmp = []
        for line in f:
            data = json.loads(line)
            if args['key'] == data['key']:
                tmp.append(data['value'])
        if not tmp:
            print('')
        else:
            print(', '.join(tmp))

elif args['value'] is not None and args['key'] is not None:
    with open(storage_path, 'a') as f:
        f.write(json.dumps(args) + '\n')