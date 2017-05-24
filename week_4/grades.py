def weighted_averages(grades, weights):
    wa = 0
    try:
        for i in range(len(grades)):
            #Check for valid grades and weights
            if grades[i] < 0 or grades[i] > 100:
                raise Exception("Error: Invalid grade")
            elif sum(weights) != 100:
                raise Exception("Error: Weights don't add up to 100")
            else:
                wa += grades[i] * weights[i]
        return wa/sum(weights)

    except IndexError:
        print("Error: Grade list and weight list are different sizes")
    except Exception as e:
        print(e)





def main():
    grades1 = [88,99,100,70]
    weights1 = [30, 30, 30, 5]
    grades2 = [78, 75, 80, 99]
    weights2 = [110, 10, -20]

    print(weighted_averages(grades1,weights1))
    print(weighted_averages(grades2,weights2))

if __name__ == "__main__":
    main()
