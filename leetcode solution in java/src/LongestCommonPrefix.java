

public class LongestCommonPrefix {
	public String longestCommonPrefix(String s1, String s2) {
		int i = 0;
		for ( ; i < s1.length() && i < s2.length(); i++) {
			if (s1.charAt(i) != s2.charAt(i))
				break;
		}
		return s1.substring(0, i);
	}
	
	public String longestCommonPrefixInArray(String[] strs) {
		int len = strs.length;
		if (len == 0){
			return "";
		}
		if (len == 1){
			return strs[0];
		}
		String prefix = longestCommonPrefix(strs[0], strs[1]);
		if (len == 2) {
			return prefix;
		}
		for (int i = 2; i < len; i++) {
			if (strs[i].startsWith(prefix)) {
				continue;
			} else {
				prefix = longestCommonPrefix(prefix, strs[i]);
			}
		}
		return prefix;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String[] strs = {"shengchaohua", "shengchaohua", "shengchao", "shengcha", "sheng"};
		LongestCommonPrefix lcp = new LongestCommonPrefix();
		System.out.println(lcp.longestCommonPrefixInArray(strs));
	}

}
