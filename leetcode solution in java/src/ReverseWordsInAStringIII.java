public class ReverseWordsInAStringIII {
	
	public String reverseWords(String s) {
        String[] strArray = new String[]{};
        StringBuilder stringBuilder = new StringBuilder();
        strArray = s.split(" ");
        for (int i = 0; i < strArray.length; i++) {
			for (int j = strArray[i].length() - 1; j >= 0; j--) {
				stringBuilder.append(strArray[i].charAt(j));
			}
			if ( i < strArray.length - 1) {
				stringBuilder.append(" ");
			}
		}
		return stringBuilder.toString();
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ReverseWordsInAStringIII rAStringIII = new ReverseWordsInAStringIII();
		String string = "Let's take LeetCode contest";
		System.out.println( rAStringIII.reverseWords(string) );
	}

}
