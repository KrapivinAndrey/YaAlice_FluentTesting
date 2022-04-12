from alice_fluentcheck import AliceEntity


class TestAliceEntity:
    def test_create_one_entity(self):
        test = AliceEntity("test").tokens(1, 2).value(5).val
        control = {
            "type": "test",
            "value": 5,
            "tokens": {"start": 1, "end": 2},
        }

        assert test == control

    def test_create_fio_entity(self):
        test = AliceEntity().fio("Фамилия", "Имя", "Отчество").val
        control = {
            "type": "YANDEX.FIO",
            "value": {
                "first_name": "Имя",
                "patronymic_name": "Отчество",
                "last_name": "Фамилия",
            },
            "tokens": {"start": 0, "end": 0},
        }

        assert test == control

    def test_create_number_entity(self):
        test = AliceEntity().number(5).val
        control = {
            "type": "YANDEX.NUMBER",
            "value": 5,
            "tokens": {"start": 0, "end": 0},
        }

        assert test == control

    def test_create_date_entity(self):
        test = AliceEntity().datetime(year=2022, month=1, day=2, hour=3, minute=5).val
        control = {
            "type": "YANDEX.DATETIME",
            "value": {"year": 2022, "month": 1, "day": 2, "hour": 3, "minute": 5},
            "tokens": {"start": 0, "end": 0},
        }

        assert test == control

    def test_create_date_tomorrow(self):
        test = AliceEntity().tomorrow().val
        control = {
            "type": "YANDEX.DATETIME",
            "value": {"day": 1, "day_is_relative": True},
            "tokens": {"start": 0, "end": 0},
        }

        assert test == control

    def test_create_date_yesterday(self):
        test = AliceEntity().yesterday().val
        control = {
            "type": "YANDEX.DATETIME",
            "value": {"day": -1, "day_is_relative": True},
            "tokens": {"start": 0, "end": 0},
        }

        assert test == control
