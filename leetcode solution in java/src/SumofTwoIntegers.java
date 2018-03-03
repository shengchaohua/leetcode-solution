

public class SumofTwoIntegers {
	public int getSum(int a, int b) {
		int res = a;
        int xor = a ^ b; //�õ�ԭλ��
        int forward = (a & b) << 1; //�õ���λ��
        if (forward != 0) { //����λ�Ͳ�Ϊ0����ݹ���ԭλ��+��λ��
            res = getSum(xor, forward);
        } else {
            res=xor;//����λ��Ϊ0�����ʱԭλ��Ϊ�����
        }
        return res;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		SumofTwoIntegers tInt = new SumofTwoIntegers();
		System.out.println(tInt.getSum(10, 10));
	}

}
