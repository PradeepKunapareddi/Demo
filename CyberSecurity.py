import os
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

try:
        file_path = r"C:\Users\prade\Downloads\Global_Cybersecurity_Threats_2015-2024.csv"
        df = pd.read_csv(file_path)
        print("File loaded successfully.")


        df.drop_duplicates() #Remove Duplicate values
        print(df)

        df.dropna() # Remove Missing values 
        print(df)

        print(df.isnull().sum()) # Here we identify the missing values 

        df['Year'] = pd.to_numeric(df['Year'], errors = 'coerce')
        df = df.dropna(subset=['Year'])
        df['Year'] = df['Year'].astype(int)






        df['Country'] = df['Country'].str.strip().str.lower()
        print(df['Country'].unique())                                                        #IT removes gthe trailing and removing white
                                                      #spaces and covert upper case to lower
                                                                              

        df.shape # It gives particular shape of rows and columns

      # Define the categorical columns based on your dataset
        categorical_columns = [
        'Attack Type',
        'Target Industry',
        'Attack Source',
        'Security Vulnerability Type',
        'Defense Mechanism Used'
         ]

# Normalize: strip whitespaces and convert to lowercase
        for col in categorical_columns:
            df[col] = df[col].astype(str).str.strip().str.lower()


        df.rename(columns={
        'Country': 'country',
        'Year': 'year',
        'Attack Type': 'attack_type',
        'Target Industry': 'target_industry',
        'Financial Loss (in Million $)': 'financial_loss_million',   # Rename the column names for esy understandability purpose
        'Number of Affected Users': 'affected_users',
        'Attack Source': 'attack_source',
        'Security Vulnerability Type': 'vulnerability_type',
        'Defense Mechanism Used': 'defense_mechanism',
        'Incident Resolution Time (in Hours)': 'resolution_time_hours'
          }, inplace=True)

        print(df)

except FileNotFoundError:
        print("File not found. Please check the path.")

except Exception as e:
        print(f"Error reading file : {e}")



# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Power@789',     # Replace with your actual MySQL password
      
)

cursor = conn.cursor()

cursor.execute("Create Database IF NOT EXISTS cybersecurity_data; ")
conn.commit()
cursor.close()
conn.close()


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Power@789',     # Replace with your actual MySQL password
    database='cybersecurity_data'  # Make sure this DB exists
)

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS THREATS (
    country VARCHAR(100),
    year INT,
    attack_type VARCHAR(100),
    target_industry VARCHAR(100),
    financial_loss_million FLOAT,
    affected_users BIGINT,
    attack_source VARCHAR(100),
    vulnerability_type VARCHAR(100),
    defense_mechanism VARCHAR(100),
    incident_resolution_time_hours FLOAT
)
''')

df = pd.DataFrame({
    'country': ['USA', 'UK'],
    'year': [2023, 2024],
    'attack_type': ['Phishing', 'Ransomware'],
    'target_industry': ['Finance', 'Healthcare'],
    'financial_loss_million': [50.25, 100.75],
    'affected_users': [10000, 20000],
    'attack_source': ['Email', 'Network'],
    'vulnerability_type': ['Social Engineering', 'Software Bug'],
    'defense_mechanism': ['2FA', 'Firewall'],
    'resolution_time_hours': [48, 72]
})

engine = create_engine("mysql+mysqlconnector://root:Power%40789@localhost/cybersecurity_data")

df.to_sql(name="threats", con=engine, if_exists="append", index=False)

print("Data has been Inserted successfully in to the MYSQL Database!!")



#Top countries affected by cyberAttacts


top_countries = df['country'].value_counts().head(30)
print("Top 10 Countries Affected by Cyber Attacks:\n")
print(top_countries)

#Frequency of different types of threats
print("\nFrequency of different attack tyupes are :")
Frequency = df['attack_type'].value_counts()
print(Frequency)

#Year - Over -Year trends in global security incidents
print("\nYearly trends in global CyberSecurity Incidents: ")
yearly_trends = df['year'].value_counts().sort_index()
print(yearly_trends)


#Severity Levels and their impact by region
print("\nSeverity levels and their impact by region:")
Severity = df.groupby('country')[['financial_loss_million', 'affected_users']].sum().sort_values(by = 'financial_loss_million',
                ascending = False).head(20)
print(Severity)

#Correlation between attack type and sector targeted
print("\nCorrelation between attack type and sector targeted:")
Correlation = df.groupby(['attack_type', 'target_industry']).size().sort_values(ascending = False).head(20)
print(Correlation)

#Console Output
print("Console Output")

#Summary Statistics
print("\n******** SUMMARY STATISTICS *******")
print(df.describe(include="all").transpose())

#Most frequent threat types
print("\n******** Most Frequent Threat Types *********")
print(df['attack_type'].value_counts().head(20))

#Region wise or year wise breakdowns
print("\n********Region wise or year wise breakdowns********* ")
print(df['country'].value_counts().head(20))

#Key trends and outliers in the data set
print("\n********* Key trends and outliers in the data set")

print("\n********Top incidents with highest loss*********")
print(df[['country','attack_type','financial_loss_million']].sort_values(by='financial_loss_million', 
ascending = False).head(10).reset_index(drop=True))

print("\n********** Top Incidents with highest loss*******")
print(df[['country','attack_type','affected_users']].sort_values(by='affected_users',ascending = False).head(10)
      .reset_index(drop=True))

top_loss = df.groupby('country')['financial_loss_million'].sum().sort_values(ascending=False).head(10)



