import difflib


class Solution():
    """
    https://www.codewars.com/kata/5259510fc76e59579e0009d4

    I'm sure, you know Google's "Did you mean ...?",
    when you entered a search term and mistyped a word.
    In this kata we want to implement something similar.

    You'll get an entered term (lowercase string) and an array of known words (also lowercase strings).
    Your task is to find out, which word from the dictionary is most similar to the entered one.
    The similarity is described by the minimum number of letters you have to add,
    remove or replace in order to get from the entered word to one of the dictionary.
    The lower the number of required changes, the higher the similarity between each two words.

    Same words are obviously the most similar ones.
    A word that needs one letter to be changed is more similar to another word that
    needs 2 (or more) letters to be changed.
    E.g. the mistyped term
        berr is more similar to
        beer (1 letter to be replaced) than to
        barrel (3 letters to be changed in total).

    Extend the dictionary in a way,
    that it is able to return you the most similar word from the list of known words.

    Code Examples:

    I know, many of you would disagree that java is more similar to heaven than all the other ones,
    but in this kata it is ;)

    Additional notes:

        there is always exactly one possible solution
    """

    def __init__(self):
        pass

    def find_most_similar_01(self, term, words):

        def levenshtein(s1, s2):
            if len(s1) > len(s2):
                s1, s2 = s2, s1

            ds = range(len(s1) + 1)
            for i2, c2 in enumerate(s2):
                ds_next = [i2 + 1]
                for i1, c1 in enumerate(s1):
                    if c1 == c2:
                        ds_next.append(ds[i1])
                    else:
                        ds_next.append(1 + min((ds[i1], ds[i1 + 1], ds_next[-1])))
                ds = ds_next
            return ds[-1]

        dists = [levenshtein(term, word) for word in words]

        return words[dists.index(min(dists))]

    def find_most_similar_02(self, term, words):

        def levenshtein(s1, s2):
            if s1 == s2:
                return 0
            l1, l2 = len(s1), len(s2)
            if l1 == 0:
                return l2
            if l2 == 0:
                return l1
            v0 = range(l2 + 1)
            v1 = [0] * (l2 + 1)
            for i in range(l1):
                v1[0] = i + 1
                for j in range(l2):
                    cost = 0 if s1[i] == s2[j] else 1
                    v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
                v0 = list(v1)
            return v1[l2]

        dists = [levenshtein(term, word) for word in words]

        return words[dists.index(min(dists))]


if __name__ == '__main__':
    sol = Solution()
    words = ['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
    assert (sol.find_most_similar_02('strawbery', words) == 'strawberry')
    assert (sol.find_most_similar_02('berry', words) == 'cherry')
    assert (sol.find_most_similar_02('aple', words) == 'apple')
