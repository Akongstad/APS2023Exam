#! /usr/env/python3

''''''
def max_rescue_people(missions, funds, time):
    # Create a memoization table to store the maximum number of people
    # that can be rescued for different subproblems
    memo = [[None] * (time + 1) for _ in range(funds + 1)]
    
    # Recursive helper function
    def max_rescue_helper(miss_len, funds, time):
        #print(missions)
        #print(miss_len)
        # Base case: if no missions or no funds or no time left, no people can be rescued
        if miss_len == 0 or funds == 0 or time == 0:
            return 0
        
        # If the result is already computed, return it from the memo table
        if memo[funds][time] is not None:
            return memo[funds][time]
        
        # Get the details of the current mission
        mission_cost, mission_time, mission_people = missions[miss_len-1]
        
        # If the current mission's cost or time exceeds the available funds or time,
        # move to the next mission
        if mission_cost > funds or mission_time > time:
            result = max_rescue_helper(miss_len-1, funds, time)
        else:
            # Recursively explore both the cases:
            # 1. Taking the current mission and reducing funds and time accordingly
            # 2. Not taking the current mission and moving to the next mission
            result = max(
                mission_people + max_rescue_helper(miss_len-1, funds - mission_cost, time - mission_time),
                max_rescue_helper(miss_len-1, funds, time)
            )
        
        # Store the result in the memo table for future reference
        memo[funds][time] = result
        
        return result
    
    # Call the recursive helper function
    return max_rescue_helper(len(missions), funds, time)


# Read the input values
M, T, N = map(int, input().split(' '))
missions = []
for _ in range(N):
    m, t, r = map(int, input().split(' '))
    missions.append((m, t, r))

# Call the function and print the result
max_people_rescued = max_rescue_people(missions, M, T)
print(max_people_rescued)
     
