#!/usr/bin/env python3
import sys
import importlib.util
import importlib.metadata


def check_dependencies() -> bool:
    packages = ["numpy", "pandas", "matplotlib"]
    missing_packages = []
    print("LOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    for package in packages:
        result = importlib.util.find_spec(package)
        if result is None:
            print(f"[MISSING] {package}")
            missing_packages.append(package)
        else:
            print(f"[OK] {package}")

    if missing_packages:
        print("\nInstall missing packages using pip:")
        print(f"pip install {' '.join(missing_packages)}")

        print("\nInstall missing packages using Poetry:")
        print("poetry install")
        print("poetry run python loading.py")
        for package in missing_packages:
            print(f"poetry add {package}")

        return False
    return True


def compare_packages():
    packages = ["numpy", "pandas", "matplotlib"]

    print("\n===== Environment Information =====")
    print(f"Python executable: {sys.executable}")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Environment path: {sys.prefix}")

    print("\n===== Installed Package Versions =====")

    for package in packages:
        version = importlib.metadata.version(package)
        print(f"{package}: {version}")


def simulate_matrix_data() -> pd.DataFrame:
    rng = np.random.default_rng()

    server_a = rng.normal(60, 10, 1000)
    server_b = rng.normal(50, 12, 1000)
    server_c = rng.normal(70, 8, 1000)

    df = pd.DataFrame({
        "Server A": server_a,
        "Server B": server_b,
        "Server C": server_c
    })
    return df


def analyze_matrix_data(matrix_data: pd.DataFrame):
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    cleaned_data = matrix_data.clip(lower=0, upper=100)

    mean_values = cleaned_data.mean()
    max_values = cleaned_data.max()
    min_values = cleaned_data.min()
    std_values = cleaned_data.std()

    summary = pd.DataFrame({
        "Mean": mean_values,
        "Max": max_values,
        "Min": min_values,
        "Std": std_values
    })
    return summary, cleaned_data


def visualize_matrix_data(data: pd.DataFrame):
    print("Generating visualization...")
    plt.figure(figsize=(12, 6))

    for column in data.columns:
        plt.plot(data.index, data[column], label=column)

    plt.title("Matrix Server CPU Usage")
    plt.xlabel("Data Point")
    plt.ylabel("CPU Usage (%)")

    plt.ylim(0, 100)
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("matrix_analysis.png")

    plt.close()
    print("Analysis complete!")
    print("\nResults saved to: matrix_analysis.png")


if __name__ =="__main__":
    if check_dependencies():
        compare_packages()

        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        matrix_data = simulate_matrix_data()

        summary, cleaned_data = analyze_matrix_data(matrix_data)

        visualize_matrix_data(cleaned_data)
