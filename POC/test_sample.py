# import yaml
import os


class Parser:
    def __init__(self):
        path_yaml = os.path.join(os.path.abspath("."), "sample.yml")
        try:
            with open(path_yaml) as file:
                a = file.readline()
                print(a)
        except:
            pass

