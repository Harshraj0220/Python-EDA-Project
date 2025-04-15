import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"D:\Python IDLE Programmes\railway.csv")

# --------------------- Basic Overview ---------------------

print("Dataset Shape (rows, columns):")
print(df.shape)
print()

print("Column Names:")
print(df.columns.tolist())
print()

print("Data Types:")
print(df.dtypes)
print()

print("First 5 Rows:")
print(df.head())
print()

print("Last 5 Rows:")
print(df.tail())
print()

print("Missing Values in Each Column:")
print(df.isnull().sum())
print()


# --------------------- Data Type Conversion ---------------------

df['Date of Purchase'] = pd.to_datetime(df['Date of Purchase'])
df['Date of Journey'] = pd.to_datetime(df['Date of Journey'])

df['Time of Purchase'] = pd.to_datetime(df['Time of Purchase'], format='%H:%M:%S').dt.time
df['Departure Time'] = pd.to_datetime(df['Departure Time'], format='%H:%M:%S').dt.time
df['Arrival Time'] = pd.to_datetime(df['Arrival Time'], format='%H:%M:%S').dt.time
df['Actual Arrival Time'] = pd.to_datetime(df['Actual Arrival Time'], format='%H:%M:%S', errors='coerce').dt.time


# --------------------- Summary Statistics ---------------------

print("Numerical Columns Summary:")
print(df.describe())
print()

print("Categorical Columns Summary:")
print(df.describe(include='object'))
print()


# --------------------- Objective 1: Ticket Price Distribution ---------------------

print("Price Statistics:")
print("Min:", df['Price'].min())
print("Max:", df['Price'].max())
print("Mean:", df['Price'].mean())
print("Median:", df['Price'].median())
print()

# Visualize the Ticket Price Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['Price'], bins=50, kde=True)
plt.title('Ticket Price Distribution')
plt.xlabel('Price (£)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()


# --------------------- Objective 2: Journey Status ---------------------

print("Journey Status Counts:")
print(df['Journey Status'].value_counts())
print()

# Visualize the Journey Status Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='Journey Status', data=df)
plt.title('Journey Status Distribution')
plt.xlabel('Status')
plt.ylabel('Count')
plt.tight_layout()
plt.show()


# --------------------- Objective 3: Popular Routes ---------------------

print("Top Departure Stations:")
print(df['Departure Station'].value_counts().head())
print()

print("Top Arrival Destinations:")
print(df['Arrival Destination'].value_counts().head())
print()

# Visualize the Popular Routes (Top Departure Stations)
plt.figure(figsize=(10, 5))
sns.countplot(y='Departure Station', data=df, order=df['Departure Station'].value_counts().head(10).index)
plt.title('Top 10 Departure Stations')
plt.xlabel('Count')
plt.ylabel('Departure Station')
plt.tight_layout()
plt.show()

# Visualize the Popular Routes (Top Arrival Destinations)
plt.figure(figsize=(10, 5))
sns.countplot(y='Arrival Destination', data=df, order=df['Arrival Destination'].value_counts().head(10).index)
plt.title('Top 10 Arrival Destinations')
plt.xlabel('Count')
plt.ylabel('Arrival Destination')
plt.tight_layout()
plt.show()


# --------------------- Objective 4: Delay Reason vs Refund ---------------------

delay_df = df[df['Journey Status'] == 'Delayed']
reason_refund_counts = delay_df.groupby(['Reason for Delay', 'Refund Request']).size().unstack(fill_value=0)

print("Delay Reason vs Refund Request:")
print(reason_refund_counts)
print()

# Visualize Delay Reason vs Refund Request
plt.figure(figsize=(10, 6))
sns.heatmap(reason_refund_counts, annot=True, cmap="Blues", fmt="d")
plt.title('Delay Reason vs Refund Request')
plt.xlabel('Refund Request')
plt.ylabel('Reason for Delay')
plt.tight_layout()
plt.show()


# --------------------- Objective 5: Purchase Behaviors ---------------------

print("Purchase Methods:")
print(df['Purchase Type'].value_counts())
print()

print("Payment Methods:")
print(df['Payment Method'].value_counts())
print()

print("Railcards Used:")
print(df['Railcard'].value_counts())
print()

print("Ticket Class Distribution:")
print(df['Ticket Class'].value_counts())
print()

print("Ticket Types:")
print(df['Ticket Type'].value_counts())
print()

# --------------------- Objective 6: Ticket Price Over Time (Scatter Plot) ---------------------

# Scatter plot: Price vs. Date of Journey
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Date of Journey', y='Price', hue='Ticket Class', alpha=0.7)
plt.title('Ticket Price Over Time by Ticket Class')
plt.xlabel('Date of Journey')
plt.ylabel('Ticket Price (£)')
plt.legend(title='Ticket Class')
plt.tight_layout()
plt.show()


# Visualize Purchase Methods
plt.figure(figsize=(8, 5))
sns.countplot(x='Purchase Type', data=df)
plt.title('Purchase Method Distribution')
plt.xlabel('Purchase Method')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Visualize Payment Methods
plt.figure(figsize=(8, 5))
sns.countplot(x='Payment Method', data=df)
plt.title('Payment Method Distribution')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Visualize Railcards Used
plt.figure(figsize=(8, 5))
sns.countplot(x='Railcard', data=df)
plt.title('Railcards Used')
plt.xlabel('Railcard')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Visualize Ticket Class Distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Ticket Class', data=df)
plt.title('Ticket Class Distribution')
plt.xlabel('Ticket Class')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Visualize Ticket Types Distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Ticket Type', data=df)
plt.title('Ticket Types Distribution')
plt.xlabel('Ticket Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
