from src.analysis.frequency import expected_counts

def test_calculates_expected_counts():
     probabilities = {
         "a": 0.5,
         "b": 0.3,
         "c": 0.2,
     }

     result = expected_counts(probabilities, 100)
     assert result == {
         "a": 50.0,
         "b": 30.0,
         "c": 20.0,
     }

def test_handles_zero_text_length():
     probabilities = {"a": 0.5, "b": 0.5}

     result = expected_counts(probabilities, 0)
     assert result == {"a": 0.0, "b": 0.0}

def test_handles_empty_probabilities():
    assert expected_counts({}, 100) == {}