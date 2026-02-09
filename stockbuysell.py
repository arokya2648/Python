#Program to find the max profit you can get from buying and selling stocks 
def calculateprofits(arr,arr_size):
    profit=0
    for i in range(1, arr_size):
        #if the current element is greater than last element then we will buy the p[revious day and sell the current day
        if arr[i]>arr[i-1]:
            #calculate profit
            profit+=arr[i]-arr[i-1]
    return profit
#prices for 7 days
prices=[635, 864, 247, 325, 257, 745, 245]
profit=calculateprofits(prices, len(prices))
print('Max Profit:', profit)