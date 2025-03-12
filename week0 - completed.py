
# week 0 problem 1
# create a function that returns a list of (vitamins,injections) tuples for each attribute that they need.
# Complete problem statement in README.mds


# your input type should be a list,
# output should also be a list containing tuples
# Example:
# input: [250, 0, 250, 0, 0, 0]
# expected output: [(25,0),(0,0),(25,0),(0,0),(0,0),(0,0)]
# input: [500, 1, 2, 3, 4, 5]
#expected output: "No medicine given"
# HINT: using % operator to find remainder may be helpful

 def medicine_needed(patient_needs):
    if sum(patient_needs) > 500 or any(need > 250 for need in patient_needs):
        return 'No medicine given'
    vitamins_injections = []
    for need in patient_needs:
        vitamins = need // 10
        injections = need % 10
        if injections > 0:
            vitamins += 1
            injections = 10 - injections
        vitamins_injections.append((vitamins, injections))
    return vitamins_injections

print(medicine_needed([250, 0, 250, 0, 0, 0]))

print(medicine_needed([223, 12, 126, 0, 37, 12]))

print(medicine_needed([500, 1, 2, 3, 4, 5]))

print(medicine_needed([260, 1, 2, 3, 4, 5]))

# print(dose([250, 0, 250, 0, 0, 0]))
    #YOUR SOLUTION ENDS HERE

