#INPUT
M, T, N = map(int, input().split()) #money, time, number of missions
#print(M, T, N)

missions = [] #list of tuples (cost, time, people_saved)

for _ in range(N): #for each mission
    m, t, r = map(int, input().split()) #cost, time, people_saved
    missions.append((m, t, r)) #add tuple to list
#print(missions)

#SOLUTION
memoization_table = {} #dictionary with keys (money_left, time_left, mission_index) and values most number of people saved

#Iterative solution:


#OUTPUT
