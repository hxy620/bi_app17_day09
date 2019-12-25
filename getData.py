import yaml,os
class GetData:

    def ge_yml_data(self, yml_name):
        with open("./"+os.sep+yml_name, "r", encoding="utf-8") as f:
            # sum_list=[]
            # data = yaml.safe_load(f)
           return yaml.safe_load(f)
            # for i in data.values():
            #     sum_list.append(tuple(i.values()))
            # return sum_list