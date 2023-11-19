from collections import Counter
print('Enter the number of gametypes !')
num_of_gametypes = int(input())
games_count = [0] * num_of_gametypes


for i in range(num_of_gametypes):
    print('Enter the count of game ' + str(i + 1))
    var = input()
    games_count[int(i)] = var

print('Enter the number of bags !')
num_of_bags = int(input())


total_games = 0

for i in games_count:
    total_games = int(total_games) + int(i)


maximum_games = int(total_games / num_of_bags)

print(int(maximum_games))

if total_games % num_of_gametypes > 0:
    maximum_games = maximum_games + 1

rows, columns = num_of_bags, maximum_games
bags = [[0 for i in range(columns)] for j in range(rows)]

currentbag = 0
bag_size = [0] * num_of_bags

for x in range(len(games_count)):
    for j in range(int(games_count[x])):
        if currentbag >= num_of_bags:
            currentbag = 0
        placeholder = bag_size[currentbag]
        bags[currentbag][placeholder] = ('G' + str(x + 1))
        bag_size[currentbag] = bag_size[currentbag] + 1

        currentbag = currentbag + 1


for c in range(num_of_bags):
    print('Wundertüte '+ str(c + 1) +' ist ' , end='')
    for d in range(bag_size[c]):
        a = dict(Counter(bags[c]))
    print(a)

