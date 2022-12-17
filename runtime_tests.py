from pounce_parser import parse
from runtime import purr

tests = [
    ['hello world', ['hello', 'world']],
    ['"hello world"', ['hello world']],
    ['abc def eee ', ['abc', 'def', 'eee']],
    [' abc def  eee ', ['abc', 'def', 'eee']],
    ['"abc def" "123 456"', ['abc def', "123 456"]],
    ['abc "def" "123 " 456', ['abc', 'def', "123 ", 456]],
    ['5.5 2.1 +', [7.6]],
    ['5.5 2.1 + 456', [7.6, 456]],
    ['', []],
    ['4 5 [a b] [b a /] pounce', [1.25]],
    ['3 [a] [1 a /] crouch', [[1, 3, '/']]],
    ['1 2 dup', [1, 2, 2]],
    ['3 dup dup', [3, 3, 3]],
    ['1 3 5 [dup] dip', [1, 3, 3, 5]],
    ['1 dup 1 +', [1, 2]],
    ['[1] dup 0 get 1 + 0 set', [[1], [2]]], # make sure a copy was made 
    ['3 5 -', [-2]],
    ['7 6 *', [42]],
    ['8 3 /', [2.6666666666666665]],
    ['8 3 %', [2]],
    ['7 7 ==', [1]],
    ['8 -1 > 7 7 > 7 17 >', [1, 0, 0]],
    ['8 -1 < 7 7 < 7 17 <', [0, 0, 1]],
    ['1 [a] if', ['a']],
    ['0 [a] if', []],
    ['1 [a] [b] ifte', ['a']],
    ['0 [a] [b] ifte', ['b']],
    ['[1 2 3] 1 get', [[1, 2, 3], 2]],
    ['[1 2 3] 5 1 set', [[1, 5, 3]]],
    ['3 [1 +] leap', [4]],
    ['[a] 8 swap', [8, ['a']]],
    ['4 5 drop', [4]],
    ['4 5 [drop] dip', [5]],
]

def cmpLists(a, b):
    same = True
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                same = False
    else:
        same = False
    return same
    
print('Starting runtime tests:')
testCount = 0
testsFailed = 0
for test in tests:
    ps = test[0]
    expected_stack = test[1]
    
    # print('starting purr test for: ', ps)
    result_stack = purr(parse(ps))
    testCount += 1
    if not cmpLists(result_stack, expected_stack):
        testsFailed += 1
        print('---- Failed purr test for: ', ps)
        print('hmmm got:', result_stack, ' when expecting:', expected_stack)
        print('---- ')
        break
if testsFailed == 0:
    print('All', testCount, 'tests passed.')