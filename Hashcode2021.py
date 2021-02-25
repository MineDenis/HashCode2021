from random import randint
from pprint import pprint

streets_data = {}
inters = 0
sim_time, intersecs, streets, cars, score_awarded = 0, 0, 0, 0, 0
count = 0
carroutes = {}

filename = 'a.txt'

def cars_expected_at_street(streetname):
    amount = 0;
    for i, data in carroutes.items():
        if streetname in data['Route']:
            amount += 1;
    return amount + int(streets_data[streetname]['TimeTaken'])
# secondsInCycle * streetToCount.second / totalNumberOfCars + 1
# simtime / amount of cars
def howmanystreetscometo(intersectionID):
    streetsarr = []
    for item, data in streets_data.items():
        if int(data['EndIntersection']) == intersectionID:
            streetsarr.append(item)
    return streetsarr

# cars amt + 1 if theres one already there
def construct_data():
    with open("../inputs/" + filename, 'r') as f:
        line1 = f.readline().strip().split()

        sim_time, intersecs, streets, cars, score_awarded = int(line1[0]), int(line1[1]), int(line1[2]), int(line1[3]), int(line1[4])
        #print('Simulation Time: {}\nIntersections: {}\nStreets: {}\nCars: {}\nScore for reaching dest: {}'.format(sim_time, intersecs, streets, cars, score_awarded))
        
        for i in range(0, streets):
            line = f.readline().split()
            streets_data[line[2]] = {'StartIntersection': line[0], 'EndIntersection': line[1], 'TimeTaken': line[3]}

        for i in range(0, cars):
            # Each car begins at the END of the FIRST ROAD in 'Route'
            line = f.readline().split()
            carroutes[i] = {'RoadsToTravel:': line[0], 'Route': line[1:]}

    pprint(streets_data)
    #print()
    #print()
    pprint(carroutes)
    #print()
    #print()
    # Constructing the schedule
    #print('SCHEDULE:')
    #print('Amount of intersections to schedule for:', intersecs - 1)
    with open("../outputs/submission_" + filename, "w") as newfile:
        newfile.write(str(intersecs - 1) + '\n')
        for intersection in range(0, intersecs - 1):
            streets_arriving = howmanystreetscometo(intersection)
            #print('Intersection ID:', intersection)
            newfile.write(str(intersection) + '\n')
            newfile.write(str(len(streets_arriving)) + '\n')#, 'streets come to this intersection.')
            for each_street in streets_arriving:
                #print(each_street, cars_expected_at_street(each_street))
                #newfile.write(str(each_street + ' ' + str(randint(15, 30))) + '\n')
                newfile.write(str(each_street + ' ' + str(cars_expected_at_street(each_street)) + '\n'))
                #newfile.write(str(each_street + ' ' + str(sim_time) + '\n'))

def main():
    construct_data()

if __name__ == '__main__':
    main()
