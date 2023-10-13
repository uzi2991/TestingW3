import unittest
from problem import check_university_admission

class TestCheckUniversityAdmission(unittest.TestCase):
    def test_1(self):
        gender = "Nam"
        score = 31
        with self.assertRaises(ValueError):
            check_university_admission(gender, score)

    def test_2(self):
        gender = "Other"
        score = 25
        with self.assertRaises(ValueError):
            check_university_admission(gender, score)
        
    def test_3(self):
        gender = "Nam"
        score = 24
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Đỗ đại học")
        
    def test_4(self):
        gender = "Nữ"
        score = 27
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Đỗ đại học")

    def test_5(self):
        gender = "Nữ"
        score = 20
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Không đỗ đại học")
        

if __name__ == '__main__':
    unittest.main()