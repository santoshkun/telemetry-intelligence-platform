
import sys
import pandas as pd
import numpy as np
import sklearn
import optuna

def main():
    print("=" * 50)
    print("TELEMETRY INTELLIGENCE PLATFORM")
    print("=" * 50)

    print(f"Python Version: {sys.version.split()[0]}")
    print(f"Pandas Version: {pd.__version__}")
    print(f"NumPy Version: {np.__version__}")
    print(f"Scikit-learn Version: {sklearn.__version__}")
    print(f"Optuna Version: {optuna.__version__}")

    print("\nEnvironment setup successful!")

if __name__ == "__main__":
    main()
