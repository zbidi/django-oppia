from django.urls import reverse
from oppia.test import OppiaTestCase
from quiz.models import Quiz, QuizAttempt

       
class QuizModelsTest(OppiaTestCase):

    fixtures = ['tests/test_user.json',
                'tests/test_oppia.json',
                'tests/test_quiz.json',
                'tests/test_permissions.json',
                'default_gamification_events.json',
                'tests/test_tracker.json',
                'tests/test_quizattempt.json']

    '''
    Quiz model
    '''
    def test_quiz_avg_score_with_attempts(self):
        quiz = Quiz.objects.get(pk=2)
        self.assertEqual(23, quiz.avg_score())

    def test_quiz_avg_score_no_attempts(self):
        quiz = Quiz.objects.get(pk=1)
        self.assertEqual(0, quiz.avg_score())

    '''
    QuizAttempt model
    '''
    def test_quiz_attempt_first(self):
        quiz_attempt = QuizAttempt.objects.get(pk=140106)
        self.assertFalse(quiz_attempt.is_first_attempt())

    def test_quiz_attempt_digest(self):
        quiz_attempt = QuizAttempt.objects.get(pk=140106)
        self.assertEqual("d95762029b6285dae57385341145c40112153cr0s2a1p80a0",
                         quiz_attempt.get_quiz_digest())
