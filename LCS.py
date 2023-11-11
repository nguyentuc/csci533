import os
import time
import sys
sys.setrecursionlimit(150000000)

# A Naive recursive Python implementation of LCS problem
def lcs_naive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs_naive(X, Y, m-1, n-1)
    else:
        return max(lcs_naive(X, Y, m, n-1), lcs_naive(X, Y, m-1, n))


# A Top-Down DP implementation of LCS problem
def lcs_top_down(X, Y, m, n, dp):
    if (m == 0 or n == 0):
        return 0

    if (dp[m][n] != -1):
        return dp[m][n]

    if X[m - 1] == Y[n - 1]:
        dp[m][n] = 1 + lcs_top_down(X, Y, m - 1, n - 1, dp)
        return dp[m][n]

    dp[m][n] = max(lcs_top_down(X, Y, m, n - 1, dp), lcs_top_down(X, Y, m - 1, n, dp))
    return dp[m][n]

# Dynamic Programming implementation of LCS problem
def lcs_bottom_up(X, Y, m, n):

    # Declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]


# Specify the path to the folder containing the text files
folder_path = "/home/tvnguye1/CSCI533/Coding_assignment_2/test_folder/"

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if 'test1a' in filename:
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            test1a = file.read()
            print(f"Length 1a:", len(test1a))
            
    elif 'test1b' in filename:
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            test1b = file.read()
            print(f"Length 1b:", len(test1b))

    elif 'test2a' in filename:
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            test2a = file.read()
            print(f"Length 2a:", len(test2a))

    elif 'test2b' in filename:
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            test2b = file.read()
            print(f"Length 2b:", len(test2b))

    elif 'test3a' in filename:
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            test3a = file.read()
            print(f"Length 3a:", len(test3a))

    elif 'test3b' in filename:
        file_path = os.path.join(folder_path, filename)
        # Open the file for reading
        with open(file_path, 'r') as file:
            test3b = file.read()
            print(f"Length 3b:", len(test3b))

print("Naive")
start_time1 = time.time()
print ("Test 1: ", lcs_naive(test1a, test1b, len(test1a), len(test1b)))
end_time1 = time.time()
print("Running time test 1:", end_time1 - start_time1)

start_time2 = time.time()
print ("Test 2: ", lcs_naive(test2a, test2b, len(test2a), len(test2b)))
end_time2 = time.time()
print("Running time test 2:", end_time2 - start_time2)

print("Top Down")
start_time7 = time.time()
dp = [[-1 for i in range(len(test1b) + 1)]for j in range(len(test1a) + 1)] 
print(f"Length of LCS is {lcs_top_down(test1a, test1b, len(test1a), len(test1b), dp)}")
end_time7 = time.time()
print("Running time 1: ", end_time7 - start_time7)

start_time8 = time.time()
dp = [[-1 for i in range(len(test2b) + 1)]for j in range(len(test2a) + 1)] 
print(f"Length of LCS is {lcs_top_down(test2a, test2b, len(test2a), len(test2b), dp)}")
end_time8 = time.time()
print("Running time 2: ", end_time8 - start_time8)


print("Bottom Up")
start_time4 = time.time()
print("Test 1:", lcs_bottom_up(test1a, test1b, len(test1a), len(test1b))) 
end_time4 = time.time()
print("Running time 1: ", end_time4-start_time4)

start_time5 = time.time()
print("Length of LCS with DP is ", lcs_bottom_up(test2a, test2b, len(test2a), len(test2b))) 
end_time5 = time.time()
print("Running time 2: ", end_time5 - start_time5)


fractions = [100, 200, 500, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000]
for fraction in  fractions:
    print("Length:", fraction)
    start_time9 = time.time()
    dp = [[-1 for i in range(len(test3b[:fraction]) + 1)]for j in range(len(test3a[:fraction]) + 1)] 
    print(f"Length of LCS is {lcs_top_down(test3a[:fraction], test3b[:fraction], len(test3a[:fraction]), len(test3b[:fraction]), dp)}")
    end_time9 = time.time()
    print("Running time 3: ", end_time9 - start_time9)

    start_time6 = time.time()
    print("Length of LCS with DP is ", lcs_bottom_up(test3a[:fraction], test3b[:fraction], len(test3a[:fraction]), len(test3b[:fraction]))) 
    end_time6 = time.time()
    print("Running time 3: ", end_time6 - start_time6)
