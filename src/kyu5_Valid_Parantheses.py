'''
Created on May 8, 2016

@author: ray.wang
'''


def valid_parentheses(string):
    counter = 0

    for char in string:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
        else:
            pass

        if counter < 0:
            return False

    if counter != 0:
        return False

    return True


if __name__ == '__main__':
    assert (valid_parentheses("()") == True)
    assert (valid_parentheses(")(()))") == False)
    assert (valid_parentheses("(") == False)
    assert (valid_parentheses("(())((()())())") == True)

    assert (valid_parentheses("  (") == False)
    assert (valid_parentheses(")test") == False)
    assert (valid_parentheses("") == True)
    assert (valid_parentheses("hi())(") == False)
    assert (valid_parentheses("hi(hi)()") == True)
