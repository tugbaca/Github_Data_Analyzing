from RequestToApi.GithubData import GithupApi
import json


# function to add to JSON
def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':

    # # Ekim Ayı
    # filename1 = 'JsonDatas/OctoberDatas/data3.json'
    # filename2 = 'JsonDatas/OctoberDatas/data4.json'

    # # Kasım Ayı
    # filename1 = 'JsonDatas/NovemberDatas/data3.json'
    # filename2 = 'JsonDatas/NovemberDatas/data4.json'

    # Aralık Ayı
    filename1 = 'JsonDatas/DecemberDatas/data3.json'
    filename2 = 'JsonDatas/DecemberDatas/data4.json'


    obj_list = list()
    for github_page in range(21, 31):
        githup = GithupApi(page_number=github_page)
        obj_list.append(githup.datas)

    #print(obj_list)
    write_json(obj_list,filename1)

    obj_list2 = list()
    # page_number = 11
    for github_page in range(31, 41):
        githup = GithupApi(page_number=github_page)
        obj_list2.append(githup.datas)

    #print(obj_list2)
    write_json(obj_list2,filename2)

