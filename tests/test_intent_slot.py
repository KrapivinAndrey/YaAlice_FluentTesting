from alice_fluentcheck import AliceIntentSlot, AliceIntent


def test_create_one_slot():
    test = AliceIntentSlot("test").type("YANDEX.NUMBER").tokens(1, 2).value(5).val
    control = {
        "test": {"type": "YANDEX.NUMBER", "tokens": {"start": 1, "end": 2}, "value": 5}
    }

    assert test == control


def test_number_slot():
    test = AliceIntentSlot("test").type_number().tokens(1, 2).value(5).val
    control = {
        "test": {"type": "YANDEX.NUMBER", "tokens": {"start": 1, "end": 2}, "value": 5}
    }

    assert test == control


def test_string_slot():
    test = AliceIntentSlot("test").type_string().tokens(1, 2).value("5").val
    control = {
        "test": {"type": "YANDEX.STRING", "tokens": {"start": 1, "end": 2}, "value": "5"}
    }

    assert test == control


def test_datetime_slot():
    test = AliceIntentSlot("test").type_datetime().tokens(1, 2).value(5).val
    control = {
        "test": {"type": "YANDEX.DATETIME", "tokens": {"start": 1, "end": 2}, "value": 5}
    }

    assert test == control


def test_geo_slot():
    test = AliceIntentSlot("test").type_geo().tokens(1, 2).value(5).val
    control = {
        "test": {"type": "YANDEX.GEO", "tokens": {"start": 1, "end": 2}, "value": 5}
    }

    assert test == control


def test_fio_slot():
    test = AliceIntentSlot("test").type_fio().tokens(1, 2).value(5).val
    control = {
        "test": {"type": "YANDEX.FIO", "tokens": {"start": 1, "end": 2}, "value": 5}
    }

    assert test == control
