def test_classes(snapshot):
    """
    snapshottest stores the memory address of the class
    by default.
    """
    class CustomClass:
        pass

    data = set([2, 1, CustomClass()])
    snapshot.assert_match(data)
