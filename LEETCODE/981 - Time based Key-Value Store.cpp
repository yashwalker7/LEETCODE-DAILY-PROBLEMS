class TimeMap {
public:
    /** Initialize your data structure here. */
    TimeMap() {
        ;
    }
    
    void set(string key, string value, int timestamp) {
        mp[key][timestamp] = value;
    }
    
    string get(string key, int timestamp) {
        if( !mp.count( key ) ) return "";
        auto it = mp[key].upper_bound( timestamp );
        if( it == mp[key].begin() ) return "";
        --it;
        return it->second;
    }
private:
    map<string, map<int, string>> mp;
};