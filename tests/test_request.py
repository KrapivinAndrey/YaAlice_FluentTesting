from alicefluentcheck import AliceEntity, AliceIntent, AliceIntentSlot, AliceRequest


class TestAliceRequest:
    def test_create_helloworld(self):
        test = AliceRequest().command("Hello Alice").build()
        control = {
            "meta": {
                "locale": "ru-RU",
                "timezone": "UTC",
                "client_id": "AliceMock",
                "interfaces": {},
            },
            "session": {
                "message_id": 3,
                "session_id": "d825cbef-e7d6-4af9-9810-3ff3f358ac16",
                "skill_id": "3308dc06-b901-4f7e-8882-beb1b84c0753",
                "user": {"user_id": "000"},
                "application": {"application_id": "000"},
                "user_id": "000",
                "new": False,
            },
            "request": {
                "command": "hello alice",
                "original_utterance": "Hello Alice",
                "nlu": {
                    "tokens": ["hello", "alice"],
                    "entities": [],
                    "intents": {},
                },
                "markup": {"dangerous_context": False},
                "type": "SimpleUtterance",
            },
            "version": "1.0",
            "state": {
                "session": {},
                "user": {},
                "applications": {},
            },
        }
        assert test == control

    def test_create_token(self):
        test = AliceRequest().command("Hello Alice").access_token("000").build()
        control = {
            "meta": {
                "locale": "ru-RU",
                "timezone": "UTC",
                "client_id": "AliceMock",
                "interfaces": {},
            },
            "session": {
                "message_id": 3,
                "session_id": "d825cbef-e7d6-4af9-9810-3ff3f358ac16",
                "skill_id": "3308dc06-b901-4f7e-8882-beb1b84c0753",
                "user": {"user_id": "000", "access_token": "000"},
                "application": {"application_id": "000"},
                "user_id": "000",
                "new": False,
            },
            "request": {
                "command": "hello alice",
                "original_utterance": "Hello Alice",
                "nlu": {
                    "tokens": ["hello", "alice"],
                    "entities": [],
                    "intents": {},
                },
                "markup": {"dangerous_context": False},
                "type": "SimpleUtterance",
            },
            "version": "1.0",
            "state": {
                "session": {},
                "user": {},
                "applications": {},
            },
        }
        assert test == control

    def test_acount_link(self):
        test = AliceRequest().account_linking_complete().access_token("000").build()
        control = {
            "meta": {
                "locale": "ru-RU",
                "timezone": "UTC",
                "client_id": "AliceMock",
                "interfaces": {},
            },
            "session": {
                "message_id": 3,
                "session_id": "d825cbef-e7d6-4af9-9810-3ff3f358ac16",
                "skill_id": "3308dc06-b901-4f7e-8882-beb1b84c0753",
                "user": {"user_id": "000", "access_token": "000"},
                "application": {"application_id": "000"},
                "user_id": "000",
                "new": False,
            },
            "account_linking_complete_event": {},
            "version": "1.0",
            "state": {
                "session": {},
                "user": {},
                "applications": {},
            },
        }
        assert test == control

    def test_add_entity(self):
        fio = AliceEntity().fio("??????????????", "??????", "????????????????")
        test = AliceRequest().command("?????????????? ?????? ????????????????").add_entity(fio).build()
        control = {
            "meta": {
                "locale": "ru-RU",
                "timezone": "UTC",
                "client_id": "AliceMock",
                "interfaces": {},
            },
            "session": {
                "message_id": 3,
                "session_id": "d825cbef-e7d6-4af9-9810-3ff3f358ac16",
                "skill_id": "3308dc06-b901-4f7e-8882-beb1b84c0753",
                "user": {"user_id": "000"},
                "application": {"application_id": "000"},
                "user_id": "000",
                "new": False,
            },
            "request": {
                "command": "?????????????? ?????? ????????????????",
                "original_utterance": "?????????????? ?????? ????????????????",
                "nlu": {
                    "tokens": ["??????????????", "??????", "????????????????"],
                    "entities": [
                        {
                            "type": "YANDEX.FIO",
                            "value": {
                                "first_name": "??????",
                                "patronymic_name": "????????????????",
                                "last_name": "??????????????",
                            },
                            "tokens": {"start": 0, "end": 0},
                        }
                    ],
                    "intents": {},
                },
                "markup": {"dangerous_context": False},
                "type": "SimpleUtterance",
            },
            "version": "1.0",
            "state": {
                "session": {},
                "user": {},
                "applications": {},
            },
        }
        assert test == control

    def test_add_intent(self):
        intent = AliceIntent().confirm()
        test = AliceRequest().command("????").add_intent(intent).build()
        control = {
            "meta": {
                "locale": "ru-RU",
                "timezone": "UTC",
                "client_id": "AliceMock",
                "interfaces": {},
            },
            "session": {
                "message_id": 3,
                "session_id": "d825cbef-e7d6-4af9-9810-3ff3f358ac16",
                "skill_id": "3308dc06-b901-4f7e-8882-beb1b84c0753",
                "user": {"user_id": "000"},
                "application": {"application_id": "000"},
                "user_id": "000",
                "new": False,
            },
            "request": {
                "command": "????",
                "original_utterance": "????",
                "nlu": {
                    "tokens": ["????"],
                    "entities": [],
                    "intents": {"YANDEX.CONFIRM": {}},
                },
                "markup": {"dangerous_context": False},
                "type": "SimpleUtterance",
            },
            "version": "1.0",
            "state": {
                "session": {},
                "user": {},
                "applications": {},
            },
        }
        assert test == control
