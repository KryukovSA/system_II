from statistics import mean

from laba3.proximity_measures import generalizing_measure
from operator import itemgetter
import re

def create_reccomend_by_keys(recommend_ids, all_objects):
    result = []
    for key in recommend_ids:
        result.append(all_objects[int(key)])
    return result

def get_recommendation(seed_objects, all_objects, weights_attributes): #для п 3.1
    recommendations = {}
    for i in range(len(all_objects)):
        for j in range(len(seed_objects)):
            if i != seed_objects[j]['id']:
                recommendations[i] = generalizing_measure(seed_objects[j], all_objects[i], weights_attributes)
    recommendations = dict(sorted(recommendations.items(), key=itemgetter(1)))
    return create_reccomend_by_keys(reversed(recommendations), all_objects)

def add_seed_object(seed_objects, all_objects, obj_index):
    seed_objects.append(all_objects[int(obj_index)])


def add_likes_object(likes_objects, all_objects, obj_indexes):
    i=0
    while i < len(obj_indexes):
        tmp_str = ''
        if(obj_indexes[i] == ','):
            i+=1
            continue
        while obj_indexes[i] != ',':
            tmp_str+=obj_indexes[i]
            i+=1
            print(i, "---------------------------------------------------")
            if i >= len(obj_indexes):
                break
        print(tmp_str)
        likes_objects.append(all_objects[int(tmp_str)])


def get_recommendation_by_likes(likes_objects, all_objects, weights_attributes): #для п 3.2
    recommendations = {}
    for i in range(len(all_objects)):
        for j in range(len(likes_objects)):
            if i != likes_objects[j]['id']:
                if(generalizing_measure(likes_objects[j], all_objects[i], weights_attributes) > 2): #показатель похожести на лайк
                    recommendations[i] = generalizing_measure(likes_objects[j], all_objects[i], weights_attributes)
    recommendations = dict(sorted(recommendations.items(), key=itemgetter(1)))
    return create_reccomend_by_keys(reversed(recommendations), all_objects)


def add_dislikes_object(dislikes_objects, all_objects, obj_indexes):
    i=0
    while i < len(obj_indexes):
        tmp_str = ''
        if(obj_indexes[i] == ','):
            i+=1
            continue
        while obj_indexes[i] != ',':
            tmp_str+=obj_indexes[i]
            i+=1
            print(i, "---------------------------------------------------")
            if i >= len(obj_indexes):
                break
        print(tmp_str)
        dislikes_objects.append(all_objects[int(tmp_str)])


def get_recommendation_by_likes_and_dislike(likes_objects, dislikes_objects, all_objects, weights_attributes): #для п 3.3
    recommendations = {}
    no_recommendation = {}
    for i in range(len(all_objects)):
        for j in range(len(likes_objects)):
            if i != likes_objects[j]['id']:
                if(generalizing_measure(likes_objects[j], all_objects[i], weights_attributes) > 2): #показатель похожести на лайк
                    recommendations[i] = generalizing_measure(likes_objects[j], all_objects[i], weights_attributes)
        for k in range(len(dislikes_objects)):
            if i != dislikes_objects[k]['id']:
                if (generalizing_measure(dislikes_objects[k], all_objects[i],
                                         weights_attributes) > 2):  # показатель похожести на дизлайк
                    no_recommendation[i] = generalizing_measure(dislikes_objects[k], all_objects[i], weights_attributes)

    for key in list(recommendations):
        for key1 in list(no_recommendation):
            if(key == key1):
                del recommendations[key]

    recommendations = dict(sorted(recommendations.items(), key=itemgetter(1)))
    return create_reccomend_by_keys(reversed(recommendations), all_objects)


def add_filter(filtres, key, value):
    filtres[key] = value
    print(filtres)

def clean_filter(filtres):
    filtres.clear()
    print("фильтры очищены")

def get_obj_by_filtres(filtres, all_objects):
    result = []

    for j in range(len(all_objects)):
        counter = 0 #количество удовлетворяющих фильтров
        for key1 in all_objects[j]:
            for key in filtres:
                if key == key1 and filtres[key] == all_objects[j][key1]:
                    counter+=1
                if(counter == len(filtres)):
                    result.append(all_objects[j])
                    counter = 0

    if(result == [] and len(filtres) > 1):#для пункта 4.2 тогда хотябы по одному фильтру из двух поищу
        print("Возможно вас заинтересует\n")
        for j in range(len(all_objects)):
            counter = 0  # количество удовлетворяющих фильтров
            for key1 in all_objects[j]:
                for key in filtres:
                    if key == key1 and filtres[key] == all_objects[j][key1]:
                        counter += 1
                    if (counter == len(filtres) - 1):
                        result.append(all_objects[j])
                        counter = 0

    if(result == []):
        print("в фильтре некорректны значения и(или) параметры\n")

    return result

#вывести средства которые не принадлежат определенному типу определенной группы например дезодоранты кроме axe
def exclude(param, value, all_objects):
    result = []
    for i in range(len(all_objects)):
        if all_objects[i][param] != value:
            result.append(all_objects[i])
    return result

def without_marks(group, all_objects):
    result = []
    value = ''
    if group == "езодорант": value = 'deodorant'
    if group == "нтиперсперант": value = 'antiperspirant'
    if group == "салф": value = 'deodorizing wipes'
    for i in range(len(all_objects)):
        if all_objects[i]['group'] == value and all_objects[i]['marks on clothes'] == "no":
            result.append(all_objects[i])
    return result


def with_fruit(group, all_objects):
    result = []
    if group == "езодорант": value = 'deodorant'
    if group == "нтиперсперант": value = 'antiperspirant'
    for i in range(len(all_objects)):
        if all_objects[i]['group'] == value and all_objects[i]['small']["viev"] == 'fruit':
            result.append(all_objects[i])
    return result




currentBrand = ''
flag_without_marks = 0
flag_with_fruit = 0
answer = []
#для лабы 6----------------------------------------
def get_answer(question, all_objects):
    global answer
    global flag_without_marks
    global flag_with_fruit
    brandList = ['rexona', 'axe', 'dove', 'nivea', 'fa', 'garnier', 'adidas', 'old spice']
    group_list = ["езодорант", "нтиперсперант", "салф"]
    global currentBrand
    for i in range(len(all_objects)):
        if(question.find("производитель " + all_objects[i]['brand']) != -1): #в 8 9 10---------------------------------------------------------
            print("Вам нужна защита от пота или от запаха от производителя " , all_objects[i]['brand'], "?")
            currentBrand = all_objects[i]['brand']
            break
        # else:
        #     print("такого производителя нет, но может заинтересуют другие? Защита от пота или от запаха вам нужна?")

    if (question.find("от пота") != -1):  # в 8 9 10
        answer = []
        if flag_with_fruit == 1:
            answer1 = with_fruit("нтиперсперант", all_objects)
            flag_with_fruit = 0
            answer = answer1
            print("подобрали средства с запахом фруктов")
            return answer
        if flag_without_marks == 1:
            answer1 = without_marks("нтиперсперант", all_objects)
            flag_without_marks = 0
            answer = answer1
            return answer
        answer.append('посмотрите эти средства')
        answer = answer + (get_obj_by_filtres({'brand' : currentBrand,'group': "antiperspirant"}, all_objects))
        return answer
    if (question.find("от запаха") != -1):  # в 8 9 10
        answer = []
        if flag_with_fruit == 1:
            answer1 = with_fruit("езодорант", all_objects)
            flag_with_fruit = 0
            answer = answer1
            print("подобрали средства с запахом фруктов")
            return answer
        if flag_without_marks == 1:
            answer1 = without_marks("езодорант", all_objects)
            flag_without_marks = 0
            answer = answer1
            return answer
        answer.append('посмотрите эти средства')
        answer = answer + (get_obj_by_filtres({'brand': currentBrand, 'group': "deodorant"}, all_objects))
        return answer
    #### 8 9 10 end----------------------------------------------------------------------------------------------------------------

    re11_13 = r'[{А|а}нтиперсперант | {Д|д}езодорант] производителя .* заменить'
    if(re.search(re11_13, question) != None):
        answer = []
        if question.find("нтиперсперант") != -1:
            for i in range(len(brandList)):
                if question.find(brandList[i]) != -1:
                    answer += exclude('brand', brandList[i], all_objects)
            answer1 = []
            for j in range(len(answer)):
                if answer[j]["group"] == "antiperspirant": answer1.append(answer[j])
            print("можете посмотреть эти варианты")
            return answer1
        if question.find("езодорант") != -1:
            for i in range(len(brandList)):
                if question.find(brandList[i]) != -1:
                    answer += exclude('brand', brandList[i], all_objects)
            answer1 = []
            for j in range(len(answer)):
                if answer[j]["group"] == "deodorant": answer1.append(answer[j])
            answer = answer1
            print("можете посмотреть эти варианты")
            return answer

    re12 = r'[производитель|производителя] .* лучше .* или'
    if (re.search(re12, question) != None):
        brand1 = ''
        brand2 = ''
        for i in brandList:
            if(question.find(i))!= -1:
                brand1 = i
        for i in brandList:
            if (question.find(i) != -1 and i != brand1):
                brand2 = i
        raiting1 = []
        raiting2 = []
        for i in range(len(all_objects)):
            if(all_objects[i]['brand'] == brand1):
                raiting1.append(all_objects[i]["raiting"])
            if (all_objects[i]['brand'] == brand2):
                raiting2.append(all_objects[i]["raiting"])

        print('средняя оценка бренда ', brand1, "равна", round(mean(raiting1),3))
        print('средняя оценка бренда ', brand2, "равна", round(mean(raiting2),3))


    re18_19_20 = r'[появил|остав|остат|остал] .* пятн|след'
    if (re.search(re18_19_20, question) != None):
        answer = []
        for i in group_list:
            if (question.find(i) != -1):
                answer = without_marks(i, all_objects)
                return answer
        flag_without_marks = 1
        print("Это было средство защищающее от пота или от запаха?")




    redelete = r'[убери | мне не нужны] [aнтиперсперанты | дезодоранты]'
    if (re.search(redelete, question) != None):
        if question.find("нтиперсперант") != -1:
            answer1 = []
            for i in range(len(answer)):
                if(answer[i]['group'] != "antiperspirant"):
                    answer1.append(answer[i])
            answer = answer1
            return answer

        if question.find("езодорант") != -1:
            answer1 = []
            for i in range(len(answer)):
                if (answer[i]['group'] != "deodorant"):
                    answer1.append(answer[i])
            answer = answer1
            return answer

    re1 = r'{покажи|выведи|пердставь} {весь|всю|полностью|имеющиеся} {каталог|ассортимент|продукцию}'
    if (re.search(re1, question) != None):
        print("показываю весь имеющийся товар")
        answer = all_objects
        return answer

    re24_25 = r"[недорог|дешев] .*[запах|запаха] .* подмыш"
    if (re.search(re24_25, question) != None):
        print("введите трехзначый верхний порог цены")



    re11 = r'[[люблю | нравится | предпоч].*фруктов|фруктовый]'#|[с .* фркут]
    if (re.search(re11, question) != None):
        print("Вам нужна защита от пота, или запаха пота, или духи?")
        flag_with_fruit = 1


    re_price = r'^[1-9][0-9][0-9]$'
    if (re.search(re_price, question) != None):
        print("подобрали средства от запаха стоимостью до ", question)
        for i in range(len(all_objects)):
            if all_objects[i]['group'] == 'deodorant' and all_objects[i]['price'] < int(question):
                answer.append(all_objects[i])
        return answer



    return []





















