import parser as parse
import type_dictionary
import runtime

tests = [
    ['hello world', ['String']],
    ['"hello world"', ['String']],
    ['abc def eee ', ['String', 'String', 'String']],
    [' abc def  eee ', ['abc', 'def', 'eee']],
    ['"abc def" "123 456"', ['String', 'String']],
    ['abc "def" "123 " 456', ['String', 'String', 'String', 'Nat']],
    ['5.5 2.1 + 456', ['Real', 'Real', 'Word', 'Nat']],
    ['[5.5 2.1] .456 +', [[5.5, 2.1], 0.456, '+']],
    ['[[5.5 2.1] [1 2 3]] .456 +', [[[5.5, 2.1], [1, 2, 3]], 0.456, '+']],
    [' [ [5.5 2.1]  [1 2 3] ]  .456  +   ', [[[5.5, 2.1], [1, 2, 3]], 0.456, '+']],
    ['[["5.5" 2.1] [1 "2" 3]] .456 +', [[['5.5', 2.1], [1, '2', 3]], 0.456, '+']],
    [' [ ["5.5" 2.1]  [1 "2" "3 3"] ]  .456  +   ', [[['5.5', 2.1], [1, '2', '3 3']], 0.456, '+']],
    ['[4 5 +] ', [[4, 5, '+']]],
    ['[4 5 +] [4 5 +]', [[4, 5, '+'], [4, 5, '+']]],
    ['[4 5 +] [4 5 +] [4 5 +]', [[4, 5, '+'],[4, 5, '+'],[4, 5, '+']]],
    ['[4 5 +] foo [4 5 +]', [[4, 5, '+'], 'foo', [4, 5, '+']]],
    ['{a:5.5 b:2.1} .456 +', [{"a":5.5, "b":2.1}, 0.456, '+']],
    [' {a:5.5 b:2.1} .456 +', [{"a":5.5, "b":2.1}, 0.456, '+']],
    ['{ a:5.5 b:2.1} .456 +', [{"a":5.5, "b":2.1}, 0.456, '+']],
    [' { a:5.5  b:2.1 } .456 + { a:5.5  b:2.1 } ', [{"a":5.5, "b":2.1}, 0.456, '+', {"a":5.5, "b":2.1}]],
    ['{a:[1 2 3] 3b_g:{a:1 y:3}}', [{"a":[1, 2, 3], "3b_g":{"a":1, "y":3}}]],
    ['[{a:[1 2 "3"] 3b_g:{a:1 y:3}} abc] cdef', [[{"a":[1, 2, '3'], "3b_g":{"a":1, "y":3}}, 'abc'], 'cdef']],
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
    
print('Starting type check tests:')
testCount = 0
testsFailed = 0
for test in tests:
    ps = test[0]
    expected_stack = test[1]
    
    #print('starting parse test for: ', ps)
    ast = parse(ps)
    result_stack = type_checker(ast)
    testCount += 1
    if not cmpLists(result_stack, expected_stack):
        testsFailed += 1
        print(result_stack, ' expected:', expected_stack)
        print('---- Failed parse test for: ', ps)
if testsFailed == 0:
    print('All', testCount, 'tests passed.')