from django.conf import settings
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from .interpreters import ScoreBatApiInterpreter, ApiFootballInterpreter
from . import models
from datetime import datetime

import requests
import logging

logger = logging.getLogger("sports")

# Create your views here.


class GetScoreBatAvailableMatches(APIView):
    """
    Api that return all the current hightlights available in ScoreBat
    """

    def get(self, request, *args, **kwargs):
        response = requests.get(settings.SOCCER_VIDEO_API)
        data = response.json()
        interpreter = ScoreBatApiInterpreter(data)
        interpreter.update_data()
        return HttpResponse("OK")


class ApiFootballView(APIView):
    """
    Abstract View that will handle all method of API Football 
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.interpreter: ApiFootballInterpreter = ApiFootballInterpreter()

    def get(self, request, *args, **kwargs):
        logger.info("Getting data from the ApiFootball API through the {} view".format(
            self.__class__.__name__))
        return JsonResponse(self.get_data(request, *args, **kwargs))

    def get_data(self, request, *args, **kwargs):
        return {}


class ApiFootballGetCountries(ApiFootballView):
    """
    Call that retrieve/updates the available countries
    """

    def get_data(self, request, *args, **kwargs):
        return self.interpreter.get_or_create_countries()


class ApiFootballGetSeasons(ApiFootballView):
    """
    Call that retrieve/updates the seasons
    """

    def get_data(self, request, *args, **kwargs):
        return self.interpreter.get_or_create_seasons()


class ApiFootballGetLeagues(ApiFootballView):
    """
    Call that retrieve/updates the leagues
    """

    def get_data(self, request, *args, **kwargs):
        return self.interpreter.get_or_create_leagues()


class ApiFootballLeagueTeams(ApiFootballView):
    """
    Call that retrieve/updates the teams per league
    """

    def get_data(self, request, *args, **kwargs):
        league_id = request.query_params.get("league")
        league_instance = models.ApiFootballLeague.objects.get(pk=league_id)
        return self.interpreter.get_league_teams(league_instance)


class ApiFootballTeamPlayers(ApiFootballView):
    """
    Call that retrieve/updates the team per team in one specific league
    """

    def get_data(self, request, *args, **kwargs):
        season_id = request.query_params.get("season")
        season_instance = models.ApiFootballSeason.objects.get(pk=season_id)

        team_id = request.query_params.get("team")
        team_instance = models.ApiFootballTeam.objects.get(pk=team_id)

        return self.interpreter.get_team_players(season_instance, team_instance)


class ApiFootballLeagueStandings(ApiFootballView):
    """
    Call that retrieve/updates the standings per league
    """

    def get_data(self, request, *args, **kwargs):

        league_id = request.query_params.get("league")
        league_instance = models.ApiFootballLeague.objects.get(pk=league_id)
        return self.interpreter.get_standings(league_instance)


class ApiFootballGetLiveFixtures(ApiFootballView):
    """
    Call that retrieve/updates get the actual live fixtures
    """

    def get_data(self, request, *args, **kwargs):
        return self.interpreter.get_live_fixtures()


class ApiFootballGetFixturesByDay(ApiFootballView):
    """
    Call that retrieve/updates the fixtures of a specific day
    """

    def get_data(self, request, *args, **kwargs):
        date_string = request.query_params.get("date")
        date = datetime.strptime(date_string, "%Y-%m-%d")
        return self.interpreter.get_fixture_by_date(date)


class ApiFootballGetFixturesByLeague(ApiFootballView):
    """
    Call that retrieve/updates the fixtures per league
    """

    def get_data(self, request, *args, **kwargs):
        league_id = request.query_params.get("league")
        league_instance = models.ApiFootballLeague.objects.get(pk=league_id)
        return self.interpreter.get_fixture_by_league(league_instance)


class ApiFootballGetH2HFixtures(ApiFootballView):
    """
    Call that retrieve/updates the Head to Head comparasion
    """

    def get_data(self, request, *args, **kwargs):
        home_team_id = request.query_params.get("home_team")
        away_team_id = request.query_params.get("away_team")
        home_team_instance = models.ApiFootballTeam.objects.get(
            pk=home_team_id)
        away_team_instance = models.ApiFootballTeam.objects.get(
            pk=away_team_id)
        return self.interpreter.get_h2h_fixture(home_team_instance, away_team_instance)


class ApiFootballGetEventsByFixture(ApiFootballView):
    """
    Call that retrieve/updates the events per fixture
    """

    def get_data(self, request, *args, **kwargs):
        api_id = request.query_params.get("fixture")
        fixture_instance = models.ApiFootballFixture.objects.get(pk=api_id)
        return self.interpreter.get_events_by_fixture(fixture_instance)


class ApiFootballGetLineupByFixture(ApiFootballView):
    """
    Call that retrieve/updates the line up of the team per fixture
    """

    def get_data(self, request, *args, **kwargs):
        api_id = request.query_params.get("fixture")
        fixture_instance = models.ApiFootballFixture.objects.get(pk=api_id)
        return self.interpreter.get_lineups_by_fixture(fixture_instance)


class ApiFootballGetStatsByFixture(ApiFootballView):
    """
    Call that retrieve/updates the stats per fixture
    """

    def get_data(self, request, *args, **kwargs):
        api_id = request.query_params.get("fixture")
        fixture_instance = models.ApiFootballFixture.objects.get(pk=api_id)
        return self.interpreter.get_stats_by_fixture(fixture_instance)


class ApiFootballGetStatsByTeam(ApiFootballView):
    """
    Call that retrieve/updates the stats per team
    """

    def get_data(self, request, *args, **kwargs):
        league_id = request.query_params.get("league")
        league_instance = models.ApiFootballLeague.objects.get(pk=league_id)

        team_id = request.query_params.get("team")
        team_instance = models.ApiFootballTeam.objects.get(
            pk=team_id)

        return self.interpreter.get_stats_by_team(league_instance, team_instance)
