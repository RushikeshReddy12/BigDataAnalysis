import dask.dataframe as dd
import os

fp = "C:/VSCode - ALL/CodTech-Internship/Task-1/large_dataset.csv"

if os.path.exists(fp):
    df = dd.read_csv(fp)

    numeric_columns = df.select_dtypes(include=["float64", "int64"])

    # mean
    result_mean = numeric_columns.groupby("Age").mean().compute()
    print("Mean values grouped by Age:\n", result_mean)

    # sum
    result_sum = numeric_columns.groupby("Age").sum().compute()
    print("Sum values grouped by Age:\n", result_sum)

    # count
    result_count = numeric_columns.groupby("Age").count().compute()
    print("Count values grouped by Age:\n", result_count)

    # maximum
    result_max = numeric_columns.groupby("Age").max().compute()
    print("Max values grouped by Age:\n", result_max)

    # minimum
    result_min = numeric_columns.groupby("Age").min().compute()
    print("Min values grouped by Age:\n", result_min)

    # standard deviation
    result_std = numeric_columns.std().compute()
    print("Standard deviation of numeric columns:\n", result_std)

else:
    print(f"The file at {fp} does not exist.")