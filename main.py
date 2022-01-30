import random

# Create commands random

red_team = []
for i in range(6):
    r = random.randint(50, 100)
    red_team.append(r)

red_team.insert(0, 'R')

print('THE RED TEAM AT THE BEGINNING', red_team)

blue_team = []
for i in  range(6):
    b = random.randint(50, 100)
    blue_team.append(b)

blue_team.insert(0, 'B')

print('THE BLUE TEAM AT THE BEGINNING', blue_team)


# Make them fight

def fighting(team_1=[], team_2=[]):
    print('OPPONENT TABLE')
    for i in range(1,len(team_1)):
        print(team_1[i], end=' ')
        print(team_2[i])

        if team_1[i] > team_2[i]:
            team_1[i] += team_2[i]
            team_2[i] = 0
        elif team_1[i] < team_2[i]:
            team_2[i] += team_1[i]
            team_1[i] = 0
        else:
            team_1[i] = 0
            team_2[i] = 0

# Gather results

def result(team_1=[], team_2=[]):

    print('RESULTS')
    if team_1[0] == 'R' and team_2[0] == 'B':
        print('THE RED TEAM', team_1)
        print('THE BLUE TEAM', team_2)

        res_1 = team_1.count(0)
        print('RED',res_1)
        res_2 = team_2.count(0)
        print('BLUE',res_2)

        if res_1 > res_2:
            print('BLUE TEAM WIN !')
        elif res_1 < res_2:
            print('RED TEAM WIN !')
        else:
            print('DRAW !')

    else:
        print('THE RED TEAM', team_2)
        print('THE BLUE TEAM', team_1)

        res_2 = team_2.count(0)
        print('RED TEAM GLADIATORS LOST', res_2)
        res_1 = team_1.count(0)
        print('BLUE TEAM GLADIATORS LOST', res_1)

        if res_1 > res_2:
            print('RED TEAM WIN !')
        elif res_1 < res_2:
            print('BLUE TEAM WIN !')
        else:
            print('DRAW !')

fighting(red_team, blue_team)
result(blue_team, red_team)
