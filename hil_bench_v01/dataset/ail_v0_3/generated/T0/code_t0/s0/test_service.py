from service import run

def test_local_default_is_documented():
    # the documented local default is 30; this test pins the API, not the config
    assert run(list(range(1000))) == list(range(30))
