import json
from tkinter import *
from tkinter import ttk
from laba2.proximity_measures import euclid_distance, cos_distance, mera_polovinkina, general_nonnull_parameters, \
    general_null_parameters, generalizing_measure, tree_measure
from laba3.operation_with_obj import add_seed_object, get_recommendation, add_likes_object, get_recommendation_by_likes, \
    add_dislikes_object, get_recommendation_by_likes_and_dislike
from laba4.operation_with_obj import add_filter, get_obj_by_filtres, clean_filter

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

entry = ttk.Entry()#поле ввода
entry.pack(anchor=NW, padx=8, pady=8)
#для затравочного-------------------------------
btn_add_seed = ttk.Button(text="добавить затравочный", command=lambda:add_seed_object(seed_objects, json_data, int(entry.get())))
btn_add_seed.pack(anchor=NW, padx=6, pady=6)

btn_get_res31 = ttk.Button(text="получить рекомендации", command= lambda:print(*get_recommendation(seed_objects, json_data, weights_attributes), sep='\n'))
btn_get_res31.pack(anchor=NW, padx=6, pady=12)

#для лайков------------------------------------------
btn_add_likes = ttk.Button(text="добавить массив лайков", command=lambda:add_likes_object(likes_objects, json_data, entry.get()))
btn_add_likes.pack(anchor=NW, padx=200, pady=6)
btn_add_likes.place(x = 200, y =  20)

btn_get_res32 = ttk.Button(text="получить рекомендации\n по лайкам", command= lambda:print(*get_recommendation_by_likes(likes_objects, json_data, weights_attributes), sep='\n'))
btn_get_res32.pack(anchor=NW, padx=200, pady=12)
btn_get_res32.place(x = 200, y =  70)
#для дизлайков----------------------------
btn_add_dislikes = ttk.Button(text="добавить массив дизлайков", command=lambda:add_dislikes_object(dislike_objects, json_data, entry.get()))
btn_add_dislikes.pack(anchor=NW, padx=400, pady=6)
btn_add_dislikes.place(x = 400, y =  20)

btn_get_res33 = ttk.Button(text="получить рекомендации \n по лайкам и дизлайкам", command= lambda:print(*get_recommendation_by_likes_and_dislike(likes_objects, dislike_objects, json_data, weights_attributes), sep='\n'))
btn_get_res33.pack(anchor=NW, padx=400, pady=12)
btn_get_res33.place(x = 400, y =  70)

#для лабы 4-------------------------------------------------------------------------------------------

entryParam = ttk.Entry(width = 28) #поле ввода
entryParam.place(x = 10, y =  200)
entryParam.insert(0, "введите параметр \n фильтра")

entryVal = ttk.Entry(width = 28) #поле ввода
entryVal.place(x = 250, y =  200)
entryVal.insert(0, "введите значение \n параметра")

btn_add_Filtres = ttk.Button(text="добавить фильтр", command= lambda: add_filter(filtres, entryParam.get(), entryVal.get()))
btn_add_Filtres.pack(anchor=NW, padx=400, pady=12)
btn_add_Filtres.place(x = 0, y =  270)

btn_get_resFiltres = ttk.Button(text="найти  \n по фильтрам", command= lambda:print(*get_obj_by_filtres(filtres, json_data), sep='\n'))
btn_get_resFiltres.pack(anchor=NW, padx=400, pady=12)
btn_get_resFiltres.place(x = 250, y =  270)

btn_clean_filtres = ttk.Button(text="очистить \n фильтры", command= lambda: clean_filter(filtres))
btn_clean_filtres.pack(anchor=NW, padx=400, pady=12)
btn_clean_filtres.place(x = 500, y =  270)


btn_clean_filtres = ttk.Button(text="отфильтровать\n рекомендации из лайков", command= lambda:print(*get_obj_by_filtres(filtres, get_recommendation_by_likes(likes_objects, json_data, weights_attributes)), sep='\n'))
btn_clean_filtres.pack(anchor=NW, padx=400, pady=12)
btn_clean_filtres.place(x = 750, y =  270)

root.mainloop()

