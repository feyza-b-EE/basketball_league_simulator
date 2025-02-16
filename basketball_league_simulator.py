# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 17:42:15 2024

@author: Feyza
"""
my_name = "Ayse Feyza Birer"
my_id = "220102002033"
my_email = "a.birer2022@gtu.edu.tr"


import random


def _read_file(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file]
    
teams_data = _read_file("teams.txt")
team_name = teams_data[0]
     
managers_data = _read_file("managers.txt")
manager_name = managers_data[0].split()[0]  
manager_last_name = managers_data[0].split()[1] 

players_data = _read_file("players.txt")
player_name = players_data[0].split()[0]  
player_last_name = players_data[0].split()[1] 


class Person:
    def __init__(self, name, last_name):
        self.name = name 
        self.last_name = last_name
        
    def get_name(self):
        return self.name + " " + self.last_name
    
    def __str__(self):
        return self.name + " " + self.last_name
    
    def __lt__(self, other):
        if self.last_name == other.last_name:
            return self.name < other.name
        else:
            return self.last_name < other.last_name
    
    
class Player(Person):
    player_id = 0

    def __init__(self, player_name, player_last_name):
        super().__init__(player_name, player_last_name)
        Player.player_id += 1
        self.id = Player.player_id
        self.shooting_pwr = random.randint(3, 9)
        self.points = 0
        self.points_list = []

    def get_power(self):
        return self.shooting_pwr
    
    def reset(self):
        self.points = 0
        self.points_list = []   
        
    def get_id(self):
        return self.id  
        
    def set_team(self, team):
        self.team = team
        
    def get_team(self):
        return self.team
    
    def add_to_points(self, x):
        self.points_list.append(x)
        self.points += x  
        
    def get_points_detailed(self):
        return self.points_list
        
    def get_points(self):
        return self.points

    def __lt__(self, other):
        if self.points == other.points:
            if self.last_name == other.last_name:
                return self.name < other.name
            else:
                return self.last_name < other.last_name
        else:
            return self.points < other.points
        
class Manager(Person):
    manager_id = 0
    def __init__(self, manager_name, manager_last_name):
        self.name = manager_name 
        self.last_name = manager_last_name
        Manager.manager_id += 1
        self.id = Manager.manager_id
        self.influence_list = []
        self.influence_points = 0
        
    def reset(self):
        self.influence_points = 0
        self.influence_list = []
        
    def get_id(self):
        return self.id
    
    def set_team(self, team):
        self.team = team

    def get_team(self):
        return self.team
    
    def get_influence_detailed(self):
        return self.influence_list
        
    def get_influence(self):
        return self.influence_points
    
    def __lt__(self, other):
        if self.influence_points == other.influence_points:
            if self.last_name == other.last_name:
                return self.name < other.name
            else:
                return self.last_name < other.last_name
        else:
            return self.influence_points < other.influence_points
        
        
class Team():
    team_id = 0
    def __init__(self, team_name, manager, players):
        self.team_name = team_name
        self.manager = manager
        self.players = players
        Team.team_id += 1
        self.id = Team.team_id
        self.score = 0 
        self.fixture = []
        self.scored = 0
        self.conceded = 0
        self.wins = 0
        self.losses = 0
        
    def reset(self):
        self.manager.reset()
        
        for player in self.players:
            player.reset()

        self.fixture = []
       
    def get_id(self):
        return self.id
       
    def get_name(self):
        return self.team_name
    
    def get_roster(self):
        return self.players
    
    def get_manager(self):
        return self.manager
    
    def add_to_fixture(self,match):
        self.fixture.append(match)
    
    def get_fixture(self):
        return self.fixture
    
    def add_result(self, s):
        own_score, opp_score = s

        self.score += own_score
        self.conceded += opp_score

        if own_score > opp_score:
            self.wins += 1
        elif own_score < opp_score:
            self.losses += 1

        self.scored += own_score
    
    def get_scored(self):
        return self.scored

    def get_conceded(self):
        return self.conceded

    def get_wins(self):
        return self.wins

    def get_losses(self):
        return self.losses
   
    def __str__(self):
        return self.team_name
 
    def  __lt__(self, other):
        if self.score == other.score:
            own_score_diff = self.scored - self.conceded
            other_score_diff = other.scored - other.conceded
            if own_score_diff == other_score_diff:
                return True
            else: 
               return own_score_diff < other_score_diff
        else:
            return self.score < other.score
 
class Match():
    def __init__(self, home_team, away_team, week_no):
        self.home_team = home_team
        self.away_team = away_team
        self.week_no = week_no
        self.played = False
    
    def play(self):
        extra_period = 0
        
        while True:
            for _ in range(4): 
                home_manager_point = random.randint(-10, 10)
                self.home_team.get_manager().influence_list.append(home_manager_point)
                self.home_team.get_manager().influence_points += home_manager_point
                
                away_manager_point = random.randint(-10, 10)
                self.away_team.get_manager().influence_list.append(away_manager_point)
                self.away_team.get_manager().influence_points += away_manager_point
                
                self.home_team.score += home_manager_point
                self.away_team.score += away_manager_point
                
                for player in self.home_team.players:
                    random_score = random.randint(-5, 5)
                    player_score = random_score + player.shooting_pwr
                    player.points += player_score
                    self.home_team.score += player_score

                for player in self.away_team.players:
                    random_score = random.randint(-5, 5)
                    player_score = random_score + player.shooting_pwr
                    player.points += player_score
                    self.away_team.score += player_score

            if self.home_team.score == self.away_team.score:
                print(f"Scores are still tied after 4 periods. Playing Tiebreaker Period {extra_period} again!")
            else:
                break

            extra_period += 1
            self.played = True
      
    def is_played(self):
        return self.played 
    
    def get_match_score(self):
        return (self.home_team.score, self.away_team.score)
    
    def get_teams(self):
        return(self.home_team, self.away_team)
       
    def get_home_team(self):
        return self.home_team
    
    def get_away_team(self):
        return self.away_team
    
    def get_winner(self):
        if self.played:
            if self.home_team.score > self.away_team.score:
                return self.home_team
            elif self.home_team.score < self.away_team.score:
                return self.away_team
        return None
    
    def __str__(self):
        if self.played:
            return f"{self.home_team.get_name()} ({self.home_team.score}) vs. ({self.away_team.score}) {self.away_team.get_name()}"
        else:
            return f"{self.home_team.get_name()} vs. {self.away_team.get_name()}"
    
class Season():
    def __init__(self, teams_file, managers_file, players_file):
        self.teams = []
        self.fixture = []
        teams_data = _read_file(teams_file)
        managers_data = _read_file(managers_file)
        players_data = _read_file(players_file)

        for i in range(len(teams_data)):
            team_name = teams_data[i]
            
            
            manager_name = managers_data[i].split()[0]
            manager_last_name = managers_data[i].split()[1]
            manager = Manager(manager_name, manager_last_name)
            
            
            players = []
            for j in range(i * 5, (i + 1) * 5):
                player_name = players_data[j].split()[0]
                player_last_name = players_data[j].split()[1]
                player = Player(player_name, player_last_name)
                players.append(player)
                     
            team = Team(team_name, manager, players)
            self.teams.append(team)

        self.build_fixture()
    def get_teams(self):
        return self.teams
    
    def get_players(self):
        return self.players
        
    def get_managers(self):
        return self.managers
    
    def get_season_length(self):
        teams_count = len(self.teams)
        weeks_half = teams_count - 1
        total_weeks = 2 * weeks_half

        return total_weeks
    
    def reset(self):
        for team in self.teams:
            team.reset()
    
    def build_fixture(self):
        self.fixture = []
        
        teams_count = len(self.teams)
        half_teams = teams_count // 2
        rounds = teams_count - 1

        first_half_teams = self.teams[:half_teams]
        second_half_teams = self.teams[half_teams:][::-1]

        for round_no in range(rounds):
            round_fixture = []

            for i in range(half_teams):
                home_team = first_half_teams[i]
                away_team = second_half_teams[i]

                if round_no % 2 == 0:
                    match = Match(home_team, away_team, round_no + 1)
                else:
                    match = Match(away_team, home_team, round_no + 1)

                round_fixture.append(match)

            first_half_teams = [first_half_teams[0]] + [first_half_teams[-1]] + first_half_teams[1:-1]
            second_half_teams = [second_half_teams[-1]] + second_half_teams[:-1]

            self.fixture.append(round_fixture)

    def get_week_fixture(self, week_no):
        return self.fixture[week_no - 1]
    
    def get_week_no(self):
        return len(self.fixture)
    
    def play_week(self):
        for match in self.get_week_fixture(self.get_week_no()):
            match.play()
    
    def get_best_player(self):
        best_player = None
        best_points = 0

        for match in self.get_week_fixture(self.get_week_no()):
            home_players = match.get_home_team().get_roster()
            away_players = match.get_away_team().get_roster()

            all_players = home_players + away_players
            
            for player in all_players:
                if player.get_points() > best_points:
                    best_points = player.get_points()
                    best_player = player

        return best_player
    
    def get_best_manager(self):
        best_manager = None
        best_influence_points = 0

        for match in self.get_week_fixture(self.get_week_no()):
            home_manager = match.get_home_team().get_manager()
            away_manager = match.get_away_team().get_manager()

            all_managers = [home_manager, away_manager]

            for manager in all_managers:
                if manager.get_influence() > best_influence_points:
                    best_influence_points = manager.get_influence()
                    best_manager = manager

        return best_manager

    def get_most_scoring_team(self):
        most_scoring_team = None
        highest_score = 0
        
        for team in self.teams:
            team_score = team.get_scored()

            if team_score > highest_score:
                highest_score = team_score
                most_scoring_team = team

        return most_scoring_team
    
    def get_champion(self):
        if self.get_week_no() == self.get_season_length():
            champion_team = None
            highest_score = 0
            
            for team in self.teams:
                team_score = team.get_scored()

                if team_score > highest_score:
                    highest_score = team_score
                    champion_team = team

            return champion_team
        else:
            return None
    
    
    
    
    
    
    
    
    
    
    
    
       
       
       
       
       
       
       
       
       
       
       
       