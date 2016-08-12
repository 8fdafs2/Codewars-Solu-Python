class Solution():
    def __init__(self):
        self.format_duration = self.format_duration_01

    def format_duration_01(self, seconds):
        if seconds == 0:
            return 'now'
        years, seconds = divmod(seconds, 365*24*60*60)
        days, seconds = divmod(seconds, 24*60*60)
        hours, seconds = divmod(seconds, 60*60)
        minutes, seconds = divmod(seconds, 60)
        ret = []
        if years != 0:
            ret.append('{} year{}'.format(years, '' if years == 1 else 's'))
        if days != 0:
            ret.append('{} day{}'.format(days, '' if days == 1 else 's'))
        if hours != 0:
            ret.append('{} hour{}'.format(hours, '' if hours == 1 else 's'))
        if minutes != 0:
            ret.append('{} minute{}'.format(minutes, '' if minutes == 1 else 's'))
        if seconds != 0:
            ret.append('{} second{}'.format(seconds, '' if seconds == 1 else 's'))
        if len(ret) > 1:
            return ', '.join(ret[:-1]) + ' and ' + ret[-1]
        return ret[-1]
