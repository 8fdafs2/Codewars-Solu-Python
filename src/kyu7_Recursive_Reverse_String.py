'''
Created on May 8, 2016

@author: ray.wang
'''
def reverse(str):
    return str[-1] + reverse(str[:-1]) if len(str) >= 2 else str



if __name__ == '__main__':
    
    assert(reverse("h") == "h")
    assert(reverse("he") == "eh")
    assert(reverse("hello world") == "dlrow olleh")