

public class ReverseString {
	public String reverseString(String s) {
        StringBuffer str = new StringBuffer();
        for(int i = s.length() - 1; i >= 0; i--) {
            str.append(s.charAt(i));
        }
        return str.toString();
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ReverseString rs = new ReverseString();
		String s = new String("hello");
		System.out.println(rs.reverseString(s));
	}

}
