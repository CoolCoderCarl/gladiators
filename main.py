import time
import random

# Create teams with random power

red_team = []
blue_team = []
teams_members = 6

def create_teams(teams_members = teams_members):
    if teams_members <= 0:
        print('Nothing to think about. Everyone sleep')
        exit()
    else:
        global red_team
        red_team = [random.randint(50, 100) for r in range(teams_members)]
        red_team.insert(0, 'R')
        print('The RED team at the beginning', red_team)

        global blue_team
        blue_team = [random.randint(50, 100) for b in range(teams_members)]
        blue_team.insert(0, 'B')
        print('The BLUE team at the beginning', blue_team)

# Make them fight

def fighting(team_1=[], team_2=[]):

    print('OPPONENT TABLE')
    for i in range(1, len(team_1)):
        print(team_1[i], end=' ')
        print(team_2[i])

        time.sleep(0.5)

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

def result(team_1=[], team_2=[], teams_members = teams_members):

    results = 'FINAL SCORE'
    print('*' * len(results))
    print(results)
    print('*' * len(results))

    over_kill_message = '!!! TOTAL ANNIHILATION !!!'

    time.sleep(2)

    if team_1[0] == 'R' and team_2[0] == 'B':
        print('The RED team after fight', team_1)
        print('The BLUE team after fight', team_2)

        res_1 = team_1.count(0)
        res_2 = team_2.count(0)

        time.sleep(1)

        print('The RED team lost', res_1, 'gladiators')
        print('The BLUE team lost', res_2, 'gladiators')

        if res_1 > res_2:
            print('BLUE TEAM WIN !')
            if res_2 == 0 and res_1 == teams_members:
                print('*' * len(over_kill_message))
                print(over_kill_message)
                print('*' * len(over_kill_message))
        elif res_1 < res_2:
            print('RED TEAM WIN !')
            if res_1 == 0 and res_2 == teams_members:
                print('*' * len(over_kill_message))
                print(over_kill_message)
                print('*' * len(over_kill_message))
        else:
            print('DRAW !')

    else:
        print('The RED team after fight', team_2)
        print('The BLUE team after fight', team_1)

        res_2 = team_2.count(0)
        res_1 = team_1.count(0)

        time.sleep(1)

        print('The RED team lost', res_2, 'gladiators')
        print('The BLUE team lost', res_1, 'gladiators')

        if res_1 > res_2:
            print('RED TEAM WIN !')
            if res_2 == 0 and res_1 == teams_members:
                print('*' * len(over_kill_message))
                print(over_kill_message)
                print('*' * len(over_kill_message))
        elif res_1 < res_2:
            print('BLUE TEAM WIN !')
            if res_1 == 0 and res_2 == teams_members:
                print('*' * len(over_kill_message))
                print(over_kill_message)
                print('*' * len(over_kill_message))
        else:
            print('DRAW !')

create_teams(teams_members)
fighting(blue_team, red_team)
result(red_team, blue_team, teams_members)
