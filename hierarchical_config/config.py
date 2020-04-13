from os import path
import yaml
import json


class Config:
    def __init__(self, config_files=[], sep="_$_$_"):
        self.sep = sep
        self.config_file_paths = config_files
        self.cacher = {}

        # Read files:
        self.config_files = [self.read_file(fp) for fp in self.config_file_paths]    
        self.flat_dicts = [self.flatten_dict(d) for d in self.config_files]
    
    def squash(self):
        for i in range(1, len(self.flat_dicts)):
            d = self.impose(self.flat_dicts[i-1], self.flat_dicts[i])
        return d

    def impose(self, dict_a, dict_b):
        return {**dict_a, **dict_b}
    

    # ------ Rebuild dict ------
    # TODO: This
    def rebuild(self, dict_):
        new_dict = {}
        for full_k,v in dict_.items():
            keys = full_k.split(self.sep)
            for par_k in keys:
                if new_dict.get(par_k, False):
                    pass

    def check(self, key):
        pass
    # ------ Rebuild dict ------

    def read_file(self, file):
        if path.exists(file):
            file_type = file.split(".")[-1]
            if file_type in ("yml", "yaml"):
                with open(file, "r") as f:
                    d = yaml.load(f, Loader=yaml.FullLoader)
            elif file_type in ("json"):
                with open(file, "r") as f:
                    d = json.load(f)
            else:
                raise Exception(f"File type not recognized: {file_type}")
        else:
            raise Exception(f"Could not find file: {file}")
        return d

    def _flatten_dict(self, dict_, path=""):
        if path == "":
            sep_ = ""
        else:
            sep_ = self.sep
        for k,v in dict_.items():
            
            if type(v) != dict:
                self.cacher[path+sep_+k] = v
            else:
                self._flatten_dict(v, path+sep_+k)
    
    def flatten_dict(self, dict_):
        self.cacher = {}
        self._flatten_dict(dict_)
        return self.cacher
    


            



        


            
    


    def read_yaml(self, file):
        pass
    def read_json(self, file):
        pass




if __name__ == "__main__":
    a = {"a": "hello", "b":"bye", "c": {"hgh": 78, "h": {"gh": 45}}, "k": ["heh", "67"]}
    b = {"a": "hello", "b":"bye", "c": "ccccc", "h": "gggface"}
    c = Config()
    c.flatten_dict(a)
    print(c.cacher)
    
