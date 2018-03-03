import java.util.Stack;

public class ValidParentheses {
	public boolean isValid(String s) {
		char[] sArray = s.toCharArray();
		Stack<Character> stack = new Stack<>();
		for (int i = 0; i < sArray.length; i++) {
			if (isLeft(sArray[i])) {
				stack.push(sArray[i]);
			} else {
				if (stack.isEmpty()) {
					return false;
				}
				char left = stack.pop();
				if (!isPair(left, sArray[i])) {
					return false;
				}
			}
		}
		if (stack.isEmpty()){
			return true;
		}
		return false;
	}
	
	public boolean isLeft(char c) {
		return c == '(' || c == '[' || c == '{' || false;
	}
	
	public boolean isRight(char c) {
		return c == ')' || c == ']' || c == '}' || false;
	}
	
	public boolean isPair(char c1, char c2) {
		if (c1 == '(' && c2 == ')' || c1 == '[' && c2 == ']' || c1 == '{' && c2 == '}') {
			return true;
		} 
		return false;	
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ValidParentheses vp = new ValidParentheses();
		System.out.println(vp.isValid("(){}"));
	}

}
