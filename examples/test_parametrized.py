import pytest

@pytest.mark.parametrize("test_input", ["backslash \\"])
def test_escape(test_input, snapshot):
    """
    snapshottest will generate new snapshots every time you run
    pytest, regardless of the --snapshot-update flag being passed.
    This is because snapshottest does not find the parametrized
    snapshot.

    syrupy's strictness would surface an issue like this in local
    development and CI.
    """
    snapshot.assert_match(test_input)


@pytest.mark.parametrize("test_input", ["simple", "unique"])
def test_filter_tests(test_input, snapshot):
    """
    Running pytest with -k to filter for the unique test will
    delete all other snapshots if using --snapshot-update
    """
    snapshot.assert_match(test_input)

