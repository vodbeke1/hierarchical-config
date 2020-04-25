from os import path
import yaml
import json
from collections.abc import Iterable


class Config:

    def __init__(self, config_files=set(), sep="_$_$_"):
        self.sep = sep
        self.config_file_paths = config_files
        self.cacher = {}
        self.config = {}

        # Read files:
        self.config_files = [self.read_file(fp) for fp in self.config_file_paths]    
        self.flat_dicts = [self.flatten_dict(d) for d in self.config_files]
        self.config = self.squash(self.flat_dicts)
        #self.config_rebuilt = self.rebuild(self.config)

    def __str__(self):
        return str(self.config)

    def __getitem__(self, key):
        if isinstance(key, (list, tuple, set)):
            key = self.sep.join(key)
        try:
            return self.config[key]
        except KeyError:
            raise Exception(f"Key path {key} not found")

    def get(self, key, default=None):
        if isinstance(key, (list, tuple, set)):
            key = self.sep.join(key)
        return self.config.get(key, default)

    def items(self):
        return self.config.items()

    def squash(self, flat_dicts):
        for i in range(1, len(flat_dicts)):
            if i == 1:
                d = self.impose(flat_dicts[i-1], flat_dicts[i])
            else:
                d = self.impose(d, flat_dicts[i])
        return d

    def impose(self, dict_a, dict_b):
        return {**dict_a, **dict_b}

    # ------ Rebuild dict ------
    # TODO: This
    def rebuild(self, dict_):
        new_dict = {}
        for full_k,_ in dict_.items():
            keys = full_k.split(self.sep)
            for par_k in keys:
                if new_dict.get(par_k, False):
                    pass
        return None

    def check(self, key):
        pass
    # ------ Rebuild dict ------

    def read_file(self, file):
        if path.exists(file):
            file_type = file.split(".")[-1]
            with open(file, "r") as f:
                if file_type in ("yml", "yaml"): 
                    d = yaml.load(f, Loader=yaml.FullLoader)
                elif file_type in ("json"):
                    d = json.load(f)
                else:
                    raise Exception(f"File type not recognized: {file_type}")
        else:
            raise Exception(f"Could not find file: {file}")
        return d

    def _flatten_dict(self, dict_, path=""):
        sep_ = self.sep if path else path
        for k,v in dict_.items():
            if type(v) != dict:
                self.cacher[path+sep_+k] = v
            else:
                self._flatten_dict(v, path+sep_+k)
    
    def flatten_dict(self, dict_):
        self.cacher = {}
        self._flatten_dict(dict_)
        return self.cacher


if __name__ == "__main__":
    #a = {"a": "hello", "b":"bye", "c": {"hgh": 78, "h": {"gh": 45}}, "k": ["heh", "67"]}
    #b = {"a": "hello", "b":"bye", "c": "ccccc", "h": "gggface"}
    #c = Config()
    #c.flatten_dict(a)
    #print(c.cacher)
    empty_str = ""
    if empty_str:
        print("dpesnt work")
    else:
        print("does work")
    
