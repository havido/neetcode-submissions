class Solution {

    public String encode(List<String> strs) {
        String newStr = "";
        for (String str : strs) {
            newStr += str + (char)0xC0;
        }
        return newStr;
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList<>();
        String curr = "";
        char[] charArray = str.toCharArray();
        for (char c : charArray) {
            if (c == 0xC0) {
                strs.add(curr);
                curr = "";
            }
            else curr += c;
        }
        return strs;
    }
}
