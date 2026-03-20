import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from api.models import User, Team, Activity, Workout, Leaderboard

# Create users
def create_users():
    users = []
    for i in range(5):
        user, _ = User.objects.get_or_create(username=f'user{i}')
        users.append(user)
    return users

# Create teams
def create_teams(users):
    teams = []
    for i in range(2):
        team, _ = Team.objects.get_or_create(name=f'Team {i}')
        team.members.set(users[i*2:(i+1)*2])
        teams.append(team)
    return teams

# Create activities
def create_activities(users):
    for user in users:
        Activity.objects.get_or_create(user=user, type='run', duration=random.randint(10, 60))

# Create workouts
def create_workouts(users):
    for user in users:
        Workout.objects.get_or_create(user=user, description='Pushups')

# Create leaderboard
def create_leaderboard(teams):
    for team in teams:
        Leaderboard.objects.get_or_create(team=team, score=random.randint(50, 200))

if __name__ == '__main__':
    users = create_users()
    teams = create_teams(users)
    create_activities(users)
    create_workouts(users)
    create_leaderboard(teams)
    print('Test data created.')
