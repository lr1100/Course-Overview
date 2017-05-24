def best(score, names):
    #Initialize Top score
    top_score = [0,""]
    #Go through all names and find their scores
    for name in names:
        name_score = [score(name.lower()),name]
        #If names score is higher than the Top Score, replace Top Score
        if name_score[0] > top_score[0]:
            top_score = name_score
    return top_score

def vowels(name):
    num_vals = 0
    for char in name:
        if char in ['a','e','i','o','u']:
            num_vals += 1
    return num_vals





names = ["Ben", "April", "Zaber", "Alexis", "McJagger", "J.J.", "Madonna"]
print(best(vowels,names))
print(best(lambda x: x.count('a'), names))
