import unittest
from problem import check_university_admission

class TestCheckUniversityAdmission(unittest.TestCase):
    def test_R1(self):
        gender = "Nam"
        score = 23
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Không đỗ đại học")

    def test_R2(self):
        gender = "Nam"
        score = 25
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Đỗ đại học")
        
    def test_R3(self):
        gender = "Nam"
        score = 28
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Đỗ đại học")
        
    def test_R4(self):
        gender = "Nữ"
        score = 23
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Không đỗ đại học")

    def test_R5(self):
        gender = "Nữ"
        score = 25
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Không đỗ đại học")
        
    def test_R6(self):
        gender = "Nữ"
        score = 28
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Đỗ đại học")
    
        
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