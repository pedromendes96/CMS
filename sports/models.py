from django.db import models
from utils.models import ActivatableOrderableModel, BaseModelMixin

# Create your models here.
"""
API FOOTBALL
* https://apifootball.com/api/?action=get_countries&APIkey=5d9a3f35763e15a339b25a9600c11a96a12bcd585a5a67f100c89b6122c701c5
* https://apifootball.com/api/?action=get_leagues&country_id=169&APIkey=5d9a3f35763e15a339b25a9600c11a96a12bcd585a5a67f100c89b6122c701c5
* https://apifootball.com/api/?action=get_standings&league_id=63&APIkey=5d9a3f35763e15a339b25a9600c11a96a12bcd585a5a67f100c89b6122c701c5
* https://apifootball.com/api/?action=get_events&from=2019-04-01&to=2019-04-31&league_id=63&APIkey=5d9a3f35763e15a339b25a9600c11a96a12bcd585a5a67f100c89b6122c701c5
* https://apifootball.com/api/?action=get_events&from=2019-04-01&to=2019-04-31&league_id=63&APIkey=5d9a3f35763e15a339b25a9600c11a96a12bcd585a5a67f100c89b6122c701c5&match_id=398144
* https://apifootball.com/api/?action=get_H2H&firstTeam=Chelsea&secondTeam=Arsenal&APIkey=5d9a3f35763e15a339b25a9600c11a96a12bcd585a5a67f100c89b6122c701c5
* https://apifootball.com/api/?action=get_events&from=2019-04-01&to=2019-04-31&league_id=63&APIkey=5d9a3f35763e15a339b25a9600c11a96a12bcd585a5a67f100c89b6122c701c5

"""


class ApiFootballCountry(ActivatableOrderableModel):
    api_name = models.CharField(null=True, blank=False, max_length=256)
    api_code = models.CharField(null=True, blank=False, max_length=256)


class ApiFootballSeason(BaseModelMixin):
    year = models.CharField(null=True, blank=False, max_length=256)
    start_date = models.CharField(null=True, blank=False, max_length=256)
    end_date = models.CharField(null=True, blank=False, max_length=256)


class ApiFootballLeague(ActivatableOrderableModel):
    api_id = models.IntegerField(null=True, blank=False)
    api_name = models.CharField(null=True, blank=False, max_length=256)

    logo = models.URLField(blank=True, null=True)
    flag = models.URLField(blank=True, null=True)
    standings = models.BooleanField(blank=True, null=True)
    country = models.ForeignKey(
        ApiFootballCountry, null=True, blank=False, on_delete=models.CASCADE)
    season = models.ForeignKey(
        ApiFootballSeason, null=True, blank=False, on_delete=models.CASCADE)


class ApiFootballTeam(ActivatableOrderableModel):
    api_id = models.IntegerField(null=True, blank=False)
    api_name = models.CharField(null=True, blank=False, max_length=256)
    code = models.CharField(null=True, blank=False, max_length=256)
    logo = models.URLField(null=True, blank=True)
    league = models.ForeignKey(
        ApiFootballLeague, null=True, blank=False, on_delete=models.CASCADE)


class ApiFootballPlayer(BaseModelMixin):
    name = models.CharField(null=True, blank=True, max_length=256)
    number = models.IntegerField(null=True, blank=True)


class ApiFootballCoach(BaseModelMixin):
    name = models.CharField(null=True, blank=False, max_length=256)


class ApiFootballStanding(ActivatableOrderableModel):
    team = models.ForeignKey(ApiFootballTeam, null=True,
                             blank=False, on_delete=models.CASCADE)
    rank = models.IntegerField(null=True, blank=False)
    matchs_played = models.IntegerField(null=True, blank=False)
    win = models.IntegerField(null=True, blank=False)
    draw = models.IntegerField(null=True, blank=False)
    lose = models.IntegerField(null=True, blank=False)
    goals_for = models.IntegerField(null=True, blank=False)
    goals_against = models.IntegerField(null=True, blank=False)
    goals_diff = models.IntegerField(null=True, blank=False)
    points = models.IntegerField(null=True, blank=False)
    group = models.CharField(null=True, blank=True, max_length=256)
    last_update = models.CharField(null=True, blank=False, max_length=256)


class ApiFootballFixture(BaseModelMixin):
    league = models.ForeignKey(
        ApiFootballLeague, null=True, blank=False, on_delete=models.CASCADE)
    home_team = models.ForeignKey(
        ApiFootballTeam, null=True, blank=False, on_delete=models.CASCADE, related_name="home_fixtures")
    away_team = models.ForeignKey(
        ApiFootballTeam, null=True, blank=False, on_delete=models.CASCADE, related_name="away_fixtures")
    api_id = models.IntegerField(null=True, blank=False)
    event_timestamp = models.IntegerField(null=True, blank=False)
    event_date = models.CharField(null=True, blank=False, max_length=256)
    league_round = models.CharField(null=True, blank=False, max_length=256)
    status = models.CharField(null=True, blank=False, max_length=256)
    status_short = models.CharField(null=True, blank=False, max_length=256)
    goals_home_team = models.IntegerField(null=True, blank=False)
    goals_away_team = models.IntegerField(null=True, blank=False)
    halftime_score = models.CharField(null=True, blank=False, max_length=256)
    final_score = models.CharField(null=True, blank=False, max_length=256)
    penalty = models.CharField(null=True, blank=True, max_length=256)
    elapsed = models.CharField(null=True, blank=False, max_length=256)
    first_half_start = models.CharField(
        null=True, blank=False, max_length=256)
    second_half_start = models.CharField(
        null=True, blank=False, max_length=256)


class ApiFootballEvent(BaseModelMixin):
    elapsed = models.IntegerField(null=True, blank=False)
    team_name = models.CharField(null=True, blank=False, max_length=256)
    player = models.CharField(null=True, blank=False, max_length=256)
    event_type = models.CharField(null=True, blank=False, max_length=256)
    detail = models.CharField(null=True, blank=False, max_length=256)


class ApiLineupGame(BaseModelMixin):
    fixture = models.ForeignKey(
        ApiFootballFixture, null=True, blank=False, on_delete=models.CASCADE)

    home_team_formation = models.CharField(
        null=True, blank=False, max_length=256)
    home_team_coach = models.ForeignKey(
        ApiFootballCoach, null=True, blank=False, on_delete=models.CASCADE, related_name="home_game")

    away_team_formation = models.CharField(
        null=True, blank=False, max_length=256)
    away_team_coach = models.ForeignKey(
        ApiFootballCoach, null=True, blank=False, on_delete=models.CASCADE, related_name="away_game")


class ApiLineUpPlayer(BaseModelMixin):
    name = models.CharField(null=True, blank=False, max_length=256)
    number = models.IntegerField(null=True, blank=True)
    is_sub = models.BooleanField(null=True, blank=False, default=False)
    line_up_game = models.ForeignKey(
        ApiLineupGame, null=True, blank=False, on_delete=models.CASCADE)
    team = models.ForeignKey(ApiFootballTeam, null=True,
                             blank=False, on_delete=models.CASCADE)


class ApiStatus(BaseModelMixin):
    assists = models.IntegerField(null=True, blank=False, default=0)
    blocked_shots = models.IntegerField(null=True, blank=False, default=0)
    corner_kicks = models.IntegerField(null=True, blank=False, default=0)
    counter_attacks = models.IntegerField(null=True, blank=False, default=0)
    cross_attacks = models.IntegerField(null=True, blank=False, default=0)
    fouls = models.IntegerField(null=True, blank=False, default=0)
    free_kicks = models.IntegerField(null=True, blank=False, default=0)
    goals = models.IntegerField(null=True, blank=False, default=0)
    goal_attempts = models.IntegerField(null=True, blank=False, default=0)
    offsides = models.IntegerField(null=True, blank=False, default=0)
    ball_possession = models.IntegerField(null=True, blank=False, default=0)
    red_cards = models.IntegerField(null=True, blank=False, default=0)
    goalkeeper_saves = models.IntegerField(null=True, blank=False, default=0)
    shots_off_goal = models.IntegerField(null=True, blank=False, default=0)
    shots_on_goal = models.IntegerField(null=True, blank=False, default=0)
    substitutions = models.IntegerField(null=True, blank=False, default=0)
    throwins = models.IntegerField(null=True, blank=False, default=0)
    medical_treatment = models.IntegerField(null=True, blank=False, default=0)
    yellow_cards = models.IntegerField(null=True, blank=False, default=0)


class ApiFixtureStats(BaseModelMixin):
    home_status = models.ForeignKey(
        ApiStatus, null=True, blank=False, on_delete=models.CASCADE, related_name="home_fixture")
    away_status = models.ForeignKey(
        ApiStatus, null=True, blank=False, on_delete=models.CASCADE, related_name="away_fixture")


class ApiTeamStatsConditions(BaseModelMixin):
    home = models.FloatField(null=True, blank=False, default=0)
    away = models.FloatField(null=True, blank=False, default=0)
    total = models.FloatField(null=True, blank=False, default=0)


class ApiTeamStats(BaseModelMixin):
    league = models.ForeignKey(ApiFootballLeague, null=True,
                               blank=False, on_delete=models.CASCADE)
    team = models.ForeignKey(ApiFootballTeam, null=True,
                             blank=False, on_delete=models.CASCADE)
    matches_played = models.ForeignKey(
        ApiTeamStatsConditions, null=True, blank=True, related_name="+", on_delete=models.CASCADE)
    wins = models.ForeignKey(ApiTeamStatsConditions,
                             null=True, blank=False, related_name="+", on_delete=models.CASCADE)
    draws = models.ForeignKey(ApiTeamStatsConditions,
                              null=True, blank=True, related_name="+", on_delete=models.CASCADE)
    loses = models.ForeignKey(ApiTeamStatsConditions,
                              null=True, blank=True, related_name="+", on_delete=models.CASCADE)
    goals_against = models.ForeignKey(
        ApiTeamStatsConditions, null=True, blank=True, related_name="+", on_delete=models.CASCADE)
    goals_for = models.ForeignKey(
        ApiTeamStatsConditions, null=True, blank=True, related_name="+", on_delete=models.CASCADE)
    goals_avg_against = models.ForeignKey(
        ApiTeamStatsConditions, null=True, blank=True, related_name="+", on_delete=models.CASCADE)
    goals_avg_for = models.ForeignKey(
        ApiTeamStatsConditions, null=True, blank=True, related_name="+", on_delete=models.CASCADE)


class SoccerCompetition(ActivatableOrderableModel):
    """ ScoreBat comepetition """
    api_id = models.IntegerField(null=True, blank=False)
    api_name = models.CharField(null=True, blank=False, max_length=256)
    inserted_name = models.CharField(null=True, blank=True, max_length=256)


class SoccerMatch(ActivatableOrderableModel):
    """ ScoreBat match """
    api_title = models.CharField(null=True, blank=False, max_length=256)
    api_embed = models.TextField(null=True, blank=False, max_length=256)
    api_thumbnail_url = models.URLField(null=True, blank=False)

    inserted_title = models.CharField(null=True, blank=True, max_length=256)
    inserted_description = models.TextField(null=True, blank=True)
    inserted_thumbnail = models.ImageField(null=True, blank=True)

    home_team = models.ForeignKey(
        "sports.SoccerTeam", null=True, blank=False, on_delete=models.CASCADE, related_name="home_match")
    away_team = models.ForeignKey(
        "sports.SoccerTeam", null=True, blank=False, on_delete=models.CASCADE, related_name="away_match")

    competition = models.ForeignKey(
        SoccerCompetition, null=True, blank=False, on_delete=models.CASCADE)


class SoccerTeam(ActivatableOrderableModel):
    """ ScoreBat team """
    api_name = models.CharField(null=True, blank=False, max_length=256)
    min_icon = models.ImageField(null=True, blank=True)
    medium_icon = models.ImageField(null=True, blank=True)
    big_icon = models.ImageField(null=True, blank=True)


class SoccerVideo(BaseModelMixin):
    """ ScoreBat Video """
    api_title = models.CharField(null=True, blank=False, max_length=256)
    api_embed = models.TextField(null=True, blank=False)
    match = models.ForeignKey(SoccerMatch, null=True,
                              blank=False, on_delete=models.CASCADE)

    inserted_title = models.CharField(null=True, blank=True, max_length=256)
    inserted_description = models.TextField(null=True, blank=True)
