def _compose(s, pl):
    global words
    # usage: [phrase] [new-word-name] compose
    new_word = s.pop()
    new_definition = s.pop()
    words[new_word] = new_definition
    return [s, pl]
def _pounce(s, pl):
    global words
    # [param1 param2] [phrase] [new-word] define
    new_word = s.pop()
    definition = s.pop()
    params = s.pop()
    # replace 
    words[new_word] = new_definition
    return [s, pl]
def _dup(s, pl):
    a = s[-1]
    s.append(a)
    return [s, pl]
def _add(s, pl):
    a = s.pop()
    b = s.pop()
    s.append(a + b)
    return [s, pl]
def _sub(s, pl):
    a = s.pop()
    b = s.pop()
    s.append(b - a)
    return [s, pl]
def _mult(s, pl):
    a = s.pop()
    b = s.pop()
    s.append(a * b)
    return [s, pl]
def _divide(s, pl):
    a = s.pop()
    b = s.pop()
    s.append(int(a / b))
    return [s, pl]
def _n_prod(s, pl):
    if len(s) >= 2:
        a = s.pop()
        b = s.pop()
        if isNumber(a) and isNumber(b):
            s.append(a * b)
            pl.insert(0, 'n*')
            return [s, pl]
        else:
            s.append(b)
            s.append(a)
    return [s, pl];
def _eq(s, pl):
    a = s.pop()
    b = s.pop()
    s.append(a == b)
    return [s, pl]
def _gt(s, pl):
    a = s.pop()
    b = s.pop()
    s.append(b > a)
    return [s, pl]
def _lt(s, pl):
    a = s.pop()
    b = s.pop()
    s.append(b < a)
    return [s, pl]
def _ift(s, pl):
    then_block = s.pop()
    expression = s.pop()
    if expression:
        if isArray(then_block):
            pl = then_block+pl
        else:
            pl.insert(0, then_block)
    return [s, pl]
def _ifte (s, pl):
    else_block = s.pop()
    then_block = s.pop()
    expression = s.pop()
    if expression:
        if isArray(then_block):
            #print(then_block)
            pl = then_block+pl
        else:
            pl.insert(0, then_block)
    else:
        if isArray(else_block):
            pl = else_block+pl
        else:
            pl.insert(0, else_block)
    return [s, pl]
def _get(s, l): # (dict key -- dict value)
    key = s.pop()
    dictionary = s[-1]
    s.append(dictionary[key])
    return [s, l]
def _set(s, l): # (dict value key -- dict)
    key = s.pop()
    value = s.pop()
    dictionary = s[-1]
    dictionary[key] = value
    return [s, l]
def _apply(s, l): # (dict key fun -- dict)
    fun = s.pop()
    key = s[-1]
    #l.insert(0, ['get', fun, key, 'set'])
    l.insert(0, 'set')
    l.insert(0, key)
    l = fun+l                                     # concat arrays so that the program list (l) has words on it, not a list
    l.insert(0, 'get')
    return [s, l]
def _swap(s, l):
    a = s.pop()
    b = s.pop()
    s.append(a)
    s.append(b)
    return [s, l]
def _drop(s, l):
    a = s.pop()
    return [s, l]
def _dip(s, l):
    f = s.pop()
    a = s.pop()
    l.insert(0, a)
    l = f+l
    return [s, l]

words = {
  'compose': _compose,
  'pounce': _pounce,
  'dup': _dup,
  '+': _add,
  '-': _sub,
  '*': _mult,
  '/': _divide,
  'n*': _n_prod,
  '==': _eq,
  '<': _lt,
  '>': _gt,
  'if': _ift,
  'if-else': _ifte,
  'get': _get,
  'set': _set,
  'app': _apply,
  'swap': _swap,
  'drop': _drop,
  'dip': _dip
}

