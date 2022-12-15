import numpy as np
from numpy import dot
from numpy.linalg import norm


def mera_polovinkina(U_AB, R_AB):
    return U_AB / R_AB


def general_nonnull_parameters(obj_A, obj_B):
    counter = 0
    if (('viev' in obj_A['small']) and ('viev' in obj_B['small'])):
        counter += 1
    print(counter)
    if (('marks on clothes' in obj_A) and ('marks on clothes' in obj_B)):
        counter += 1
        print(counter + 21)
    return counter


def general_null_parameters(obj_A, obj_B):  # для придачи смысла можем просто написать ключ которого
    counter = 0  # нет впринципе - этот параметр как раз и будет общим отсутствующим
    if (('viev' not in obj_A['small']) and ('viev' not in obj_B['small'])):
        counter += 1
    if (('marks on clothes' not in obj_A) and ('marks on clothes' not in obj_B)):
        counter += 1
    return counter


def euclid_distance(obj_A, obj_B):
    vecA = []
    vecB = []
    vecA.append(obj_A['price'])
    vecA.append(obj_A['raiting'])
    vecB.append(obj_B['price'])
    vecB.append(obj_B['raiting'])
    return norm(np.array(vecA) - np.array(vecB))


def cos_distance(obj_A, obj_B):
    vecA = []
    vecB = []
    vecA.append(obj_A['price'])
    vecA.append(obj_A['raiting'])
    vecB.append(obj_B['price'])
    vecB.append(obj_B['raiting'])
    cos_sim = dot(vecA, vecB) / (norm(vecA) * norm(vecB))
    return cos_sim


def tree_measure(obj_A, obj_B):
    tree_measure = 0
    if (obj_A["group"] == obj_B["group"] and obj_A["group"] == 'deodorizing wipes'):
        tree_measure = 0
        return tree_measure

    if(obj_A["group"] != obj_B["group"]):
        if(obj_A["group"] != 'deodorizing wipes' and obj_B["group"]!= 'deodorizing wipes'):
            tree_measure = 8
            return tree_measure
        else: #один из объектов - салфетки
            tree_measure = 5
            return tree_measure
    elif(obj_A["degree of sweating"] != obj_B["degree of sweating"]):
        tree_measure = 6
        return tree_measure
    elif (obj_A["type"] != obj_B["type"]):
        tree_measure = 4
        return tree_measure
    elif (obj_A['small']["viev"] != obj_B['small']["viev"]):
        tree_measure = 2
        return tree_measure
    else:
        tree_measure = 0
        return tree_measure

def generalizing_measure(obj_A, obj_B, weights):
    similarity = 0 #мера схожести
    # current_len = 0
    # if len(obj_A) > len(obj_B) or len(obj_A) == len(obj_B):
    #     current_len = len(obj_A)
    # else:
    #     current_len = len(obj_B)
    counter = 0
    for key in obj_A:
        if(obj_A[key] == obj_B[key]):
            similarity += weights[counter];
        counter+=1
        if(key == 'small'):
            for key1 in obj_A[key]:
                if(obj_A[key][key1] == obj_B[key][key1]):
                    similarity += weights[counter];
                #print(obj_A[key][key1] , "  " , weights[counter])
                counter+=1
    return similarity