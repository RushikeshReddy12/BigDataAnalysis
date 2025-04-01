# BigDataAnalysis

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: Kodakandla Rushikesh Reddy

*INTERN ID*: CTO4WP231

*DOMAIN*: DATA ANALYTICS

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*I analyzed data on a large dataset using Dask, a powerful Python tool for parallel and distributed computing, to demonstrate scalability. The goal was to apply various aggregate operations to large datasets in an efficient manner. Scalability is a crucial aspect of data analysis, particularly when dealing with datasets that are too large to fit in memory or that demand more processing power than a single computer can offer. In these cases, distributed computing tools like Dask or PySpark are very helpful. Dask is particularly well-suited for Python users because it provides a familiar interface similar to Pandas, plus the added advantage of parallelism, which makes handling big datasets easy.
First, it was necessary to confirm that the file path was accurate with OS.path.exists. This would help one determine whether the dataset could be accessed. This essential stage guarantees the dataset is ready for use even before any data is imported. After file confirmation, I read the data into a Dask DataFrame with Dask's read_csv tool. This makes Dask rather efficient for large datasets by letting Dask read data in parallel and split it into smaller partitions that might be handled across several CPU cores.
The work mostly concentrated on performing several aggregations arranged according to the Age column on the numerical columns. These operations computed the mean, sum, count, maximum, minimum, and standard deviation for each numerical column. The Age column in Dask arranged the data using the groupby feature, and every group underwent relevant aggregate operations. For example, the mean was computed using numerical_columns.groupby("Age").mean().compute(), so obtaining the average value for every numerical column, arranged according to Age. Likewise, for every age group the sum, count, maximum, and minimum were calculated using same Dask operations. The standard deviation was computed lastly to estimate the variation or spread of the numerical columns.
In conclusion, I used Dask to successfully demonstrate the scalability of data analysis on a large dataset. I was able to perform several aggregate operations, including mean, sum, count, maximum, minimum, and standard deviation, on large amounts of data while maintaining high performance using Dask. This task showed how Dask can handle datasets larger than memory limits by utilizing parallel computing and out-of-core processing. Dask has proven to be a valuable tool for scalable data analysis and is a great choice for working with large datasets in Python.*

*OUTPUT*
![Image](https://github.com/user-attachments/assets/5b13d310-2f2e-42f1-801a-663e517c83b6)
![Image](https://github.com/user-attachments/assets/690de7b2-8e41-4340-869a-e9c8467a798d)
![Image](https://github.com/user-attachments/assets/485b21bd-ac33-42c1-b14a-691556052e83)
![Image](https://github.com/user-attachments/assets/dfaab20a-fbfe-44ac-bcbc-91cbfc688e10)
![Image](https://github.com/user-attachments/assets/cdc8614b-a5a2-40de-a82d-d33a62f13599)
