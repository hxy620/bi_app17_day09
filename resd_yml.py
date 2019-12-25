import yaml

#读取文件
# with open("./value_02.yaml","r",encoding="utf-8") as f:
#     data = yaml.safe_load(f)
#
#     print("data:{}".format(data))
#     print("类型.{}".format(type(data.get("value"))))





data = {'Search_Data':
            { 'search_test_002':
                  {'expect': {'value': '你好'}, 'value': '你好'},
              'search_test_001':
                  {'expect': [4, 5, 6], 'value': 456}}}
#写入文件
with open("./ww.yml","w") as f:
    yaml.safe_dump(data,f ,encoding ="utf-8",allow_unicode=True)