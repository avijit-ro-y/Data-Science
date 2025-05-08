#-----------------------------------------------Scipy Constants-----------------------------------------------

# The Scipy constants module provides a large set of physical and mathematical constants that are commonly used in scientific computations.
# These constants are defined as global variables and can be easily accessed by importing the Scipy constants module.

import scipy.constants as const

# Convert 10 meters to centimeters
meters = 10
centimeters = meters / const.centi
print(centimeters)

# Converting temperature units

# Convert 20 degrees Celsius to Kelvin
celsius = 20
kelvin = celsius + const.zero_Celsius
print(kelvin)

#-----------------------------------------------Scipy Stats-----------------------------------------------
#The Scipy stats module provides a large number of probability distributions and statistical functions that are commonly used in statistical analysis and modeling.
# Calculate the mean and standard deviation of a sample:

import scipy.stats as stats
import numpy as np

sample = np.array([1, 2, 3, 4, 5])

mean = stats.tmean(sample)
std = stats.tstd(sample)
print(mean,std)

#-----------------------------------------------Hypothesis Testing-----------------------------------------------
#-----------------------------------------------#One sample t-test-----------------------------------------------
sample = np.random.normal(75, 10, 100)

t_statistic, p_value = stats.ttest_1samp(sample, 75)

if p_value < 0.05:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")
    
#-----------------------------------------------Two sample t-test-----------------------------------------------
group1 = np.random.normal(89, 10, 100)
group2 = np.random.normal(70, 10, 100)

t_statistic, p_value = stats.ttest_ind(group1, group2, equal_var=False)

if p_value < 0.05:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")
    
#-----------------------------------------------Chi-Squared test with/without Contingeny table-----------------------------------------------
grades = np.array([[20, 30, 40], [20, 40, 30]])

chi2_stat, p_value, dof, expected = stats.chi2_contingency(grades)

if p_value < 0.05:
    print("Reject null hypothesis")
else:
    print("Fail to reject null hypothesis")


#-----------------------------------------------Skewness-----------------------------------------------
#Skewness is a measure of the asymmetry of a probability distribution
import matplotlib.pyplot as plt
from scipy.stats import skew

# Create a dataset with positive skewness
data = np.random.gamma(2, size=1000) + 3

# Calculate skewness
skewness = skew(data)

# Plot the histogram
plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(np.mean(data), color='red', linestyle='dashed', linewidth=2, label="Mean")
plt.title(f"Histogram of Skewed Data (Skewness: {skewness:.2f})")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Print skewness value
print(f"Skewness: {skewness:.2f}")

#-----------------------------------------------Handling Sparse Data-----------------------------------------------
import scipy
#Sparse data refers to data that contains a large number of zero or near-zero values, and only a small number of non-zero values. In order to efficiently store and manipulate this type of data, special data structures and algorithms are used, known as sparse matrices
# Let's extend it to 2-D matrix to see what changes
sample_data = [[0, 1, 2, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2] * 10 for _ in range(14)]

print("CSR matrix output : ")
sparse_mn = scipy.sparse.csc_matrix(sample_data)
print(sparse_mn)

#-----------------------------------------------Image Handling-----------------------------------------------
# Load a sample image from scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew
import scipy
#image_data = scipy.misc.face()
# plt.figure(figsize=(6, 6))
# plt.imshow(image_data)
# plt.show()

# Let's do some augmentation on the image at hand
# Rotate the image
# rotated_image = scipy.ndimage.rotate(image_data, 180)
# plt.figure(figsize=(6, 6))
# plt.imshow(rotated_image)
# plt.show()

# Apply other transforms
# zoom_image = scipy.ndimage.zoom(image_data, zoom=[3, 3, 1])
# plt.figure(figsize=(6, 6))
# plt.imshow(zoom_image)
# plt.show()
# print(zoom_image.shape)
# print(image_data.shape)

# Apply Gaussin Filter
# g_image = scipy.ndimage.gaussian_filter(image_data, sigma=3)
# plt.figure(figsize=(6, 6))
# plt.imshow(g_image)
# plt.show()

# -----------------------------------------------Maths with Scipy-----------------------------------------------
# Let's do some integration with scipy

"""
Uses lambda function to define integrals and its limits
"""
# Define the integral equation
function_x = lambda x : (x + 1)

# Compute the integral
integral = scipy.integrate.quad(func=function_x, a=0, b=1) #a=0, b=1: The limits of integration (lower and upper bounds).
print(f"Value of integral is : {integral}")

f = lambda x : x**2 + x*2

# Find the differential equations
#derivative = scipy.misc.derivative(func=f, x0=1, dx=1e-6)
#print(f"Derivative : {derivative}")

#-----------------------------------------------Linear Algebra-----------------------------------------------
from scipy import linalg
# Define a matrix
matrix = np.array([[11, 20, 30], [4, 5, 6], [7, 8, 9]])
print(f"Determinant of the matrix : {linalg.det(matrix)}")

