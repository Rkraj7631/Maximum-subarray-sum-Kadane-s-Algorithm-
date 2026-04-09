def kadane(lst):
    max_sum=0
    sum=0

    for i in range(len(lst)):
        sum=lst[i]+sum
        max_sum=max(max_sum,sum)

        if sum <0:
            sum=0
    return max_sum

lst=list(map(int, input("Enter numbers Using Space : ").split()))

print("Maximum subarry Sum : ", kadane(lst))
