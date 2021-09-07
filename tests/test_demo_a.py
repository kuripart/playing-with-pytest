import mock_tests.demo_a

# mocking the module when it is imported, not where CONSTANT_TEST is from
def test_mocking_constant_a(mocker):
    # use  patch.object() to replace the CONSTANT_TEST with another constant.
    mocker.patch.object(mock_tests.demo_a, 'CONSTANT_TEST', 5)
    assert mock_tests.demo_a.double() == 25 # 5 * 5