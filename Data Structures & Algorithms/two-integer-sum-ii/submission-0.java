class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length -1;
        while (numbers[l]<numbers[r]) {
            if (numbers[l]+numbers[r] > target) r--;
            else if (numbers[l]+numbers[r] < target) l++;
            else return new int[] {numbers[l], numbers[r]};
        }
        return null;
    }
}
