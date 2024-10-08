# -*- coding: utf-8 -*-
from greetlib.greet import Greet, UnknownGreetingException


class GreetFixture(object):
    pass


class TestGreetingForEnglish(GreetFixture):
    @classmethod
    def setup_class(cls):
        cls.greeting = Greet.forLocale("en")

    def test_greeting_is_hello(self):
        assert self.greeting == "Hello"


class TestGreetingForItalian(GreetFixture):
    @classmethod
    def setup_class(cls):
        try:
            cls.greeting = Greet.forLocale("it")
            cls.exception = False
        except Exception as e:
            cls.exception = e

    def test_exception_is_UnknownGreetingException(self):
        assert self.exception
        assert isinstance(self.exception, UnknownGreetingException)
