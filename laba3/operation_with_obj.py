from laba3.proximity_measures import generalizing_measure
from operator import itemgetter

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