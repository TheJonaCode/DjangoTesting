import datetime
from urllib import response

from django.utils import timezone
from django.test import TestCase


from polls.models import Question

class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿cual es el mejor course director de Platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


    def create_question(questiontext, days):
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(questiontext=questiontext, pub_date=time)


class QuestionIndexViewTest(TestCase):

    def test_no_question(self):
        """if no question exist , an aporpiate message is displayed"""

        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], []) 

    def test_future_question(self):
        """ No public questions del future """
        createQuestion("future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])


    def test_past_question(self):
        """ Question with a pub_date in the past are displayed on the index page """

        question = createQuestion("Past question", days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [question])