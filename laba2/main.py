import json

from laba2.proximity_measures import euclid_distance, cos_distance, mera_polovinkina, general_nonnull_parameters, \
    general_null_parameters, generalizing_measure, tree_measure

m = 14  # количество полей объекта

# веса признаков
weights_attributes = [0, 0.6, 0.3, 0.2, 0.42, 0.31, 0.45, 0.21, 0.35, 0.29, 0.71, 0.4, 0.65,
                      0.45]  # 0.31 - small, 0.71 - composition
print("start")
with open('../dataset.json', 'r') as j:  # массив словарей
    json_data = json.load(j)



# #мера близости евклидово расстояние
# print("мера близости евклидово расстояние--------------------------------------------------------------------------------------------------")
# for i in range(len(json_data)):
#     list_mer = []
#     for j in range(len(json_data)):
#         list_mer.append(round(euclid_distance(json_data[i], json_data[j]), 2))
#     print(list_mer)
#
# #косинусная мера близости
# print("\nмера близости косинусная--------------------------------------------------------------------------------------------------")
# for i in range(len(json_data)):
#     list_mer = []
#     for j in range(len(json_data)):
#         list_mer.append(round(cos_distance(json_data[i], json_data[j]), 8))
#     print(list_mer)

# мера половинкина в которой деление на ноль
# print("\nассоциативная мера половинкина--------------------------------------------------------------------------------------------------")
# print(mera_polovinkina(general_nonnull_parameters(json_data[0], json_data[1]), general_null_parameters(json_data[0], json_data[1])))

#print(generalizing_measure(json_data[1], json_data[2], weights_attributes))
#мера близости обобщенная максимум сходства 5.34
print("обобщенная мера близости--------------------------------------------------------------------------------------------------")
for i in range(len(json_data)):
    list_mer = []
    for j in range(len(json_data)):
        list_mer.append(round(generalizing_measure(json_data[i], json_data[j], weights_attributes), 2))
    print(list_mer)

print("мера близости по дереву--------------------------------------------------------------------------------------------------")
for i in range(len(json_data)):
    list_mer = []
    for j in range(len(json_data)):
        list_mer.append(tree_measure(json_data[i], json_data[j]))
    print(list_mer)
