import yaml
import pprint

cfg = yaml.safe_load(open('config1.yaml'))

# print(cfg)

pp = pprint.PrettyPrinter()
pp.pprint(cfg)