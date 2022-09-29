class Solution {
public:
    string pushDominoes(string dominoes) {
        int a=dominoes.size();
        int left[a];
        int right[a];
        int sum[a]; 
        int com=0;
        for(int i=0;i<a;i++)
        {
            if(dominoes[i]=='R') com=a;
            else if(dominoes[i]=='L') com=0;
            else if(dominoes[i]=='.')
                com=max(com-1,0);
            
            right[i]=com;
        }
        int b=0;
        for(int i=a-1;i>=0;i--,b++)
        {
             if(dominoes[i]=='L') com=a;
            else if(dominoes[i]=='R') com=0;
            else if(dominoes[i]=='.')
                com=max(com-1,0);
            
            left[i]=com*(-1);
        }
        for(int i=0;i<a;i++) {
            sum[i]=right[i]+left[i];
            if(sum[i]==0) dominoes[i]='.';
            else if(sum[i]>0) dominoes[i]='R';
            else dominoes[i]='L';
                             }
        return dominoes;
    }
};