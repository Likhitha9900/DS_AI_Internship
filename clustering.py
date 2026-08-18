import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("cleaned_blood_transfusion.csv")

X = df[["Recency", "Frequency", "Monetary", "Time"]]

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

print("Cluster Distribution:")
print(df["Cluster"].value_counts())

print("\nCluster Summary:")
print(
    df.groupby("Cluster")[[
        "Recency",
        "Frequency",
        "Monetary",
        "Time"
    ]].mean()
)

plt.figure(figsize=(8, 6))

plt.scatter(
    df["Frequency"],
    df["Monetary"],
    c=df["Cluster"]
)

plt.xlabel("Frequency")
plt.ylabel("Monetary")
plt.title("Donor Behavior Clusters")

plt.show()