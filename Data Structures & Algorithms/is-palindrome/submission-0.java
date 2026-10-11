class Solution {
    public boolean isPalindrome(String s) {
        String ss = s.toLowerCase();
        int i = 0;
        int j = ss.length()-1;
        while (i < j) {
            while (!Character.isLetter(ss.charAt(i)) && !Character.isDigit(ss.charAt(i)) && i < j) {
                i++;
            }
            while (!Character.isLetter(ss.charAt(j)) && !Character.isDigit(ss.charAt(j)) && i < j) {
                j--;
            }
            if (ss.charAt(i) != ss.charAt(j)) return false;
            i++;
            j--;
        }
        return true;
    }
}
