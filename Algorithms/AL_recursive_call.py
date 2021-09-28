def factorial(n):
    if n > 0:
        return n*factorial(n-1)
    elif n == 0:
        return 1
    else:
        return n*factorial(n+1)

def list_sum(list):
    if len(list) == 0:
        return 0
    return list[0] + list_sum(list[1:])

def is_palindrome(str):
    if len(str) == 0:
        return True
    else:
        if str[0] == str[-1]:
            return is_palindrome(str[1:-1])
        else:
            return False

def recursive_prac(n):
    print(n)
    if n == 1:
        return 
    if n % 2 == 1:
        val = 3 * n + 1
        recursive_prac(val)
    else:
        val = int(n // 2)
        recursive_prac(val)

def sum_of_123(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return sum_of_123(n-3) + sum_of_123(n-2) + sum_of_123(n-1)

if __name__ == '__main__':
    def test(func, data_list):
        print('test:', func)
        for data in data_list:
            print('f(%s) = %s'%(data, func(data)))
    
    test(factorial, [-1,-2,-3,0,1,2,3,4,5])
    test(list_sum, [[1,2,3,4,5],[0,1,-1,2,-2]])
    test(is_palindrome, ['', 'a','abcba','snake','ssss','level'])
    test(recursive_prac, [3, 4])
    test(sum_of_123, [4, 5, 6, 7, 15])