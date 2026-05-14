class Solution {
    public boolean isAnagram(String s, String t) {
        
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<String,Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            String c = s.substring(i,i+1);
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        for (int i = 0; i < s.length(); i++) {
            String c = t.substring(i,i+1);
            if (map.containsKey(c)) {
                map.put(c,map.get(c) - 1);
                if (map.get(c) == 0) {
                    map.remove(c);
                }
            } else {
                return false;
            }
        }
        return true;

    }
}
