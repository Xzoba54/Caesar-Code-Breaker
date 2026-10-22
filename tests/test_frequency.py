from src.analysis.frequency import calculate_frequency

def test_calculate_frequency():
     assert calculate_frequency("aabbcccb") == {
          "a": 2,
          "b": 3,
          "c": 3
     }