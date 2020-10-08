class Solution {
    public boolean detectCapitalUse(String word) {

        if (word.length() < 2) return true;

        if (word.toUpperCase().equals(word)) return true;

        // substring()只有一个参数时表示开始index
        if (word.substring(1).toLowerCase().equals(word.substring(1))) return true;

        return false;
    }
}
