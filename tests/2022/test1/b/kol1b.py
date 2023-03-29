from kol1btesty import runtests

def make_word_arr(word: str) -> list:
    r = ord('a')
    res = [0]*26

    for char in word:
        res[ord(char)-r] += 1
    
    return res

def find_max_letter_quantity(arr: list) -> int:
    max_q = 0
    for j in range(26):
        for i in range(len(arr)):
            max_q = (max_q if max_q > arr[i][j] else arr[i][j]) 
    
    return max_q

def counting_sort(arr: list, quant: int, letter: int) -> None:
    n = len(arr)
    count = [0]*(quant+1)
    res = [[]]*n

    for i in range(n):
        count[arr[i][letter]] += 1
    
    for i in range(1, quant+1):
        count[i] += count[i-1]
    
    for i in range(n-1, -1, -1):
        res[count[arr[i][letter]]-1] = arr[i]
        count[arr[i][letter]] -= 1
    
    for i in range(n):
        arr[i] = res[i]

def f(arr: list) -> int:
    word_arr = [make_word_arr(word) for word in arr]
    quant = find_max_letter_quantity(word_arr)

    for letter in range(26-1, -1, -1):
        counting_sort(word_arr, quant, letter)
    
    max_pop = 0
    curr_pop = 1
    for i in range(1, len(word_arr)):
        if word_arr[i] == word_arr[i-1]:
            curr_pop += 1
        else:
            max_pop = (max_pop if max_pop > curr_pop else curr_pop)
            curr_pop = 1
    
    return (max_pop if max_pop > curr_pop else curr_pop)




#Ostateczna złożoność O(NlogN)

# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )

# T = ["tygrys", "kot", "wilk", "trysyg", "wlik", "sygryt", "likw", "tygrys"]
# print(f(T))