import mock_tests.demo_c

def test_bar(mocker):
    mocker.patch('mock_tests.demo_c.Foo.load_foo', return_value='foo-updated')
    assert mock_tests.demo_c.bar() == 'foo-updated'