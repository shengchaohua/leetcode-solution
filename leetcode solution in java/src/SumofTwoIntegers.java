

public class SumofTwoIntegers {
	public int getSum(int a, int b) {
		int res = a;
        int xor = a ^ b; //得到原位和
        int forward = (a & b) << 1; //得到进位和
        if (forward != 0) { //若进位和不为0，则递归求原位和+进位和
            res = getSum(xor, forward);
        } else {
            res=xor;//若进位和为0，则此时原位和为所求和
        }
        return res;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SumofTwoIntegers tInt = new SumofTwoIntegers();
		System.out.println(tInt.getSum(10, 10));
	}

}
