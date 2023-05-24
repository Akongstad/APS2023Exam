import time

start = time.time()
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

#Recursive solution:
def solve(money_left, time_left, mission_index): 
    if (money_left, time_left, mission_index) in memoization_table: #if key is in dictionary
        #print("used memoization_table")
        return memoization_table[(money_left, time_left, mission_index)] #return value
    
    if mission_index == len(missions): #if no more missions
        return 0 #no people saved

    if money_left < 0 or time_left < 0: #if no more enough money or time
        return 0 #no people saved

    mission_cost, time_spend, people_saved = missions[mission_index] #get mission info
    
    if money_left < mission_cost or time_left < time_spend: #if not enough money or time
        best = solve(money_left, time_left, mission_index + 1) #skip mission
        #print(best)
    else:
        best = max(solve(money_left, time_left, mission_index + 1),
                     solve(money_left-mission_cost, time_left-time_spend, mission_index + 1) + people_saved) #skip mission or do mission
        #print(best)
    
    memoization_table[(money_left, time_left, mission_index)] = best #add key and value to dictionary
    return best #return value

#OUTPUT
print(solve(M, T, 0)) #print answer
end = time.time()
print(end - start, "seconds")