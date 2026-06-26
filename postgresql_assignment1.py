"""
PostgreSQL + Python Assignment
Topics: Connect, Create Table, Insert, Fetch, Parameterized Queries,
        SELECT with WHERE, TRUNCATE
Library: psycopg2
"""

import psycopg2
from psycopg2 import OperationalError, Error

# ──────────────────────────────────────────────
# DATABASE CONNECTION
# ──────────────────────────────────────────────
def connect():
    """Create and return a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",   # Change to your database name
            user="postgres",            # Change to your PostgreSQL username
            password="1234",   # Change to your PostgreSQL password
            port="5432"
        )
        print("✅ Connected to PostgreSQL successfully.")
        return conn
    except OperationalError as e:
        print(f"❌ Connection failed: {e}")
        return None


# ──────────────────────────────────────────────
# TASK 1: CREATE TABLE
# ──────────────────────────────────────────────
def create_table(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id      SERIAL PRIMARY KEY,
                name    VARCHAR(100) NOT NULL,
                age     INT          NOT NULL,
                grade   VARCHAR(10)  NOT NULL
            );
        """)
        conn.commit()
        print("✅ Table 'students' created successfully.")
    except Error as e:
        print(f"❌ Error creating table: {e}")
    finally:
        cursor.close()


# ──────────────────────────────────────────────
# TASK 2: INSERT STATIC RECORDS
# ──────────────────────────────────────────────
def insert_records(conn):
    cursor = conn.cursor()
    try:
        records = [
            ("Anuj",  20, "A"),
            ("Bobby",    22, "B"),
            ("Charu",21, "A"),
            ("Darsh",  19, "C"),
            ("Ishan",    23, "B"),
        ]
        cursor.executemany(
            "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s);",
            records
        )
        conn.commit()
        print(f"✅ {cursor.rowcount} records inserted successfully.")
    except Error as e:
        print(f"❌ Error inserting records: {e}")
    finally:
        cursor.close()


# ──────────────────────────────────────────────
# TASK 3: FETCH AND DISPLAY DATA (fetchone + fetchall)
# ──────────────────────────────────────────────
def fetch_records(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM students;")

        # fetchone – retrieve first row
        first_row = cursor.fetchone()
        print("\n📌 First record (fetchone):")
        print(f"   ID: {first_row[0]} | Name: {first_row[1]} | Age: {first_row[2]} | Grade: {first_row[3]}")

        # fetchall – retrieve remaining rows
        remaining = cursor.fetchall()
        print("\n📋 All remaining records (fetchall):")
        print(f"   {'ID':<5} {'Name':<15} {'Age':<6} {'Grade'}")
        print("   " + "-" * 35)
        for row in remaining:
            print(f"   {row[0]:<5} {row[1]:<15} {row[2]:<6} {row[3]}")

    except Error as e:
        print(f"❌ Error fetching records: {e}")
    finally:
        cursor.close()


# ──────────────────────────────────────────────
# TASK 4: USER INPUT + PARAMETERIZED QUERY (INSERT)
# ──────────────────────────────────────────────
def insert_user_input(conn):
    print("\n📝 Enter details to add a new student:")
    name  = input("   Name  : ").strip()
    age   = input("   Age   : ").strip()
    grade = input("   Grade : ").strip()

    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s) RETURNING id;",
            (name, int(age), grade)
        )
        new_id = cursor.fetchone()[0]
        conn.commit()
        print(f"✅ New student '{name}' inserted with ID = {new_id}.")
    except (Error, ValueError) as e:
        print(f"❌ Error inserting user data: {e}")
        conn.rollback()
    finally:
        cursor.close()


# ──────────────────────────────────────────────
# TASK 5: SELECT WITH WHERE CONDITION
# ──────────────────────────────────────────────
def select_with_where(conn):
    grade_filter = input("\n🔍 Enter grade to filter students (e.g. A, B, C): ").strip().upper()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT * FROM students WHERE grade = %s;",
            (grade_filter,)
        )
        rows = cursor.fetchall()
        if rows:
            print(f"\n📋 Students with grade '{grade_filter}':")
            print(f"   {'ID':<5} {'Name':<15} {'Age':<6} {'Grade'}")
            print("   " + "-" * 35)
            for row in rows:
                print(f"   {row[0]:<5} {row[1]:<15} {row[2]:<6} {row[3]}")
        else:
            print(f"   No students found with grade '{grade_filter}'.")
    except Error as e:
        print(f"❌ Error in SELECT WHERE: {e}")
    finally:
        cursor.close()


# ──────────────────────────────────────────────
# TASK 6: TRUNCATE TABLE
# ──────────────────────────────────────────────
def truncate_table(conn):
    confirm = input("\n⚠️  Truncate ALL records from 'students'? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("   Truncate cancelled.")
        return

    cursor = conn.cursor()
    try:
        cursor.execute("TRUNCATE TABLE students RESTART IDENTITY;")
        conn.commit()
        print("✅ Table 'students' truncated. All records removed and ID sequence reset.")
    except Error as e:
        print(f"❌ Error truncating table: {e}")
    finally:
        cursor.close()


# ──────────────────────────────────────────────
# MAIN MENU
# ──────────────────────────────────────────────
def main():
    conn = connect()
    if conn is None:
        return

    while True:
        print("""
╔══════════════════════════════════════╗
║       PostgreSQL Assignment Menu     ║
╠══════════════════════════════════════╣
║  1. Create Table                     ║
║  2. Insert Static Records            ║
║  3. Fetch & Display Records          ║
║  4. Insert via User Input            ║
║  5. SELECT with WHERE condition      ║
║  6. TRUNCATE Table                   ║
║  0. Exit                             ║
╚══════════════════════════════════════╝""")

        choice = input("Enter your choice: ").strip()

        if   choice == "1": create_table(conn)
        elif choice == "2": insert_records(conn)
        elif choice == "3": fetch_records(conn)
        elif choice == "4": insert_user_input(conn)
        elif choice == "5": select_with_where(conn)
        elif choice == "6": truncate_table(conn)
        elif choice == "0":
            conn.close()
            print("✅ Connection closed. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
