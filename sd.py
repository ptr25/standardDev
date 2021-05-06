
import math
import statistics


# list of elements to calculate mean
import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]
#file_data[[60,61,65,63,98,99,90,95,91,96]]
# data=[60,61,65,63,98,99,90,95,91,96]

# finding mean
def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean



# squaring and getting the values
squared_list= []
for number in data:
    #calling the function mean and passing data
    a = int(number) - mean(data)
    #a**2 squares it
    a= a**2
    squared_list.append(a)

#getting sum of all those squares
sum =0
for i in squared_list:
    sum =sum + i

#dividing the sum by the total values
result = sum/ len(data)

# getting the deviation by taking square root of the result
std_deviation = math.sqrt(result)
print(std_deviation)
#print("derived using predefined function ", statistics.stdev(data))