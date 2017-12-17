# Eeva Nikkari

class TrieJumper:

    def __init__(self):
        self.root = Leaf('')

    def add_word(self, word: str):
        in_leaf = self.root
        for c in word:
            next_leaf = in_leaf.child_with_value(c)
            if next_leaf is None:
                in_leaf = in_leaf.add_child(c)
            else:
                in_leaf = next_leaf
        in_leaf.add_child('END')

    #jump over word if it's contained in the trie
    # return 0 if not contains, else return the length
    def make_jump(self, leftower_of_text: str) -> int:
        in_leaf = self.root
        i = 0
        while True:
            char_now = leftower_of_text[i]
            next_leaf = in_leaf.child_with_value(char_now)
            if(next_leaf is not None):
                i+=1
                in_leaf = next_leaf
            else:
                break

        # check if we came to an end of a word
        if(in_leaf.child_with_value('END')):
            return i
        else:
            return 0

class Leaf():
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def add_child(self, value):
        new_child = Leaf(value.lower())
        self.children.append(new_child)
        #self.children = sorted(self.children, lambda child: child.value())
        return new_child

    def child_with_value(self, value):
        for child in self.children:
            if child.value == value.lower():
                return child
        return None

if __name__ == '__main__':
    segmenter = TrieJumper()
    segmenter.add_word('esim.')
    segmenter.add_word('<d>.<d>.<d>')

    print(segmenter.make_jump("esim. kotona"))
    print(segmenter.make_jump("Esim. kotona"))
    print(segmenter.make_jump("<d>.<d>.<d> jälkeen"))

    # l1 = Leaf('a')
    # l2 = l1.add_child('b')
    # l22 = l1.add_child('bb')
    # print(l1.value)
    # print(l1.child_with_value('b'))
    # print(l1.child_with_value('ads') is None)
    # print(l1)