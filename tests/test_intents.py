from alicefluentcheck import AliceIntentSlot, AliceIntent


class TestAliceIntentSlot:
    def test_create_one_slot(self):
        test = AliceIntentSlot("test").type("YANDEX.NUMBER").tokens(1, 2).value(5).val
        control = {
            "test": {
                "type": "YANDEX.NUMBER",
                "tokens": {"start": 1, "end": 2},
                "value": 5,
            }
        }

        assert test == control

    def test_number_slot(self):
        test = AliceIntentSlot("test").type_number().tokens(1, 2).value(5).val
        control = {
            "test": {
                "type": "YANDEX.NUMBER",
                "tokens": {"start": 1, "end": 2},
                "value": 5,
            }
        }

        assert test == control

    def test_string_slot(self):
        test = AliceIntentSlot("test").type_string().tokens(1, 2).value("5").val
        control = {
            "test": {
                "type": "YANDEX.STRING",
                "tokens": {"start": 1, "end": 2},
                "value": "5",
            }
        }

        assert test == control

    def test_datetime_slot(self):
        test = AliceIntentSlot("test").type_datetime().tokens(1, 2).value(5).val
        control = {
            "test": {
                "type": "YANDEX.DATETIME",
                "tokens": {"start": 1, "end": 2},
                "value": 5,
            }
        }

        assert test == control

    def test_geo_slot(self):
        test = AliceIntentSlot("test").type_geo().tokens(1, 2).value(5).val
        control = {
            "test": {"type": "YANDEX.GEO", "tokens": {"start": 1, "end": 2}, "value": 5}
        }

        assert test == control

    def test_fio_slot(self):
        test = AliceIntentSlot("test").type_fio().tokens(1, 2).value(5).val
        control = {
            "test": {"type": "YANDEX.FIO", "tokens": {"start": 1, "end": 2}, "value": 5}
        }

        assert test == control


class TestAliceIntent:
    def test_name_intent(self):
        slot = AliceIntentSlot("test").type("YANDEX.NUMBER").tokens(1, 2).value(5)
        test = AliceIntent("Num").add_slot(slot).val

        control = {
            "Num": {
                "test": {
                    "type": "YANDEX.NUMBER",
                    "tokens": {"start": 1, "end": 2},
                    "value": 5,
                }
            }
        }

        assert test == control

    def test_confirm(self):
        test = AliceIntent().confirm().val

        control = {"YANDEX.CONFIRM": {}}

        assert test == control

    def test_reject(self):
        test = AliceIntent().reject().val

        control = {"YANDEX.REJECT": {}}

        assert test == control

    def test_discard(self):
        test = AliceIntent().discard().val

        control = {"YANDEX.REJECT": {}}

        assert test == control

    def test_help(self):
        test = AliceIntent().help().val

        control = {"YANDEX.HELP": {}}

        assert test == control

    def test_what_can(self):
        test = AliceIntent().what_can_you_do().val

        control = {"YANDEX.WHAT_CAN_YOU_DO": {}}

        assert test == control

    def test_repeat(self):
        test = AliceIntent().repeat().val

        control = {"YANDEX.REPEAT": {}}

        assert test == control
