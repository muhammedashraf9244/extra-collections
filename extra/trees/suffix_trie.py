"""
Suffix trees store information about a single string and exports a huge amount
of structural information about that string.
"""
from abc import abstractmethod
from extra.interface import Extra
from extra.trees.radix_trie import TrieNode, RadixTrie




def lcp(word1, word2):
    # NOTE: LCP stands for Longest Common Prefix
    assert type(word1)==str and type(word2)==str
    assert len(word1)>0 and len(word2)>0

    for i in range(min(len(word1), len(word2))):
        if word1[i] != word2[i]:
            return word1[:i]
    return word1 if len(word1) < len(word2) else word2




class SuffixTrie(Extra):
    def __name__(self):
        return "extra.SuffixTrie"

    
    def __init__(self, word):
        super()._validate_item(word)
        if type(word) != str:
            raise TypeError(f"Can't insert {type(word)} into {self.__name__()}")
        elif len(word) == 0:
            raise ValueError(\
                f"An empty string can't be inserted to {self.__name__()}!!")
        
        # Ukkonen's algorithm
        self._word = word.replace('$', '')
        # dictionary containing suffix-index as key and leaf nodes as values 
        self._leaf_nodes = {}
        # SuffixTrie is basically a RadixTrie
        self._rt = RadixTrie()
        for idx in range(len(self._word)):
            leaf_node = self._rt._insert(self._word[idx:] + "$ ⟶ " + str(idx))
            self._leaf_nodes[idx] = leaf_node
        self._leaf_nodes[idx] = self._rt._insert("$ ⟶ " + str(idx))


    def __repr__(self):
        return str(self._rt)


    def __len__(self):
        return len(self._rt)


    def has_substr(self, substr):
        return self._rt.has_prefix(substr)


    ##############################     LCS/LRS    ##############################
    def __get_deepest_nodes(self):
        if self._rt.is_empty():
            return self._rt._root
        level_nodes = \
            self._rt._get_nodes_per_level(self._rt._root, 0, [], False)
        if len(level_nodes) > 2:
            return level_nodes[-1] + level_nodes[-2]
        return level_nodes[-1]


    def _get_ancestors_data(self, node):
        assert type(node) is TrieNode

        ancestors_data = []
        parent = node.get_parent()
        while(parent is not self._rt._root):
            parent_data = parent.get_data()
            ancestors_data.append(parent_data)
            parent = parent.get_parent()
        return "".join(ancestors_data[::-1])


    def get_longest_common_substring(self):
        if self._rt.is_empty():
            return []
        lcs_set = set()
        longest_length = 0
        for node in self.__get_deepest_nodes():
            lcs = self._get_ancestors_data(node)            
            longest_length = max(longest_length, len(lcs))
            lcs_set.add(lcs)
        # return the longest ones
        return [substr for substr in lcs_set if len(substr) == longest_length]


    def get_longest_repeated_substring(self):
        # LRS is the longest substring that occurs at least twice.
        return self.get_longest_common_substring()

    
    ##############################    MATCHING    ##############################
    def count_pattern_occurrences(self, pattern):
        if type(pattern) != str:
            return 0
        last_node, remaining = self._rt._follow_path(pattern)
        if remaining:
            child = last_node.get_child(remaining[0])
            child_data = child.get_data() if child else ''
            if child_data[:len(remaining)] == remaining:
                last_node = child
            else:
                return 0
        if last_node == self._rt._root:
            return 0
        return self._rt._count_leaf_nodes(last_node)


    def get_longest_palindrome(self):
        pass


    def get_lowest_common_ancestor(self, i, j):
        if type(i) != int or type(j) != int:
            raise TypeError("`i` and `j` should be integer values!!")
        elif i < 0 or j < 0 :
            raise ValueError("`i` and `j` should be postive integer values!!")
        elif i >= len(self._word) or j >= len(self._word):
            raise ValueError(\
                f"`i` and `j` values can't exceed {len(self._word)} " + 
                f"since it is the length of given word `{self._word}`!!"
            )


        
        
       

    def to_suffix_array(self):
        pass








if __name__ == "__main__":
    # st = SuffixTrie("ATCGATCGA")
    # print(st)
    # # print(st.get_longest_repeated_substr())
    # print("Total Nodes:", len(st))


    # st = SuffixTrie("minimize")
    # print(st)
    # print("Total Nodes:", len(st))
    # print(st.has_suffix('ize'))    

    # st = SuffixTrie("nonsense")
    # print(st)
    # print("Total Nodes:", len(st))
    # print(st.get_lcs())


    # st = SuffixTrie("PAPERSFORPAPERS")
    # print(st)
    # print(st.get_longest_common_substring())
    # print(st.count_pattern_occurrences('P'))



    st = SuffixTrie("banana")
    # print(st.get_longest_common_substring())
    print(st.get_lowest_common_ancestor(2, 4))
    # print(st)