from csdl import get_connection

def getsinhvien():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        query = """
        SELECT * FROM SinhVien
        """
        
        cursor.execute(query)
        sinhviens = cursor.fetchall()
        return sinhviens

    except Exception as e:
        print("Lỗi khi truy vấn dữ liệu từ cơ sở dữ liệu:", e)
        return None

    finally:
        if conn:
            conn.close()