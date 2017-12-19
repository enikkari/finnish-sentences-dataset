# Eeva Nikkari

debug = False
def dd(s: str):
    if debug:
        print(s)

class TrieJumper:

    def __init__(self):
        self.root = Leaf(' ')

    def add_word(self, word: str):
        in_leaf = self.root
        for c in word:
            next_leaf = in_leaf.child_with_value(c)
            if next_leaf is None:
                dd('add child')
                in_leaf = in_leaf.add_child(c)
            else:
                dd('go to next leaf')
                in_leaf = next_leaf
        in_leaf.add_child('END')

    #jump over word if it's contained in the trie
    # return 0 if not contains, else return the length
    def make_jump(self, leftower_of_text: str) -> int:
        in_leaf = self.root
        i = 0
        while i < len(leftower_of_text):
            char_now = leftower_of_text[i]
            next_leaf = in_leaf.child_with_value(char_now)
            if(next_leaf is not None):
                i+=1
                in_leaf = next_leaf
                dd(in_leaf == next_leaf)
            else:
                break

        # check if we came to an end of a word
        if(in_leaf.child_with_value('END')):
            dd("in leaf")
            dd(in_leaf.value)
            dd([c.value for c in in_leaf.children])
            dd(in_leaf.children)
            return i
        else:
            return 0

class Leaf():
    def __init__(self, value):
        self.value = value
        self.children = list()

    def add_child(self, value):
        new_child = Leaf(value.lower())
        self.children.append(new_child)
        dd('add child')
        dd([c.value for c in self.children])
        #self.children = sorted(self.children, lambda child: child.value())
        return new_child

    def child_with_value(self, value):
        for child in self.children:
            if child.value == value.lower():
                dd("return:" + str(child))
                dd("child children")
                dd(child.children)
                return child
        return None

if __name__ == '__main__':
    segmenter = TrieJumper()
    segmenter.add_word('esim.')
    segmenter.add_word('<d>.<d>.<d>')

    print(segmenter.make_jump("esim. kotona"))
    print(segmenter.make_jump("esi kotona"))
    print(segmenter.make_jump("Esim. kotona"))
    print(segmenter.make_jump("<d>.<d>.<d> jälkeen"))
    print(segmenter.make_jump("as <d>.<d>.<d> jälkeen"))
    print(segmenter.make_jump("as <d>. jälkeen"))

    print(segmenter.make_jump("Testilause. jälkeen esim."))

    l1 = Leaf('a')
    l2 = l1.add_child('b')
    l22 = l1.add_child('bb')
    l23 = l22.add_child('ab')
    print(l1.value)
    print(l1.child_with_value('b'))
    print(l1.child_with_value('ads') is None)
    print([c.value for c in l1.children])
    print([c.value for c in l22.children])
    print(l23.value)