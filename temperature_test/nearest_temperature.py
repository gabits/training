def find_nearest_temperature(temperatures, number):
    if number in temperatures:
        return number
    elif number > max(temperatures):
        return max(temperatures)
    elif number < min(temperatures):
        return min(temperatures)
    else:
        temperatures.sort()
        for index in range(len(temperatures)):
            if number > temperatures[index]:
                pass
            else:
                avg_comparison = (temperatures[index] + temperatures[index - 1]) / 2
                if number == avg_comparison or number > avg_comparison:
                    return temperatures[index]
                else:
                    return temperatures[index - 1]
