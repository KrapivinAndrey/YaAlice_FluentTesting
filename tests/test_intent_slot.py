from alice_fluentcheck import AliceIntentSlot, AliceIntent


def test_create_one_slot():
    test = AliceIntentSlot("test").type_number().tokens(1, 2).value(5).val
    control = {
        "test": {"type": "YANDEX.NUMBER", "tokens": {"start": 1, "end": 2}, "value": 5}
    }

    assert test == control
