# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def find_capital(T):
    for i in range(len(T)):
        if T[i] == i:
            return i
    

def calculate_distance(T, D, i, capital):
    check = i
    total_distance = 0
    while(1):
        if D[check]!=0:
            return total_distance + D[check]
        else:
            if T[i] == capital:
                return total_distance
            else:
                check = T[i]
                total_distance += 1 
        
def solution(T):
    # write your code in Python 3.6
    capital = find_capital(T)
    distance_matrix = [0]*(len(T))
    for i in range(len(T)):
        distance_matrix[i] = calculate_distance(T, distance_matrix, i, capital)
    
    print (distance_matrix)     
    result_array = [0]*(len(T)-1)
