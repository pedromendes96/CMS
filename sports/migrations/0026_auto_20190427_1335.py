# Generated by Django 2.1.7 on 2019-04-27 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0025_auto_20190427_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apifixturestats',
            name='away_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_fixture', to='sports.ApiStatus'),
        ),
        migrations.AlterField(
            model_name='apifixturestats',
            name='home_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_fixture', to='sports.ApiStatus'),
        ),
        migrations.AlterField(
            model_name='apifootballcoach',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballcountry',
            name='api_code',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballcountry',
            name='api_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballevent',
            name='detail',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballevent',
            name='elapsed',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballevent',
            name='event_type',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballevent',
            name='player',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballevent',
            name='team_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='away_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_fixtures', to='sports.ApiFootballTeam'),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='elapsed',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='event_date',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='event_timestamp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='final_score',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='first_half_start',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='fixture_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='goals_away_team',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='goals_home_team',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='halftime_score',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='home_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_fixtures', to='sports.ApiFootballTeam'),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.ApiFootballLeague'),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='league_round',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='second_half_start',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='status',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballfixture',
            name='status_short',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballleague',
            name='api_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballleague',
            name='api_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballleague',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.ApiFootballCountry'),
        ),
        migrations.AlterField(
            model_name='apifootballleague',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.ApiFootballSeason'),
        ),
        migrations.AlterField(
            model_name='apifootballseason',
            name='end_date',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballseason',
            name='start_date',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballseason',
            name='year',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballstanding',
            name='draw',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballstanding',
            name='goals_against',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballstanding',
            name='goals_diff',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballstanding',
            name='goals_for',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballstanding',
            name='last_update',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballstanding',
            name='lose',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballstanding',
            name='matchs_played',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballstanding',
            name='points',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballstanding',
            name='rank',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballstanding',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.ApiFootballTeam'),
        ),
        migrations.AlterField(
            model_name='apifootballstanding',
            name='win',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballteam',
            name='api_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='apifootballteam',
            name='api_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballteam',
            name='code',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apifootballteam',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.ApiFootballLeague'),
        ),
        migrations.AlterField(
            model_name='apilineupgame',
            name='away_team_coach',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_game', to='sports.ApiFootballCoach'),
        ),
        migrations.AlterField(
            model_name='apilineupgame',
            name='away_team_formation',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apilineupgame',
            name='fixture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.ApiFootballFixture'),
        ),
        migrations.AlterField(
            model_name='apilineupgame',
            name='home_team_coach',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_game', to='sports.ApiFootballCoach'),
        ),
        migrations.AlterField(
            model_name='apilineupgame',
            name='home_team_formation',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apilineupplayer',
            name='is_sub',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='apilineupplayer',
            name='line_up_game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.ApiLineupGame'),
        ),
        migrations.AlterField(
            model_name='apilineupplayer',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apilineupplayer',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.ApiFootballTeam'),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='assists',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='ball_possession',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='blocked_shots',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='corner_kicks',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='counter_attacks',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='cross_attacks',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='fouls',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='free_kicks',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='goal_attempts',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='goalkeeper_saves',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='goals',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='medical_treatment',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='offsides',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='red_cards',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='shots_off_goal',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='shots_on_goal',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='substitutions',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='throwins',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apistatus',
            name='yellow_cards',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apiteamstats',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.ApiFootballLeague'),
        ),
        migrations.AlterField(
            model_name='apiteamstats',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.ApiFootballTeam'),
        ),
        migrations.AlterField(
            model_name='apiteamstats',
            name='wins',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sports.ApiTeamStatsConditions'),
        ),
        migrations.AlterField(
            model_name='apiteamstatsconditions',
            name='away',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apiteamstatsconditions',
            name='home',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apiteamstatsconditions',
            name='total',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='soccercompetition',
            name='api_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='soccercompetition',
            name='api_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='soccermatch',
            name='api_embed',
            field=models.TextField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='soccermatch',
            name='api_thumbnail_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='soccermatch',
            name='api_title',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='soccermatch',
            name='away_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_match', to='sports.SoccerTeam'),
        ),
        migrations.AlterField(
            model_name='soccermatch',
            name='competition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.SoccerCompetition'),
        ),
        migrations.AlterField(
            model_name='soccermatch',
            name='home_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_match', to='sports.SoccerTeam'),
        ),
        migrations.AlterField(
            model_name='soccerteam',
            name='api_name',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='soccervideo',
            name='api_embed',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='soccervideo',
            name='api_title',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='soccervideo',
            name='match',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sports.SoccerMatch'),
        ),
    ]
