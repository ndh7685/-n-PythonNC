import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="student_management",
        user="postgres",
        password="duyhung1611"
    )
