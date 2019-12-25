import pytest, yaml, os

from getData import GetData


def get_sum_data():
    sum_list = []
    #     with open("./sum.yaml", "r", encoding="utf-8") as f:
    #         data = yaml.safe_load(f)
    #         print("data:{}".format(data))
    data = GetData().ge_yml_data("sum.yaml")
    for i in data.values():
        sum_list.append(tuple(i.values()))
    return sum_list


#
#
# print(get_sum_data())


class TestSum:
    @pytest.mark.parametrize("a,b,c", get_sum_data())
    # def test_sum(self,a,b,c):
    #     print("{}+{}={}",format(a,b,c))
    #     assert a+b == c
    def test_sum(self, a, b, c):
        print("{}+{}={}".format(a, b, c))
        assert a + b == c
