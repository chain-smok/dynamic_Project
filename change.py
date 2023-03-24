import pandas as pd
import json

def json_inputs(open_path):
    """
    返回json字符串列表
    :param path: 需要转换excel文件的路径
    :return: 返回json列表
    """
    df = pd.read_excel(open_path)
    # print(df)
    cols = [colName for colName in df.columns]
    json_list = []
    for row in df.itertuples():
        json_dict = {}
        for index in range(len(cols)):
            json_dict[cols[index]] = getattr(row,cols[index])
        json_list.append(json_dict)

    return json_list

def save_json(open_path,save_path):
    json_list = json_inputs(open_path)
    with open(save_path,"w",encoding="utf-8") as fw:
        #解决中文编码问题
        json.dump(json_list,fw,ensure_ascii=False)


if __name__ == '__main__':
    open_path = r'dynamic_project.xlsx'
    save_path = 'transfrom.json'
    save_json(open_path,save_path)