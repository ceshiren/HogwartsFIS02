import yaml

yaml_data = yaml.safe_load(open("data.yml"))

a = [[{'a': 1}, 'admin2'], 'admin3']

with open("data3", "w") as f:
    yaml.safe_dump(a,f)