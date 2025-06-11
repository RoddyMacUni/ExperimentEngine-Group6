from AppSettings import GetAppSettings

def test_can_get_appsettings():
    appSettings = GetAppSettings()
    
    assert appSettings is not None
    assert len(appSettings.ExperimentsEndpoint) > 0
    assert len(appSettings.ResultsEndpoint) > 0