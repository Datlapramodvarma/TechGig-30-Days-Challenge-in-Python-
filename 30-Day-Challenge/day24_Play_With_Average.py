def main():
    n = int(input())
    arr = list(map(int,input().split()))
    even,odd,oc,ec = 0,0,0,0
    for i in range(n):
        if arr[i] % 2 == 0:
            ec += 1
            even += arr[i]
        else:
            odd += arr[i]
            oc += 1
    if ec>0:
        even_avg = round(even/ec)
    else:
        even_avg=0
    if oc>0:
        odd_avg = round(odd/oc )
    else:
        odd_avg = 0
    print(odd_avg+even_avg)
main()

