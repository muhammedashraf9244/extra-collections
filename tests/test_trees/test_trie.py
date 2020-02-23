import pytest
from tests import *
from extra.trees.trie import TrieNode, Trie




def test_trienode():
    pass


def test_empty_trie():
    t = Trie()
    t.clear()
    assert len(t) == 1
    assert isinstance(t.root, TrieNode)
    assert t.root.get_data() == "ROOT"
    assert '' not in t
    assert get_string() not in t
    assert t.has_prefix('')
    assert t.auto_complete() == t.auto_complete('') \
        == t.auto_complete(get_string()) == []
    t.remove('')
    with pytest.raises(TypeError):
        t.insert(get_int())
        t.remove(get_list())
        get_float() in t
        t.has_prefix(get_int())
        t.auto_complete(get_list())
        



# def test_trie_simple():
#     t = Trie()
#     t.insert('a')
#     t.insert('A')
#     t.remove('AA')
#     print(t)


def test_trie_similar_words():
    t = Trie()
    t.insert("tre")
    t.insert("trees")
    t.insert("treed")
    t.remove("trees")
    t.remove("tre")
    assert len(t) == 6
    assert t.auto_complete("t") == ['treed']


def test_trie_many_words():
    t = Trie()
    t.insert('car')
    t.insert('card')
    t.insert('cards')
    t.insert('cot')
    t.insert('cots')
    t.insert('trie')
    t.insert('tried')
    t.insert('tries')
    t.insert('try')
    assert t.has_prefix('ca')
    assert len(t) == 16
    # explort Trie
    assert t.root.get_data() == "ROOT"
    assert t.root.get_child('t').get_data() == 't'
    assert list(t.root.get_child('c').get_characters()) == ['a', 'o']
    # test find() and get_cadidates()
    assert 'cards' in t
    assert 'c' not in t
    assert t.auto_complete() == \
        ['car', 'card', 'cards', 'cot', 'cots', 'trie', 'tried', 'tries', 'try']
    assert t.auto_complete('c') == ['car', 'card', 'cards', 'cot', 'cots']
    assert t.auto_complete('tri') == ['trie', 'tried', 'tries']
    assert t.auto_complete('caa') == []