import unittest
from problem import check_university_admission

class TestCheckUniversityAdmission(unittest.TestCase):
    def test_male_admission(self):
        gender = "Nam"
        score = 25
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Đỗ đại học")

    def test_female_admission(self):
        gender = "Nữ"
        score = 28
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Đỗ đại học")

    def test_male_non_admission(self):
        gender = "Nam"
        score = 23
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Không đỗ đại học")

    def test_female_non_admission(self):
        gender = "Nữ"
        score = 26
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Không đỗ đại học")

    def test_invalid_score(self):
        gender = "Nam"
        score = 32
        with self.assertRaises(ValueError):
            check_university_admission(gender, score)

    def test_invalid_gender(self):
        gender = "Other"
        score = 21
        with self.assertRaises(ValueError):
            check_university_admission(gender, score)

if __name__ == '__main__':
    unittest.main()