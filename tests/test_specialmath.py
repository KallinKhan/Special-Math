from settings import SPECIALMATH_ENDPOINT


def test_input_7(client):
    response = client.get(SPECIALMATH_ENDPOINT + str(7))
    assert b'79\n' == response.data


def test_input_17(client):
    response = client.get(SPECIALMATH_ENDPOINT + str(17))
    assert b'10926\n' == response.data


def test_input_90(client):
    response = client.get(SPECIALMATH_ENDPOINT + str(90))
    assert b'19740274219868223074\n' == response.data


def test_input_negative(client):
    response = client.get(SPECIALMATH_ENDPOINT + str(-5))
    assert b'-4\n' == response.data


def test_input_string(client):
    response = client.get(SPECIALMATH_ENDPOINT + 'number')
    assert b'"There is a problem with the value you entered. Is it not an integer?"\n' == response.data
