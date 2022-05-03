import os, json, itertools, argparse, yaml, sys
import distutils.util
import datetime
import random 
import shutil


def flatten(lines):
    """
    Tages a list of lists as input. 
    Returns a flattened list.
    """
    return [item for sublist in lines for item in sublist]


def pick_n(list, n):
    return [random.choice(list) for i in range(n)]


def get_file_mod_datetime(file):
    return datetime.datetime.fromtimestamp(os.path.getmtime(file))
    

def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)


def empty_dir(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def save_text(path, txt):
    with open(path, "w", encoding="utf-8") as outfile:
        outfile.write(txt)


def load_text(path):
    with open(path, "r", encoding="utf-8") as infile:
        txt = infile.read()
    return txt


def load_yaml(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as infile:
        return yaml.load(infile, Loader=yaml.FullLoader)


def load_json(path):
    with open(path, "r", encoding="utf-8") as infile:
        data = json.load(infile)
    return data


def save_json(path, data, ensure_ascii=False):
    with open(path, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=ensure_ascii)


def save_yaml(path, data):
    with open(path, 'w', encoding="utf-8") as file:
        yaml.dump(data, file, allow_unicode=True)


def load_cfg(path):
    if path.endswith(".json"):
        return load_json(path)
    elif path.endswith(".yaml"):
        return load_yaml(path)
    else:
        raise Exception(f"Unsupported config format: {path}")


def save_cfg(path, data):
    if path.endswith(".json"):
        save_json(path, data)
    elif path.endswith(".yaml"):
        save_yaml(path, data)
    else:
        raise Exception(f"Unsupported config format: {path}")


def environ_or_required(key):
    return (
        {'default': os.environ.get(key)} if os.environ.get(key)
        else {'required': True}
    )


