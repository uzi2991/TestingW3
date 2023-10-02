import unittest
from problem import check_university_admission

class TestCheckUniversityAdmission(unittest.TestCase):
    def test_path_1(self):
        gender = "Nam"
        score = -5
        with self.assertRaises(ValueError):
            check_university_admission(gender, score)

    def test_path_2(self):
        gender = "Khác"
        score = 25
        with self.assertRaises(ValueError):
            check_university_admission(gender, score)
        
    def test_path_3(self):
        gender = "Nam"
        score = 26
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Đỗ đại học")
        
    def test_path_4(self):
        gender = "Nữ"
        score = 29
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Đỗ đại học")

    def test_path_5(self):
        gender = "Nam"
        score = 20
        result = check_university_admission(gender, score)
        self.assertEqual(result, "Không đỗ đại học")
        

if __name__ == '__main__':
    unittest.main()