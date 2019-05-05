from django.conf import settings
from urllib.parse import urljoin
from datetime import datetime
from . import models
from utils.utils import if_empty_string_then_none
import requests
import logging

logger = logging.getLogger("sports")


class ScoreBatApiInterpreter(object):
    """
    Class that handle the interpretation of the JSON from ScoreBatAPI
    """

    def __init__(self, games_info):
        self._games_info = games_info

    def update_data(self):
        for game_info in self._games_info:
            competition = self.update_or_create_competition(game_info)
            home_team, away_team = self.update_or_create_teams_game(game_info)
            match = self.update_or_create_match(
                game_info, home_team, away_team, competition)
            videos_match = self.update_or_create_videos_match(game_info, match)

    def update_or_create_competition(self, game_info):
        competition_json = game_info.get("competition", dict())
        if competition_json:
            filter_context = {"api_id": competition_json.get("id")}
            create_data_context = {
                "api_id": competition_json.get("id"),
                "api_name": competition_json.get("name")
            }
            instance, created = models.SoccerCompetition.create_or_update(filter_context)
        else:
            instance = None
        return instance

    def update_or_create_teams_game(self, game_info):
        home_team_info = game_info.get("side1", dict())
        away_team_info = game_info.get("side2", dict())
        if home_team_info and away_team_info:
            home_team_data = {
                "api_name": home_team_info.get("name")
            }
            away_team_data = {
                "api_name": away_team_info.get("name")
            }
            home_team, home_created = models.SoccerTeam.create_or_update(home_team_data)
            away_team, away_created = models.SoccerTeam.create_or_update(away_team_data)
        else:
            home_team = None
            away_team = None
        return (home_team, away_team)

    def update_or_create_match(self, game_info, home_team, away_team, competition):
        filter_context = {
            "home_team": home_team,
            "away_team": away_team,
            "competition": competition
        }
        update_context = {
            "api_title": game_info.get("title", ""),
            "api_embed": game_info.get("embed", ""),
            "api_thumbnail_url": game_info.get("thumbnail", ""),
        }

        instance, created = models.SoccerMatch.create_or_update(
            filter_context, update_data_context=update_context)

        return instance

    def update_or_create_videos_match(self, game_info, match):
        videos = game_info.get("videos", "")

        for video in videos:
            filter_context = {
                "match": match
            }
            context = {
                "api_title": video.get("title"),
                "api_embed": video.get("embed"),
                "match": match
            }
            instance, created = models.SoccerVideo.create_or_update(
                filter_context, update_data_context=context)
        return videos


class ApiFootballInterpreter(object):
    """
    Class that handle the interpretation of the JSON from ApiFootball
    """

    def _get_request_headers(self):
        headers = {
            "X-RapidAPI-Key": settings.API_FOOTBALL_TOKEN,
            "Accept": "application/json"
        }
        return headers

    def get_or_create_countries(self):
        url = urljoin(settings.API_FOOTBALL_BASE_URL, "countries")
        response = requests.get(url, headers=self._get_request_headers())
        data = response.json()
        for country in data.get("api").get("countries").values():
            context = {
                "api_name": country
            }
            instance, created = models.ApiFootballCountry.objects.get_or_create(**context)
        return data

    def get_or_create_seasons(self):
        response = requests.get(
            urljoin(settings.API_FOOTBALL_BASE_URL, "seasons"), headers=self._get_request_headers())
        data = response.json()
        for key, season in data.get("api").get("seasons").items():
            context = {
                "year": season
            }
            instance, created = models.ApiFootballSeason.objects.get_or_create(**context)
        return data

    def get_or_create_leagues(self):
        response = requests.get(
            urljoin(settings.API_FOOTBALL_BASE_URL, "leagues"), headers=self._get_request_headers())
        data = response.json()
        for league in data.get("api").get("leagues").values():
            filter_context = { "api_name" : league.get("country") }
            update_context = { "api_code" : league.get("country_code") }
            country_instance, created = models.ApiFootballCountry.create_or_update(filter_context, update_data_context=update_context)
            
            filter_context = { "year" : league.get("season") }
            update_context = { "start_date" : league.get("season_start"), "end_date" : league.get("season_end") }
            season_instance, created = models.ApiFootballSeason.create_or_update(filter_context, update_data_context=update_context)

            filter_context = { "api_id": league.get("league_id") }
            update_context = {"api_name": league.get("name"),"logo": league.get("logo"),"flag": league.get("flag"),"country": country_instance,"season": season_instance}
            league_instance, created = models.ApiFootballLeague.create_or_update(filter_context, update_data_context=update_context)
        return data

    def get_league_teams(self, league):
        response = requests.get(
            urljoin(settings.API_FOOTBALL_BASE_URL, "teams/league/{}".format(league.api_id)), headers=self._get_request_headers())
        data = response.json()
        for team in data.get("api").get("teams").values():
            filter_context = { "api_id": team.get("team_id") }
            update_context = { "api_name" : team.get("name"), "code" : team.get("code"), "logo" : team.get("logo"), "league" : league}
            instance, created = models.ApiFootballTeam.create_or_update(filter_context, update_data_context=update_context)
        return data

    def get_team_players(self, season: models.ApiFootballSeason, team : models.ApiFootballTeam):
        response = requests.get(
            urljoin(settings.API_FOOTBALL_BASE_URL, "players/{}/{}".format(season.year, team.api_id)), headers=self._get_request_headers())
        data = response.json()
        for coach in data.get("api").get("coachs"):
            instance, created = models.ApiFootballCoach.objects.get_or_create(
                name=coach)

        for player in data.get("api").get("players"):
            number = if_empty_string_then_none(player.get("number", ""))
            filter_context = { "name" : player.get("player") }
            update_context = { "number" : number }
            instance, created = models.ApiFootballPlayer.create_or_update(filter_context, update_data_context=update_context)
        return data

    def get_standings(self, league):
        response = requests.get(urljoin(settings.API_FOOTBALL_BASE_URL, "leagueTable/{}".format(league.api_id)), headers=self._get_request_headers())
        data = response.json()
        for standing in data.get("api").get("standings"):
            for team in standing:
                try:
                    team_instance = models.ApiFootballTeam.objects.get(
                        api_id=team.get("team_id"))
                    filter_context = { "team": team_instance }
                    update_context = {
                        "rank": team.get("rank"),
                        "matchs_played": team.get("matchsPlayed"),
                        "win": team.get("win"),
                        "draw": team.get("draw"),
                        "lose": team.get("lose"),
                        "goals_for": team.get("goalsFor"),
                        "goals_against": team.get("goalsAgainst"),
                        "goals_diff": team.get("goalsDiff"),
                        "points": team.get("points"),
                        "group": team.get("group"),
                        "last_update": team.get("lastUpdate")
                    }
                    team = models.ApiFootballStanding.create_or_update(filter_context, update_data_context=update_context)
                except:
                    logger.exception("It occur a serious data error in the class {}:\nRelevant data:\nTeam_data:{}\n".format(
                        self.__class__.__name__, team))
        return data

    def _insert_fixture(self, live_fixture):
        home_team, home_created = models.ApiFootballTeam.create_or_update(
            {
                "api_id" : live_fixture.get("homeTeam_id")
            },
            update_data_context={
                "api_name" : live_fixture.get("homeTeam")
            }
        )
        away_team, away_created = models.ApiFootballTeam.create_or_update(
            {
                "api_id" : live_fixture.get("awayTeam_id")
            },
            update_data_context={
                "api_name" : live_fixture.get("awayTeam")
            }
        )
        league = models.ApiFootballLeague.objects.get(
            api_id=live_fixture.get("league_id"))
        filter_context = context = {
            "api_id": live_fixture.get("api_id"),
            "league": league,
            "home_team": home_team,
            "away_team": away_team
        }
        update_context = context = {
            "event_timestamp": live_fixture.get("event_timestamp"),
            "event_date": live_fixture.get("event_date"),
            "league_round": live_fixture.get("round"),
            "status": live_fixture.get("status"),
            "status_short": live_fixture.get("statusShort"),
            "goals_home_team": live_fixture.get("goalsHomeTeam"),
            "goals_away_team": live_fixture.get("goalsAwayTeam"),
            "halftime_score": live_fixture.get("halftime_score"),
            "final_score": live_fixture.get("final_score"),
            "penalty": live_fixture.get("penalty"),
            "elapsed": live_fixture.get("elapsed"),
            "first_half_start": live_fixture.get("firstHalfStart"),
            "second_half_start": live_fixture.get("secondHalfStart")
        }
        instance, created = models.ApiFootballFixture.create_or_update(filter_context, update_data_context=update_context)

    def get_live_fixtures(self):
        response = requests.get(
            urljoin(settings.API_FOOTBALL_BASE_URL, "fixtures/live"), headers=self._get_request_headers())
        data = response.json()
        for live_fixture in data.get("api").get("fixtures").values():
            self._insert_fixture(live_fixture)
        return data

    def get_fixture_by_date(self, date: datetime):
        date_string = date.strftime("%Y-%m-%d")
        response = requests.get(
            urljoin(settings.API_FOOTBALL_BASE_URL, "fixtures/date/{}".format(date_string)), headers=self._get_request_headers())
        data = response.json()
        for fixture in data.get("api").get("fixtures").values():
            self._insert_fixture(fixture)
        return data

    def get_fixture_by_league(self, league):
        response = requests.get(
            urljoin(settings.API_FOOTBALL_BASE_URL, "fixtures/league/{}".format(league.api_id)), headers=self._get_request_headers())
        data = response.json()

        for fixture in data.get("api").get("fixtures").values():
            self._insert_fixture(fixture)
        return data

    def get_h2h_fixture(self, team_one: models.ApiFootballTeam, team_two: models.ApiFootballTeam):
        response = requests.get(
            urljoin(settings.API_FOOTBALL_BASE_URL, "fixtures/h2h/{}/{}".format(team_one.api_id, team_two.api_id)), headers=self._get_request_headers())
        data = response.json()
        for fixture in data.get("api").get("fixtures").values():
            self._insert_fixture(fixture)
        return data

    def get_events_by_fixture(self, fixture: models.ApiFootballFixture):
        response = requests.get(
            urljoin(settings.API_FOOTBALL_BASE_URL, "events/{}".format(fixture.api_id)), headers=self._get_request_headers())
        data = response.json()

        for event in data.get("api").get("events"):
            instance, created = models.ApiFootballEvent.objects.get_or_create(
                elapsed=event.get("elapsed"), team=event.get("teamName"), player=event.get("player"), event_type=event.get("type"), detail=event.get("detail"))
        return data

    def get_lineups_by_fixture(self, fixture: models.ApiFootballFixture):
        response = requests.get(
            urljoin(settings.API_FOOTBALL_BASE_URL, "lineups/{}".format(fixture.api_id)), headers=self._get_request_headers())
        data = response.json()
        is_home_team = True
        line_up_game_instance = models.ApiLineupGame(fixture=fixture)
        for key, line_up in data.get("api").get("lineUps").items():
            formation = line_up.get("formation")
            coach_instance, created = models.ApiFootballCoach.objects.get_or_create(
                name=line_up.get("coach"))

            if is_home_team:
                is_home_team = False
                line_up_game_instance.home_team = fixture.home_team
                line_up_game_instance.home_team_formation = formation
                line_up_game_instance.home_team_coach = coach_instance
            else:
                line_up_game_instance.away_team = fixture.away_team
                line_up_game_instance.away_team_formation = formation
                line_up_game_instance.away_team_coach = coach_instance

        line_up_game_instance.save()

        is_home_team = True
        for key, line_up in data.get("api").get("lineUps").items():
            for player in line_up.get("startXI"):
                filter_context = context = {
                    "line_up_game" : line_up_game_instance,
                    "name" : player.get("player")
                }
                if is_home_team:
                    filter_context.update({"team" : line_up_game_instance.home_team})
                else:
                    filter_context.update({"team" : line_up_game_instance.away_team})
                update_context = {
                    "name" : player.get("player"),
                    "number" : if_empty_string_then_none(player.get("number", "")),
                    "is_sub" : False
                }

                line_up_player_instance, created = models.ApiLineUpPlayer.create_or_update(filter_context, update_data_context=update_context)

            for player in line_up.get("substitutes"):
                filter_context = context = {
                    "line_up_game" : line_up_game_instance,
                    "name" : player.get("player")
                }
                if is_home_team:
                    filter_context.update({"team" : line_up_game_instance.home_team})
                else:
                    filter_context.update({"team" : line_up_game_instance.away_team})
                update_context = {
                    "name" : player.get("player"),
                    "number" : if_empty_string_then_none(player.get("number", "")),
                    "is_sub" : True
                }
                line_up_player_instance, created = models.ApiLineUpPlayer.create_or_update(filter_context, update_data_context=update_context)
            is_home_team = False
        return data

    def get_stats_by_fixture(self, fixture: models.ApiFootballFixture):
        path = "statistics/fixture/{}".format(fixture.api_id)
        url = urljoin(settings.API_FOOTBALL_BASE_URL, path)
        response = requests.get(url, headers=self._get_request_headers())
        data = response.json()
        home_status = models.ApiStatus()
        away_status = models.ApiStatus()
        for status in data.get("api").get("statistics"):
            for key in status.keys():
                if key == "Assists":
                    home_status.assists = status.get("home")
                    away_status.assists = status.get("away")
                elif key == "Blocked Shots":
                    home_status.blocked_shots = status.get("home")
                    away_status.blocked_shots = status.get("away")
                elif key == "Corner Kicks":
                    home_status.corner_kicks = status.get("home")
                    away_status.corner_kicks = status.get("away")
                elif key == "Counter Attacks":
                    home_status.counter_attacks = status.get("home")
                    away_status.counter_attacks = status.get("away")
                elif key == "Cross Attacks":
                    home_status.cross_attacks = status.get("home")
                    away_status.cross_attacks = status.get("away")
                elif key == "Fouls":
                    home_status.fouls = status.get("home")
                    away_status.fouls = status.get("away")
                elif key == "Free Kicks":
                    home_status.free_kicks = status.get("home")
                    away_status.free_kicks = status.get("away")
                elif key == "Goals":
                    home_status.goals = status.get("home")
                    away_status.goals = status.get("away")
                elif key == "Goal Attempts":
                    home_status.goal_attempts = status.get("home")
                    away_status.goal_attempts = status.get("away")
                elif key == "Offsides":
                    home_status.offsides = status.get("home")
                    away_status.offsides = status.get("away")
                elif key == "Ball Possession":
                    home_status.ball_possession = status.get("home")
                    away_status.ball_possession = status.get("away")
                elif key == "Red Cards":
                    home_status.red_cards = status.get("home")
                    away_status.red_cards = status.get("away")
                elif key == "Goalkeeper Saves":
                    home_status.goalkeeper_saves = status.get("home")
                    away_status.goalkeeper_saves = status.get("away")
                elif key == "Shots off Goal":
                    home_status.shots_off_goal = status.get("home")
                    away_status.shots_off_goal = status.get("away")
                elif key == "Shots on Goal":
                    home_status.shots_on_goal = status.get("home")
                    away_status.shots_on_goal = status.get("away")
                elif key == "Substitutions":
                    home_status.substitutions = status.get("home")
                    away_status.substitutions = status.get("away")
                elif key == "Throwins":
                    home_status.throwins = status.get("home")
                    away_status.throwins = status.get("away")
                elif key == "Medical Treatment":
                    home_status.medical_treatment = status.get("home")
                    away_status.medical_treatment = status.get("away")
                elif key == "Yellow Cards":
                    home_status.yellow_cards = status.get("home")
                    away_status.yellow_cards = status.get("away")
        home_status.save()
        away_status.save()
        return data

    def get_stats_by_team(self, league: models.ApiFootballLeague, team: models.ApiFootballTeam):
        response = requests.get(
            urljoin(settings.API_FOOTBALL_BASE_URL, "statistics/{}/{}".format(league.api_id, team.api_id)), headers=self._get_request_headers())
        data = response.json()
        api_team_stats, created = models.ApiTeamStats.objects.get_or_create(
            league=league, team=team)
        context = dict()

        for key, stats in data.get("api").get("stats").items():
            if key == "matchs":
                context.update(self._get_match_stats(stats))
            elif key == "goals":
                context.update(self._get_goals_stats(stats))
            elif key == "goalsAvg":
                context.update(self._get_avg_goals_stats(stats))

        for key in context.keys():
            related_instance = getattr(api_team_stats, key)
            if related_instance:
                related_instance.delete()
            setattr(api_team_stats, key, context[key])
        api_team_stats.save()
        return data

    def _get_match_stats(self, match_stats):
        context = dict()
        context["matches_played"] = self._create_stats_conditions(
            match_stats.get("matchsPlayed"))
        context["wins"] = self._create_stats_conditions(
            match_stats.get("wins"))
        context["draws"] = self._create_stats_conditions(
            match_stats.get("draws"))
        context["loses"] = self._create_stats_conditions(
            match_stats.get("loses"))
        return context

    def _get_goals_stats(self, goals_stats):
        context = dict()
        context["goals_against"] = self._create_stats_conditions(
            goals_stats.get("goalsAgainst"))
        context["goals_for"] = self._create_stats_conditions(
            goals_stats.get("goalsFor"))
        return context
    
    def _get_avg_goals_stats(self, avg_goals_stats):
        context = dict()
        context["goals_avg_against"] = self._create_stats_conditions(
            avg_goals_stats.get("goalsFor"))
        context["goals_avg_for"] = self._create_stats_conditions(
            avg_goals_stats.get("goalsAgainst"))
        return context

    def _create_stats_conditions(self, status):
        return models.ApiTeamStatsConditions.objects.create(home=status.get("home"), away=status.get("away"), total=status.get("total"))
