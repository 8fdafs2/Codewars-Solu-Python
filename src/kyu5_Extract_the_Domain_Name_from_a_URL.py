import re

class Solution():
    """
    https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1

    Write a function that when given a URL as a string,
    parses out just the domain name and returns it as a string. For example:

    domain_name("http://github.com/carbonfive/raygun") == "github"
    domain_name("http://www.zombie-bites.com") == "zombie-bites"
    domain_name("https://www.cnet.com") == "cnet"
    """
    def __init__(self):
        pass

    def domain_name_01(self, url):
        """
        """
        url = url.split('/')
        return url[0 if len(url) == 1 else 2].split('.')[-2]

    def domain_name_02(self, url):
        """
        """
        return url.split('//')[-1].split('/')[0].split('.')[-2]

    def domain_name_03(self, url):
        """
        """
        result = re.search(r"(//)?((?P<domain>\w+)\.)+", url)
        return result.group('domain') if result else None

    def domain_name_04(self, url):
        """
        """
        result = re.search(r"(//)?(\w+\.)?(?P<domain>\w+)\.", url)
        return result.group('domain') if result else None


if __name__ == '__main__':
    sol = Solution()
    print(sol.domain_name_04("http://github.com/carbonfive/raygun"))
    print(sol.domain_name_04("www.xakep.ru"))
    print(sol.domain_name_04("https://youtube.com"))
    print(sol.domain_name_04("https://www.cnet.com"))
    print(sol.domain_name_04("http://github.com/carbonfive/raygun"))
    print(sol.domain_name_04("http://www.zombie-bites.com"))
