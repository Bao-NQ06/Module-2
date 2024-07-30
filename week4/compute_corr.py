import numpy as np
import pandas as pd

def compute_correlation_cofficient (X , Y ) :
    N = len( X )
    numerator = 0
    denominator = 0
    numerator = N *(np.sum(X*Y))-(sum(X)*sum(Y))
    denominator = np.sqrt(N*np.sum(X**2)-(np.sum(X)**2)) * np.sqrt(N*np.sum(Y**2)-(np.sum(Y)**2))

    return np . round ( numerator / denominator ,2)

# X = np . asarray ([ -2 , -5 , -11 , 6 , 4 , 15 , 9])
# Y = np . asarray ([4 , 25 , 121 , 36 , 16 , 225 , 81])
# print (" Correlation : ", compute_correlation_cofficient (X , Y ) )


data = pd . read_csv ("Module-2\\week4\\advertising.csv")

def correlation (x , y ) :
    X = np.asarray(x)
    Y = np.asarray(y)
    corr = compute_correlation_cofficient(X,Y)
    
    return corr


# Example usage :
# x = data ['TV']
# y = data ['Radio']
# corr_xy = correlation (x , y )
# print ( f" Correlation between TV and Sales : { round ( corr_xy , 2)}")


# Example 2:

# features = ['TV', 'Radio', 'Newspaper']

# for feature_1 in features :
#     for feature_2 in features :
#         correlation_value = correlation ( data [ feature_1 ] , data [ feature_2 ])
#         print ( f" Correlation between { feature_1 } and { feature_2 }: { round (correlation_value , 2)}")


# Example 3:
# x = data ['Radio']
# y = data ['Newspaper']

# result = np.corrcoef(x, y)
# print(result)


# Example 4:
# x = data ['Radio']
# y = data ['Newspaper']
# print(data.corr())


# Example 5:
import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(10 ,8))
sns.heatmap(data.corr(), annot=True, fmt=".2f", linewidth=.5)
plt.show()