from alice_fluentcheck import AliceIntentSlot, AliceIntent, AliceRequest


class Test_Simple:
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
