def expected_counts(probabilities: dict[chr, float], text_length: int) -> dict[chr, float]:
     expected = {}
     for character, probability in probabilities.items():
          expected[character] = probability * text_length
     return expected

def chi_square(observed: dict[chr, int], expected: dict[chr, float]) -> float:
     score = 0.0
     for character, expected_count in expected.items():
          observed_count = observed.get(character, 0)
          score += (observed_count - expected_count)**2 / expected_count
     return -score