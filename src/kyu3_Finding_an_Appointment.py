from itertools import chain
from functools import reduce


class Solution():
    """
    The businesspeople among you will know that it's often not easy to find an appointment.
    In this kata we want to find such an appointment automatically.
    You will be given the calendars of our businessperson and a duration for the meeting.
    Your task is to find the earliest time, when every businessperson is free for at least that duration.

    Example Schedule:

    Person | Meetings
    -------+-----------------------------------------------------------
         A | 09:00 - 11:30, 13:30 - 16:00, 16:00 - 17:30, 17:45 - 19:00
         B | 09:15 - 12:00, 14:00 - 16:30, 17:00 - 17:30
         C | 11:30 - 12:15, 15:00 - 16:30, 17:45 - 19:00

    Rules:

        All times in the calendars will be given in 24h format "hh:mm", the result must also be in that format
        A meeting is represented by its start time (inclusively) and end time (exclusively) ->
            if a meeting takes place from 09:00 - 11:00, the next possible start time would be 11:00
        The businesspeople work from 09:00 (inclusively) - 19:00 (exclusively),
            the appointment must start and end within that range
        If the meeting does not fit into the schedules, return null or None as result
        The duration of the meeting will be provided as an integer in minutes

    Following these rules and looking at the example above the earliest time for a 60 minutes meeting would be 12:15.

    Data Format:

        The schedule will be provided as 3-dimensional array. The schedule above would be encoded this way:
    """

    def __init__(self):
        pass

    def get_start_time_01(self, schedules, duration):
        """
        recursion, duration overlay calc
        """

        def to_minute(t):
            return int(t[:2]) * 60 + int(t[-2:])

        def duration_overlay_of(t_pair1, t_pair2):
            t_s1, t_e1 = t_pair1
            t_s2, t_e2 = t_pair2
            t_s1, t_e1 = to_minute(t_s1), to_minute(t_e1)
            t_s2, t_e2 = to_minute(t_s2), to_minute(t_e2)
            return max(t_e1, t_e2) - min(t_s1, t_s2) - abs(t_s1 - t_s2) - abs(t_e1 - t_e2)

        t_tables = []
        for schedule in schedules:
            n = len(schedule)
            if n == 0:
                sub = [['09:00', '19:00'], ]
            else:
                sub = [['09:00', schedule[0][0]], ]
                for i in range(n - 1):
                    sub.append([schedule[i][1], schedule[i + 1][0]])
                sub.append([schedule[-1][1], '19:00'])
            t_tables.append(sub)

        def recur(t_pair, t_tables):
            n = len(t_tables)
            for t_pair_ in t_tables[0]:
                if duration_overlay_of(t_pair, t_pair_) >= duration:
                    if n == 1:
                        return max(t_pair[0], t_pair_[0])
                    ret = recur((max(t_pair[0], t_pair_[0]), min(t_pair[1], t_pair_[1])), t_tables[1:])
                    if ret is not None:
                        return ret

        return recur(['09:00', '19:00'], t_tables)

    def get_start_time_02(self, schedules, duration):
        """
        global minutes table
        """

        def to_minute(time):
            return int(time[:2]) * 60 + int(time[-2:])

        def from_minute(minute):
            return '{:02d}:{:02d}'.format(*divmod(minute, 60))

        m_t = 60 * 24

        free_minutes = [1, ] * m_t
        for schedule in schedules:
            for meeting in schedule:
                for i in range(to_minute(meeting[0]), to_minute(meeting[1])):
                    free_minutes[i] = 0

        for i in range(9 * 60, 19 * 60 - duration + 1):
            if all(free_minutes[i: i + duration]):
                return from_minute(i)

    def get_start_time_03(self, schedules, duration):
        """
        global minutes table, mod
        """
        m_o = 9 * 60
        m_t = (19 - 9) * 60

        def to_minute(time):
            return int(time[:2]) * 60 + int(time[-2:]) - m_o

        def minutes_bw(time_pair):
            return range(to_minute(time_pair[0]), to_minute(time_pair[1]))

        def from_minute(minute):
            return '{:02d}:{:02d}'.format(*divmod(minute + m_o, 60))

        free_minutes = [1, ] * m_t
        for schedule in schedules:
            for meeting in schedule:
                for i in minutes_bw(meeting):
                    free_minutes[i] = 0

        i = 0
        while 1 in free_minutes:
            i1 = free_minutes.index(1)
            free_minutes = free_minutes[i1:]
            if 0 not in free_minutes:
                i0 = len(free_minutes)
            else:
                i0 = free_minutes.index(0)
            free_minutes = free_minutes[i0:]

            if i0 >= duration:
                return from_minute(i + i1)
            i += i1 + i0

    def get_start_time_04(self, schedules, duration):
        """
        itertools.chain
        """

        def to_minute(time):
            return int(time[:2]) * 60 + int(time[-2:])

        t = 9 * 60
        for (m_s, m_e) in (
                    sorted((to_minute(meeting[0]), to_minute(meeting[1])) for meeting in chain(*schedules)) +
                    [(19 * 60, 24 * 60), ]
        ):
            if m_s - t >= duration:
                return '{:02d}:{:02d}'.format(*divmod(t, 60))
            t = max(t, m_e)

    def get_start_time_05(self, schedules, duration):
        """
        global minutes table
        """
        m_o = 9 * 60
        m_t = (19 - 9) * 60

        def fuse(list1, list2):
            return [a or b for a, b in zip(list1, list2)]

        def to_minute(t):
            return int(t[:2]) * 60 + int(t[-2:]) - m_o

        def busy(meeting):
            m_s, m_e = map(to_minute, meeting)
            return [0, ] * m_s + [1, ] * (m_e - m_s) + [0, ] * (m_t - m_e)

        common = reduce(fuse, [busy(meeting) for schedule in schedules for meeting in schedule],
                        [0, ] * m_t)
        result = ''.join(map(str, common)).find(duration * "0")

        if result >= 0:
            return '{:02d}:{:02d}'.format(*divmod(result + m_o, 60))


def sets_gen(get_start_time):
    import random

    def min2str(minute):
        return '{:02d}:{:02d}'.format(*divmod(minute, 60))

    test_sets = []
    for i in range(100):
        schedules = []
        for _ in range(random.randint(2, 6)):
            schedule = []
            k_max = random.randint(0, 5)
            if k_max > 0:
                m_s = 9 * 60
                m_d = (19 - 9) * 60 // k_max
                m_e = m_s + m_d
                for k in range(k_max):
                    m_s = s = random.randint(m_s, m_e - 15)
                    m_s = e = random.randint(m_s + 5, m_e)
                    m_e += m_d
                    schedule.append([min2str(s), min2str(e)])
            schedules.append(schedule)

        duration = random.randint(30, 90)
        match = get_start_time(schedules, duration)

        test_sets.append((
            (schedules, duration),
            match
        ))

    return test_sets


if __name__ == '__main__':
    sol = Solution()
    from test_fixture import Test_Fixture

    tf = Test_Fixture(sol, sets_gen)
    tf.prep()
    tf.test(prt_docstr=False)
    tf.test_spd(100, prt_docstr=True)
