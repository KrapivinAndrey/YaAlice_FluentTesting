from __future__ import annotations

from chain import chained
from constants import *
from typing import Dict


class AliceIntentSlot:
    """
    Описание одной позиции интента - слота: тип, позиция

    Документация: https://yandex.ru/dev/dialogs/alice/doc/nlu.html
    """

    def __init__(self, name: str):
        self.name = name
        self.type = YA_STRING
        self.tokens = {"start": 0, "end": 0}
        self.value = ""

    @chained
    def type(self, intent_type: str) -> AliceIntentSlot:
        """
        Указать тип слота
        Допустимые значения:

            - YANDEX.NUMBER
            - YANDEX.STRING
            - YANDEX.DATETIME
            - YANDEX.GEO

        :param str intent_type: задает тип слота
        """
        assert intent_type in [
            YA_STRING,
            YA_NUMBER,
            YA_GEO,
            YA_DATETIME
        ], "Неверный тип интента"
        self.type = intent_type

    @chained
    def tokens(self, start=0, end=0) -> AliceIntentSlot:
        """
        Описание позиции найденного интента во фразе пользователя

        :param int start: начало слота во фразе
        :param int end: окончания слота во фразе
        """
        assert type(start) is int, "Параметр НАЧАЛО должен быть числом"
        assert type(end) is int, "Параметр ОКОНЧАНИЕ должен быть числом"

        assert 0 <= start <= end, "Нарушен порядок следования"
        self.tokens["start"] = start
        self.tokens["end"] = end

    @chained
    def value(self, value) -> AliceIntentSlot:
        """
        Указать значение слота

        :param value: значение слота
        """
        self.value = value

    def val(self) -> Dict:
        """
        Собрать значение слота

        :return: значение одной позиции слота интента
        """
        result = {
            self.name: {
                "type": self.type,
                "tokens": {
                    "start": self.tokens["start"],
                    "end": self.tokens["end"],
                },
                "value": self.value,
            }
        }

        return result


class AliceIntent:
    """
    Описание одно интента: имя интента и слоты

    Документация: https://yandex.ru/dev/dialogs/alice/doc/nlu.html
    """

    def __init__(self, name=""):
        self.name = name
        self.slots = {}

    @chained
    def add_slot(self, slot: AliceIntentSlot) -> AliceIntent:
        """

        Добавить слот к интенту: описание позиции где был найден интент, его значение
        :param AliceIntentSlot slot: один слот для интента
        """
        self.slots.update(slot.val())

    def val(self) -> Dict:
        """

        Собрать значение интента
        :return: значение одно интента: тип и слоты
        """
        return {self.name: self.slots}

# Специфичные интенты

    @chained
    def confirm(self) -> AliceIntent:
        """
        Интент "Согласие пользователя": да, согласен и тд
        """
        self.name = YA_CONFIRM
        self.slots.clear()

    @chained
    def reject(self) -> AliceIntent:
        """
        Интент "Отказ пользователя": нет, не надоё и тд
        """
        self.name = YA_REJECT
        self.slots.clear()

    @chained
    def discard(self) -> AliceIntent:
        """
        Интент "Отказ пользователя": нет, не надоё и тд
        """
        self.name = YA_REJECT
        self.slots.clear()

    @chained
    def help(self) -> AliceIntent:
        """
        Интент "Пользователь просит помощи": помощь, справка и тд
        """
        self.name = YA_HELP
        self.slots.clear()

    @chained
    def what_can_you_do(self) -> AliceIntent:
        """
        Интент "Что умеет навык": что ты умеешь
        """
        self.name = YA_WHAT_CAN_YOU_DO
        self.slots.clear()

    @chained
    def repeat(self) -> AliceIntent:
        """
        Интент "Повтори что было до этого": повтори, еще раз и тд
        """
        self.name = YA_REPEAT
        self.slots.clear()
