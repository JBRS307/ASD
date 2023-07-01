def binary_check(start, end):
    if start > end:
        return
    mid = (start+end)//2
    print(mid)
    binary_check(start, mid-1)
    binary_check(mid+1, end)

if __name__ == "__main__":
    N = 10000

    binary_check(0, N)

