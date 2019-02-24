def find_capital(T):
    for i in range(len(T)):
        if T[i] == i:
            return i


def calculate_distance(T, D, i, capital):
    check = i
    total_distance = 0
    print "in function"
    while (1):
        if D[check] != 0:
            print "here"
            return total_distance + D[check]
        else:
            print "there"
            print T[check]
            if T[check] == capital:
                return total_distance +1
            else:
                check = T[check]
                total_distance += 1


def solution(T):
    # write your code in Python 3.6
    capital = find_capital(T)
    distance_matrix = [0] * (len(T))
    # distance_matrix[0] = calculate_distance(T, distance_matrix, 0, capital)
    for i in range(len(T)):
        distance_matrix[i] = calculate_distance(T, distance_matrix, i, capital)

    print (distance_matrix)
    result_array = [0] * (len(T))

    for i in range(len(distance_matrix)):
        result_array[distance_matrix[i]] +=1
    print (result_array[1:])
T = [9,1,4,9,0,4,8,9,0,1]
solution(T)
