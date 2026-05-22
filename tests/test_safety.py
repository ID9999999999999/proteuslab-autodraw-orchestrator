import pytest
from proteus_lab_assistant.safety import validate_project_filename, assert_safe_text

def test_filename_ok():
    assert validate_project_filename("A.pdsprj") == "A.pdsprj"

def test_filename_bad_ext():
    with pytest.raises(ValueError):
        validate_project_filename("A.txt")

def test_refuse_crack():
    with pytest.raises(ValueError):
        assert_safe_text("crack proteus")
