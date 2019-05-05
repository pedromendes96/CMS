from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('scorebat/get/available/matches/',
         views.GetScoreBatAvailableMatches.as_view(), name="scorebat_get_available_matches"),
    path('football/get/countries/',
         views.ApiFootballGetCountries.as_view(), name="football_get_countries"),
    path('football/get/seasons/', views.ApiFootballGetSeasons.as_view(),
         name="football_get_seasons"),
    path('football/get/leagues/', views.ApiFootballGetLeagues.as_view(),
         name="football_get_leagues"),
    path('football/get/league/teams/',
         views.ApiFootballLeagueTeams.as_view(), name="football_get_league_teams"),
    path('football/get/team/players/',
         views.ApiFootballTeamPlayers.as_view(), name="football_get_team_players"),
    path('football/get/league/standings/',
         views.ApiFootballLeagueStandings.as_view(), name="football_get_league_standings"),
    path('football/get/live/fixtures/',
         views.ApiFootballGetLiveFixtures.as_view(), name="football_get_live_fixtures"),
    path('football/get/date/fixtures/',
         views.ApiFootballGetFixturesByDay.as_view(), name="football_get_date_fixtures"),
    path('football/get/league/fixtures/',
         views.ApiFootballGetFixturesByLeague.as_view(), name="football_get_league_fixtures"),
    path('football/get/h2h/fixtures/',
         views.ApiFootballGetH2HFixtures.as_view(), name="football_get_h2h_fixtures"),
    path('football/get/fixture/events/',
         views.ApiFootballGetEventsByFixture.as_view(), name="football_get_fixture_events"),
    path('football/get/fixture/lineups/',
         views.ApiFootballGetLineupByFixture.as_view(), name="football_get_fixture_lineups"),
    path('football/get/fixture/stats/',
         views.ApiFootballGetStatsByFixture.as_view(), name="football_get_fixture_stats"),
    path('football/get/team/stats/',
         views.ApiFootballGetStatsByTeam.as_view(), name="football_get_team_stats"),
]
