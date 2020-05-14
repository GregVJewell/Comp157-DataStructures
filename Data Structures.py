# Written by Greg Jewell
# Problem 8:
# a) stack
# b) list
# c) priority queue
# d) queue
# e) dictionary

import csv
import time

# Really effective data structure!
def dictionary():
    print("-------------------------Using a map to search!-------------------------")
    dictStart = time.time()
    populations = open("populations.csv", "r")
    if populations.mode == "r":
        reader = csv.reader(populations)
        poplist = {}
        for city, row in reader:
            poplist[city] = row

    query = open("queries.txt", "r")
    if query.mode == "r":
        queries = query.readlines()

    for x in queries:
        print(poplist[x.strip('\n')])

    populations.close()
    query.close()

    dictStop = time.time()
    global time1
    time1 = dictStop - dictStart

# Really ineffective data structure!
def popList():
    print("\n-------------------------Using a list to search!-------------------------\n")
    listStart = time.time()

    city = []
    population = []

    with open('populations.csv') as csvDataFile:
        reader = csv.reader(csvDataFile)
        for row in reader:
            city.append(row[0])
            population.append(row[1])

    with open("queries.txt") as queries:
        query = queries.read().splitlines()

    for y in range(len(query)):
        for i in range(len(city)):
            if city[i] == query[y]:
                print(population[i])

    listStop = time.time()
    global time2
    time2 = listStop - listStart


def main():
    dictionary()
    popList()

    print("\nDictionary Time: ", time1)
    print("\nList Time: ", time2)

main()