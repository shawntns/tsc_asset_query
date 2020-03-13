import os
import yaml

def loadyamlfile(yamlfile):
    configfilelist = []
    with  open(yamlfile, encoding='utf-8') as f:
        y = yaml.load_all(f)
        for data in y:
            configfilelist.append(data)
        return configfilelist

def getnessussearchyaml():# yamlfile里面放配置文件
    yamllist = []
    dirpath = os.path.dirname((os.path.abspath(__file__)))
    yamldir = os.path.join(dirpath,'yamlfile')
    for file in os.listdir(yamldir):
        if file.endswith('yml'):
            filepath = os.path.join(yamldir,file)
            print(filepath)
            ayamllist = loadyamlfile(filepath)
            yamllist.extend(ayamllist)
    return yamllist
