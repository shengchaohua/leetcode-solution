public class NumberComplement {
	public int numberComplement(int num){
		String numBinary = Integer.toBinaryString(num);
		byte[] numByte = numBinary.getBytes();
		for(int i = 0; i < numByte.length; i++){
			if( numByte[i] == '0' ){
				numByte[i] = 1;
			} else {
				numByte[i] = 0;
			}
		}
		int sum = 0;
		for (int i = numByte.length - 1, j = 0; i >= 0; i--, j++){
			int bitValue = (int) (Math.pow(2.0, j) * numByte[i]);
			sum = sum + bitValue;
		}
		return sum;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		NumberComplement nComplement = new NumberComplement();
		System.out.println( nComplement.numberComplement(1) );
	}

}
