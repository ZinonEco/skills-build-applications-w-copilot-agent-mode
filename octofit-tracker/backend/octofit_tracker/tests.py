from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout')
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2023-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_activity_creation(self):
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(self.activity.type, 'Running')

    def test_leaderboard_points(self):
        self.assertEqual(self.leaderboard.points, 100)

    def test_workout_creation(self):
        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(self.workout.name, 'Test Workout')
