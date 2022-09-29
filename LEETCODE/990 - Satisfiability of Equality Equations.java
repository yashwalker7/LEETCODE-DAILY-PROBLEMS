class Solution {
    public boolean equationsPossible(String[] equations) {
        
        UnionFind u = new UnionFind();
        for (String equation : equations) {
            int a = equation.charAt(0) - 'a';
            int b = equation.charAt(3) - 'a';
            if (equation.charAt(1) == '=') {
                u.union(a,b);
            }
        }
        for (String equation: equations){
            int aFather = u.compressedFind(equation.charAt(0)- 'a');
            int bFather = u.compressedFind(equation.charAt(3)- 'a');
            if(equation.charAt(1) == '!' && aFather == bFather){
                return false;
            }
        }
        return true;
    }
    class UnionFind{
        int[] parent;
        int[] rank;
        
        UnionFind() {
            parent = new int[26];
            rank = new int[26];
            for (int i = 0; i<parent.length;i++)
            {
                parent[i] = i;
                rank[i] = 1;
            }
        }
        public int compressedFind(int a) {
            if (parent[a] != a)
            {
                return compressedFind(parent[a]);
            }
            return parent[a];
        }
        public void union(int a, int b)
        {
            int aFather =  compressedFind(a), bFather = compressedFind(b);
            if (aFather != bFather) {
                if (rank[aFather]>rank[bFather]) {
                    parent[bFather] = aFather;
                    rank[aFather] += rank[bFather];
                } else
                {
                    parent[aFather] = bFather;
                    rank[bFather] += rank[aFather];
                }
            }
        }
    }
}