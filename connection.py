import pyodbc
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


connection = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=DESKTOP-P4JB2O7\SQLEXPRESS;'
    r'DATABASE=AdventureWorks2022;'
    r'Trusted_Connection=yes;'
    r'TrustServerCertificate=yes;'
)


query = """
    SELECT Squarefeet, AnnualRevenue, NumberEmployees
    FROM Sales.vStoreWithDemographics
"""


df = pd.read_sql_query(query, connection)


connection.close()


avg_data = df.groupby('Squarefeet').agg(
    avg_employees=('NumberEmployees', 'mean'),
    avg_revenue=('AnnualRevenue', 'mean')
).reset_index()


print(avg_data)

#  Average Revenue by Store Size
plt.figure(figsize=(12, 6))
plt.plot(avg_data['Squarefeet'], avg_data['avg_revenue'], label='Average Revenue', color='blue')
plt.xlabel('Store Size (Squarefeet)')
plt.ylabel('Average Revenue')
plt.title('Average Revenue by Store Size')
plt.xticks(rotation=45)
plt.legend()
plt.show()

#       Average Employees by Store Size
plt.figure(figsize=(12, 6))
plt.plot(avg_data['Squarefeet'], avg_data['avg_employees'], label='Average Employees', color='green')
plt.xlabel('Store Size (Squarefeet)')
plt.ylabel('Average Employees')
plt.title('Average Employees by Store Size')
plt.xticks(rotation=45)
plt.legend()
plt.show()

plt.plot(avg_data['avg_employees'], avg_data['avg_revenue'], color='green')
plt.xlabel('Average Employees')
plt.ylabel('Average revenue')
plt.title("Average Employee Count vs Average Revenue")
plt.text(x=55, y=262000, s="However, revenue plateaus \nafter an average employee \ncount of 52.")
plt.show()

