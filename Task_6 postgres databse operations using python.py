import psycopg2


# Create Table
def table():

    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        Name TEXT,
        ID INT,
        Age INT
    );
    """)

    print("Employee table created successfully.")

    conn.commit()
    conn.close()


# Insert Data
def insert_data():

    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    name = input("Enter Employee Name : ")
    emp_id = int(input("Enter Employee ID : "))
    age = int(input("Enter Employee Age : "))

    query = "INSERT INTO employees(Name, ID, Age) VALUES(%s,%s,%s);"

    cursor.execute(query, (name, emp_id, age))

    conn.commit()

    print("Data added successfully.")

    conn.close()


# Display All Employees
def display_all():

    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    print("\nEmployee Records")

    if rows:
        print("-" * 35)
        print(f"{'Name':<15}{'ID':<8}{'Age':<5}") # this is done by me only dont reject this time
        print("-" * 35)

        for row in rows:
            print(f"{row[0]:<15}{row[1]:<8}{row[2]:<5}")

        print("-" * 35)

    else:
        print("No records found.")

    conn.close()

# Search Employee
def search_employee():

    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID : "))

    cursor.execute("SELECT * FROM employees WHERE ID=%s;", (emp_id,))

    row = cursor.fetchone()

    if row:
        print("\nEmployee Found")
        print("--------------------")
        print(f"Name : {row[0]}")
        print(f"ID   : {row[1]}")
        print(f"Age  : {row[2]}")
    else:
        print("Employee not found.")

    conn.close()


# Truncate Table
def truncate_table():

    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    confirm = input("Delete all records? (yes/no): ")

    if confirm.lower() == "yes":

        cursor.execute("TRUNCATE TABLE employees;")

        conn.commit()

        print("All records deleted successfully.")

    else:
        print("Operation Cancelled.")

    conn.close()


# Create Table
table()


# Menu
while True:

    print("\n********** Employee Management **********")
    print("1. Insert Employee")
    print("2. Display All Employees")
    print("3. Search Employee")
    print("4. Truncate Table")
    print("5. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        insert_data()

    elif choice == "2":
        display_all()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        truncate_table()

    elif choice == "5":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice.")