import random
import time

flag_team1 = "RED"
flag_team2 = "BLUE"
teams_members = 6


def create_teams(flag_team: str, teams_members=teams_members) -> list:
    """
    Create teams with random power
    :param flag_team:
    :param teams_members:
    :return:
    """
    if teams_members <= 0:
        print("Nothing to think about. Everyone sleep")
        exit()
    else:
        team = [random.randint(50, 100) for r in range(teams_members)]
        team.insert(0, flag_team)
        print(f"The {flag_team} team at the beginning {team}")

        return team


def fighting(team_1=[], team_2=[]):
    """
    Make the teams fight each other
    :param team_1:
    :param team_2:
    :return:
    """
    print("OPPONENT TABLE")
    for i in range(1, len(team_1)):
        print(f"Pair N {i} : {team_1[i]} {team_2[i]}")

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


def result(
    team_1=[],
    team_2=[],
    teams_members=teams_members,
    flag_team1=flag_team1,
    flag_team2=flag_team2,
):
    """
    Gather and show results
    :param team_1:
    :param team_2:
    :param teams_members:
    :param flag_team1:
    :param flag_team2:
    :return:
    """
    results = "FINAL SCORE"
    print("*" * len(results))
    print(results)
    print("*" * len(results))

    over_kill_message = "!!! TOTAL ANNIHILATION !!!"

    time.sleep(2)

    if team_1[0] == flag_team1 and team_2[0] == flag_team2:
        print(f"The {flag_team1} team after fight {team_1}")
        print(f"The {flag_team2} team after fight {team_2}")

        res_1 = team_1.count(0)
        res_2 = team_2.count(0)

        time.sleep(1)

        print(f"The {flag_team1} team lost {res_1} gladiators")
        print(f"The {flag_team2} team lost {res_2} gladiators")

        if res_1 > res_2:
            print(f"{flag_team2} TEAM WIN !")
            if res_2 == 0 and res_1 == teams_members:
                print("*" * len(over_kill_message))
                print(over_kill_message)
                print("*" * len(over_kill_message))
        elif res_1 < res_2:
            print(flag_team1, "TEAM WIN !")
            if res_1 == 0 and res_2 == teams_members:
                print("*" * len(over_kill_message))
                print(over_kill_message)
                print("*" * len(over_kill_message))
        else:
            print("DRAW !")

    else:
        print(f"The {flag_team2} team after fight {team_2}")
        print(f"The {flag_team1} team after fight {team_1}")

        res_2 = team_2.count(0)
        res_1 = team_1.count(0)

        time.sleep(1)

        print(f"The {flag_team2} team lost {res_2} gladiators")
        print(f"The {flag_team1} team lost {res_1} gladiators")

        if res_1 > res_2:
            print(f"{flag_team2} TEAM WIN !")
            if res_2 == 0 and res_1 == teams_members:
                print("*" * len(over_kill_message))
                print(over_kill_message)
                print("*" * len(over_kill_message))
        elif res_1 < res_2:
            print(f"{flag_team1} TEAM WIN !")
            if res_1 == 0 and res_2 == teams_members:
                print("*" * len(over_kill_message))
                print(over_kill_message)
                print("*" * len(over_kill_message))
        else:
            print("DRAW !")


if __name__ == "__main__":
    team_1 = create_teams(flag_team1, teams_members)
    team_2 = create_teams(flag_team2, teams_members)

    fighting(team_1, team_2)
    result(team_1, team_2, teams_members, flag_team1, flag_team2)
