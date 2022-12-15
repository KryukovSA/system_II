import json
from tkinter import *
from tkinter import ttk
from laba2.proximity_measures import euclid_distance, cos_distance, mera_polovinkina, general_nonnull_parameters, \
    general_null_parameters, generalizing_measure, tree_measure
from laba3.operation_with_obj import add_seed_object, get_recommendation, add_likes_object, get_recommendation_by_likes, \
    add_dislikes_object, get_recommendation_by_likes_and_dislike
from laba4.operation_with_obj import add_filter, get_obj_by_filtres, clean_filter
from laba6.operation_with_obj import get_answer

seed_objects = [] #список затравочных объектов
likes_objects = [] #список лайков
dislike_objects = [] #список дизлайков
filtres = {} #словарь фильтров

m = 14  # количество полей объекта
# веса признаков
weights_attributes = [0, 0.6, 0.9, 0.2, 0.8, 0.31, 0.45, 0.21, 0.35, 0.29, 0.71, 0.4, 0.65,
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

# print("мера близости по дереву--------------------------------------------------------------------------------------------------")
# for i in range(len(json_data)):
#     list_mer = []
#     for j in range(len(json_data)):
#         list_mer.append(tree_measure(json_data[i], json_data[j]))
#     print(list_mer)














#работа с интерфейсом----------------------------------------
root = Tk()
root.title("laba3")
root.geometry("1500x800")


#для лабы 6-------------------------------------------------------------------------------------------

entryQuestion = ttk.Entry(width = 200) #поле ввода
entryQuestion.place(x = 10, y =  20)
entryQuestion.insert(0, "введите вопрос")

btn_get_Answer = ttk.Button(text="отправить", command= lambda: print(*get_answer(entryQuestion.get(), json_data), sep='\n'))
btn_get_Answer.pack(anchor=NW, padx=400, pady=12)
btn_get_Answer.place(x = 10, y =  100)


root.mainloop()

