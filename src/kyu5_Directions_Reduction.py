class Solution():
    def __init__(self):
        self.dirReduc = self.dirReduc_01

    def dirReduc_01(self, arr):
        ret = list(arr)
        dir_pair = {
            "NORTH": "SOUTH",
            "SOUTH": "NORTH",
            "EAST": "WEST",
            "WEST": "EAST"
        }
        while True:
            len_ret = len(ret)
            for i in range(len(ret) - 1):
                if dir_pair[ret[i]] == ret[i + 1]:
                    ret.pop(i)
                    ret.pop(i)
                    break
            if len(ret) == len_ret:
                return ret

    def dirReduc_02(self, arr):
        ret = []
        dir_pair = {
            "NORTH": "SOUTH",
            "SOUTH": "NORTH",
            "EAST": "WEST",
            "WEST": "EAST"
        }
        for _dir_ in arr:
            if ret and ret[-1] == dir_pair[_dir_]:
                ret.pop()
            else:
                ret.append(_dir_)

        return ret

    def dirReduc_03(self, arr):
        ret = ' '.join(arr)

        while True:
            len_arr = len(ret)
            ret = ret.replace(
                'NORTH SOUTH', '').replace(
                'SOUTH NORTH', '').replace(
                'EAST WEST', '').replace(
                'WEST EAST', '')
            ret = ' '.join(ret.split())
            if len_arr == len(ret):
                return ret.split()


if __name__ == '__main__':
    sol = Solution()
    print((sol.dirReduc_03(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])))
