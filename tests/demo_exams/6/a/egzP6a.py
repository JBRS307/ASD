from egzP6atesty import runtests

def buckets_spread(passwords: list, buckets: list, n: int) -> None:
    max_len = 0
    min_len = float('inf')
    for passwd in passwords:
        leng = len(passwd)
        max_len = (leng if leng > max_len else max_len)
        min_len = (leng if leng < min_len else min_len)
    
    b_range = (max_len-min_len)/n
    if(min_len == max_len):
        for passwd in passwords:
            buckets[n-1].append(passwd)
        return

    for passwd in passwords:
        leng = len(passwd)
        diff = (leng-min_len)/b_range - int((leng-min_len)/b_range)
        if diff < 0.0000001 and leng != min_len:
            buckets[int((leng-min_len)/b_range - 1)].append(passwd)
        else:
            buckets[int((leng-min_len)/b_range)].append(passwd)

def count_letters(passwd: str) -> int:
    letters = 0
    for c in passwd:
        if c >= 'a' and c <= 'z':
            letters += 1
    return letters

def spread_buckets_by_letters(arr: list, buckets: list, n: int) -> None:
    max_letters = 0
    min_letters = float('inf')
    for passwd in arr:
        letters =  count_letters(passwd)
        max_letters = (letters if letters > max_letters else max_letters)
        min_letters = (letters if letters < min_letters else min_letters)
    
    b_range = (max_letters - min_letters)/n

    if min_letters == max_letters:
        for passwd in arr:
            buckets[n-1].append(passwd)
        return

    for passwd in arr:
        letters = count_letters(passwd)
        diff = (letters - min_letters)/b_range - int((letters - min_letters)/b_range)
        if diff < 0.0000001 and letters != min_letters:
            buckets[int((letters - min_letters)/b_range - 1)].append(passwd)
        else:
            buckets[int((letters - min_letters)/b_range)].append(passwd)

def google (passwords: list, s: int) -> str:
    n = len(passwords)
    buckets = [[] for _ in range(n)]
    buckets_spread(passwords, buckets, n)

    passwd_counter = 0
    for i in range(n-1, -1, -1):
        passwd_counter += len(buckets[i])
        if passwd_counter >= s:
            good_bucket = buckets[i]
            s_new = s-(passwd_counter-len(buckets[i]))
            break
    
    buckets = [[] for _ in range(len(good_bucket))]
    spread_buckets_by_letters(good_bucket, buckets, len(good_bucket))

    passwd_counter = 0
    for i in range(len(good_bucket)-1, -1, -1):
        passwd_counter += len(buckets[i])
        if passwd_counter >= s_new:
            return buckets[i][0]





runtests ( google, all_tests=True )

# H = ['aba', 'abc', 'ab1', 'abab', 'a1a1', 'aa12a'] 
# s = 3

# print(google(H, s))