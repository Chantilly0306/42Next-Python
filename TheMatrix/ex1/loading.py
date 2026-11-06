#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

np.random.seed(42)
cpu_data = np.random.randint(0, 101, size=(3, 5))
df = pd.DataFrame(
    cpu_data,
    index=["Server A", "Server B", "Server C"],
    columns=["T1", "T2", "T3", "T4", "T5"]
)

df.loc["Server A", "T2"] = np.nan

df["Avg"] = df.mean(axis=1)

print(df.isnull().sum())

# bars = plt.bar(df.index, df["Avg"])

# plt.title("Average CPU Usage per Server")
# plt.xlabel("Server")
# plt.ylabel("CPU Usage (%)")
# plt.bar_label(bars, fmt="%.1f%%")
# plt.ylim(0, 100)
# plt.savefig("cpu_usage.png")
# plt.show()
