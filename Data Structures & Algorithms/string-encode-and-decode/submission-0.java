class Solution {

    public String encode(List<String> strs) {
        String newStr = "";
        for (String str : strs) {
            newStr += str + " ";
        }
        return newStr;
    }

    public List<String> decode(String str) {
        List<String> strs = new ArrayList<>();
        String curr = "";
        char[] charArray = str.toCharArray();
        for (char c : charArray) {
            if (c == ' ') {
                strs.add(curr);
                curr = "";
            }
            else curr += c;
        }
        return strs;
    }
}
