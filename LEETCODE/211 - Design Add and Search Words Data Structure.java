class TrieNode {
    TrieNode[] children;
    boolean hasWord;
    
    public TrieNode() {
        children = new TrieNode[26];
        hasWord = false;
    }
    
    public void insert(String word, int index) {
        if (index == word.length()) {
            hasWord = true;
            return;
        }
        int p = word.charAt(index) - 'a';
        if (children[p] == null) {
            children[p] = new TrieNode();
        }
        children[p].insert(word, index + 1);
    }
    
    public boolean find(String word, int index) {
        if (index == word.length()) {
            return this.hasWord == true;
        }
        char c = word.charAt(index);
        if (c != '.') {
            int p = c - 'a';
            if (children[p] == null) return false;
            return children[p].find(word, index + 1);
        } else if (c == '.') {
            for (int i = 0; i < 26; i++) {
                if (children[i] != null) {
                    boolean temp = children[i].find(word, index + 1);
                    if (temp) {
                        return true;
                    } 
                }
            }
        }
        return false;
    }
}
public class WordDictionary {
    TrieNode root;
    public WordDictionary() {
        root = new TrieNode();
    }
    public void addWord(String word) {
        root.insert(word, 0);
    }

    public boolean search(String word) {
        return root.find(word, 0);
        
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
