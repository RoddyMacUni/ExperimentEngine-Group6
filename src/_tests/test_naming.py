from processing.FileNameValidator import FileNameValidator

def test_simple_name_works():
    assert FileNameValidator().ValidateEncodedVideoName("testid_1_encoded.mp4") == True

def test_complex_name_works():
    assert FileNameValidator().ValidateEncodedVideoName("6d8518a5-7057-4e9d-b7d7-76465c29158e_20_encoded.mp4") == True

def test_name_without_suffix_fails():
    assert FileNameValidator().ValidateEncodedVideoName("testid_1") == False

def test_invalid_sequence_fails():
    assert FileNameValidator().ValidateEncodedVideoName("testid_one_encoded.mp4") == False

def test_prefix_fails():
    assert FileNameValidator().ValidateEncodedVideoName("test_testid_1_encoded.mp3") == False