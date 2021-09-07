import mock_tests.demo_b

def test_foo(mocker):
    mocker.patch('mock_tests.demo_b.foo', return_value=100)
    assert mock_tests.demo_b.foo() == 100