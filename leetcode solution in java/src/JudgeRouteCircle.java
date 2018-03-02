public class JudgeRouteCircle {

	public static boolean judgeCircle(String moves) {
		int UDnum = 0, LRnum= 0; 
		for (int i = 0; i < moves.length(); i++) {
			switch (moves.charAt(i)) {
			case 'U':
				UDnum++;
				break;
			case 'D':
				UDnum--;
				break;
			case 'L':
				LRnum++;
				break;
			case 'R':
				LRnum--;
				break;
			default:
				break;
			}
		}
		return UDnum == 0 && LRnum == 0;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println(JudgeRouteCircle.judgeCircle("LLLRRRUUUDDD"));
	}

}
