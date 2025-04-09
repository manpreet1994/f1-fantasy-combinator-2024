import json
import pickle

def write_json(filename, json_object):
    with open(filename, "w") as outfile:
        outfile.write(json.dumps(json_object))

def save_pickle(filename, object):
    with open(filename, "wb") as outfile:
        pickle.dump(object, outfile, protocol=pickle.HIGHEST_PROTOCOL)

def read_pickle(filename):
    with open(filename, "rb") as outfile:
        b = pickle.load(outfile)
    return b

def read_json(filename):
    with open(filename, 'r') as openfile:
        json_object = json.load(openfile)
        return json_object