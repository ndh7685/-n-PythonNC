from db_config import get_connection

def register_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


# Thêm mới học sinh
def add_student(name, age, grade, address):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO students (name, age, grade, address) VALUES (%s, %s, %s, %s)",
            (name, age, grade, address),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

# Xem danh sách học sinh
def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        return students
    finally:
        cursor.close()
        conn.close()

# Xóa học sinh
def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

# Sửa thông tin học sinh
def update_student(student_id, name, age, grade, address):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE students
            SET name = %s, age = %s, grade = %s, address = %s
            WHERE id = %s
            """,
            (name, age, grade, address, student_id),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

# Tìm kiếm học sinh theo tên
def search_students_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM students WHERE name ILIKE %s", (f"%{name}%",))
        students = cursor.fetchall()
        return students
    finally:
        cursor.close()
        conn.close()

# Tìm kiếm học sinh theo ID
def search_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        student = cursor.fetchone()
        return student
    finally:
        cursor.close()
        conn.close()
