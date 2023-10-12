def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0

    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)
    else:
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
                   knapSack(W, wt, val, n - 1))

n = int(input("Enter the number of items: "))
val = list(map(int, input("Enter the values of the items separated by spaces: ").split()))
wt = list(map(int, input("Enter the weights of the items separated by spaces: ").split()))
W = int(input("Enter the knapsack capacity: "))

print("Maximum value in the knapsack:", knapSack(W, wt, val, n))
