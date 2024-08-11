import numpy as np

arr = np.array([3, 4, 2, 1, 100])
print("Mean = ",np.mean(arr))
# print(np.sort(arr))
print("Median = ", np.median(np.sort(arr)))
print("Standard Deviation = ", np.std(arr))
print("Variance = ", np.var(arr))
print("Min = ", np.min(arr))
print("Max = ", np.max(arr))
print("percentile of 50 ", np.percentile(np.sort(arr),25))
print("Sum = ", np.sum(arr))
print("Product = ", np.prod(arr))
print("Cumulative Sum = ", np.cumsum(arr))
print("Cumulative Product = ", np.cumprod(arr))

arr1 = np.array([6, 5, 4, 3, 100])
print("Correlation of coefficients = ", np.corrcoef(arr, arr1))
print("Co variance = ",np.cov(arr,arr1))
print("Histogram = ",np.histogram(arr,bins=10))
print("Occurrence = ", np.bincount(arr))
from scipy import stats
print("Mode  = ", stats.mode(arr))










