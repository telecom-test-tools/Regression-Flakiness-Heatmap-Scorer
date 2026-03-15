

def test_plugin_import():
    from flakiness_plugin import FlakinessPlugin

    plugin = FlakinessPlugin()
    assert plugin.name == "flakiness-scorer"
