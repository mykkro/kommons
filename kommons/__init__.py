import os, json, itertools, argparse, yaml, sys
import distutils.util
import datetime

# YAML/JSON I/O

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


