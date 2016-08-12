class Solution():
    """
    https://www.codewars.com/kata/51646de80fd67f442c000013

    Complete the method so that it does the following:

        Removes any duplicate query string parameters from the url
        Removes any query string parameters specified within the 2nd argument (optional array)

    Examples:

        stripUrlParams('www.codewars.com?a=1&b=2&a=2') // returns 'www.codewars.com?a=1&b=2'
        stripUrlParams('www.codewars.com?a=1&b=2&a=2', ['b']) // returns 'www.codewars.com?a=1'
        stripUrlParams('www.codewars.com', ['b']) // returns 'www.codewars.com'
    """

    def __init__(self):
        pass

    def strip_url_params_01(self, url, params_to_strip=[]):
        """
        left to right, append
        """
        if '?' not in url:
            return url

        host, params = url.split('?')
        if not params:
            return host

        params_stripped = []
        param_set = []
        for param in params.split('&'):
            n = param.split('=')[0]
            if n not in param_set and n not in params_to_strip:
                param_set.append(n)
                params_stripped.append(param)

        if params_stripped:
            return host + '?' + '&'.join(params_stripped)
        return host

    def strip_url_params_02(self, url, params_to_strip=[]):
        """
        right to left, pop
        """
        if '?' not in url:
            return url

        host, params = url.split('?')
        if not params:
            return host

        params = params.split('&')
        ns = [param.split('=')[0] for param in params]
        for i in range(len(params) - 1, -1, -1):
            if ns[i] in params_to_strip or ns[i] in ns[:i]:
                params.pop(i)

        if params:
            return host + '?' + '&'.join(params)
        return host


if __name__ == '__main__':
    sol = Solution()
    print(sol.strip_url_params_02('www.codewars.com?a=1&b=2&a=2'))
    print(sol.strip_url_params_02('www.codewars.com?a=1&b=2&a=2', ['b']))
    print(sol.strip_url_params_02('www.codewars.com?a=1&b=2&a=2', ['b', 'a']))
    print(sol.strip_url_params_02('www.codewars.com', ['b']))
