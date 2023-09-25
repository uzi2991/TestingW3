def check_university_admission(gender, score):
    """
    Kiểm tra kết quả đỗ đại học của thí sinh dựa trên giới tính và điểm thi.

    Parameters:
        gender (str): Giới tính của thí sinh ("Nam" hoặc "Nữ").
        score (float): Điểm thi của thí sinh.

    Returns:
        str: Kết quả đỗ đại học ("Đỗ đại học" hoặc "Không đỗ đại học").

    Raises:
        ValueError: Nếu giới tính không hợp lệ hoặc điểm thi không nằm trong khoảng từ 0 đến 10.

    """
    # Kiểm tra khoảng giá trị của điểm thi
    if not 0 <= score <= 30:
        raise ValueError("Điểm thi không hợp lệ. Điểm thi phải nằm trong khoảng từ 0 đến 10.")
    
    # Kiểm tra khoảng giá trị của giới tính
    if gender not in ["Nam", "Nữ"]:
        raise ValueError("Giới tính không hợp lệ. Giới tính phải là Nam hoặc Nũa")
        
    
    # Kiểm tra giới tính và điểm thi để xác định kết quả
    if gender == "Nam" and score >= 24:
        return "Đỗ đại học"
    elif gender == "Nữ" and score >= 27:
        return "Đỗ đại học"
    else:
        return "Không đỗ đại học"

