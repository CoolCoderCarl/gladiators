import random
import time

flag_team1 = "RED"
flag_team2 = "BLUE"
teams_members = 6


class Team:
    def __init__(self, flag_team: str, teams_members: int):
        self.flag_team = flag_team
        self.teams_members = teams_members

    def create_teams(self) -> dict:
        team_members_force = [
            random.randint(50, 100) for r in range(self.teams_members)
        ]
        team = {self.flag_team: team_members_force}
        print(f"The {team[self.flag_team]} team at the beginning {team}")
        return team


class Fighting:
    OVER_KILL_MESSAGE = "!!! TOTAL ANNIHILATION !!!"
    WIN_MESSAGE = "TEAM WIN !"
    DRAW_MESSAGE = "DRAW !"

    def fighting(self, team_1: dict, team_2: dict):
        print("OPPONENT TABLE")
        teams_1 = team_1[flag_team1]
        teams_2 = team_2[flag_team2]
        for i in range(0, len(teams_1)):
            print(f"Pair N {i} : {teams_1[i]} {teams_2[i]}")

            time.sleep(0.5)

            if teams_1[i] > teams_2[i]:
                teams_1[i] += teams_2[i]
                teams_2[i] = 0
            elif teams_1[i] < teams_2[i]:
                teams_2[i] += teams_1[i]
                teams_1[i] = 0
            else:
                teams_1[i] = 0
                teams_2[i] = 0

    def result(
        self,
        team_1,
        team_2,
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

        time.sleep(2)

        print(f"The {flag_team1} team after fight {team_1}")
        print(f"The {flag_team2} team after fight {team_2}")

        res_1 = team_1.count(0)
        res_2 = team_2.count(0)

        time.sleep(1)

        print(f"The {flag_team1} team lost {res_1} gladiators")
        print(f"The {flag_team2} team lost {res_2} gladiators")

        if res_1 > res_2:
            print(flag_team2, self.WIN_MESSAGE)
            if res_2 == 0 and res_1 == teams_members:
                print("*" * len(self.OVER_KILL_MESSAGE))
                print(self.OVER_KILL_MESSAGE)
                print("*" * len(self.OVER_KILL_MESSAGE))
        elif res_1 < res_2:
            print(flag_team1, self.WIN_MESSAGE)
            if res_1 == 0 and res_2 == teams_members:
                print("*" * len(self.OVER_KILL_MESSAGE))
                print(self.OVER_KILL_MESSAGE)
                print("*" * len(self.OVER_KILL_MESSAGE))
        else:
            print(self.DRAW_MESSAGE)


if __name__ == "__main__":
    team_1 = Team(flag_team1, teams_members).create_teams()
    team_2 = Team(flag_team2, teams_members).create_teams()

    fig = Fighting()
    fig.fighting(team_1, team_2)
    fig.result(team_1[flag_team1], team_2[flag_team2])
