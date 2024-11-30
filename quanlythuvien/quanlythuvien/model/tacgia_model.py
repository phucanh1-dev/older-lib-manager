from csdl import get_connection
def gettacgia():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        query = """
        SELECT * FROM TacGia
        """
        
        cursor.execute(query)
        tacgias = cursor.fetchall()
        return tacgias

    except Exception as e:
        print("Lỗi khi truy vấn dữ liệu từ cơ sở dữ liệu:", e)
        return None

    finally:
        if conn:
            conn.close()