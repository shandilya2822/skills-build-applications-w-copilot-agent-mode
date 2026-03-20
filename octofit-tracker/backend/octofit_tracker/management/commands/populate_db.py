from django.core.management.base import BaseCommand
from api.models import User, Team, Activity, Workout, Leaderboard
import random

class Command(BaseCommand):
    help = 'Populate the database with test data.'

    def handle(self, *args, **kwargs):
        users = []
        for i in range(5):
            user, _ = User.objects.get_or_create(username=f'user{i}')
            users.append(user)
        teams = []
        for i in range(2):
            team, _ = Team.objects.get_or_create(name=f'Team {i}')
            team.members.set(users[i*2:(i+1)*2])
            teams.append(team)
        for user in users:
            Activity.objects.get_or_create(user=user, type='run', duration=random.randint(10, 60))
            Workout.objects.get_or_create(user=user, description='Pushups')
        for team in teams:
            Leaderboard.objects.get_or_create(team=team, score=random.randint(50, 200))
        self.stdout.write(self.style.SUCCESS('Test data created.'))
