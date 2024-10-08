# -*- coding: utf-8 -*-


class UnknownGreetingException(Exception):
    def __init__(self, locale):
        super(self.__class__, self).__init__(
            "Could not find greeting for locale {0}".format(locale))


class Greet(object):
    _localizedGreetings = {
        "en": "Hello",
        "fr": "Bonjour",
        "de": "Guten Tag",
        "es": "Hola"
    }

    @classmethod
    def forLocale(cls, locale):
        if cls._localizedGreetings.get(locale):
            return cls._localizedGreetings[locale]
        else:
            raise UnknownGreetingException(locale)
