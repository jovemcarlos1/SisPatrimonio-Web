import pyodbc

SERVER = 'CARLOS'
DATABASE = 'DB_TESTE'
USERNAME = 'sa'
PASSWORD = 'root2025'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()
