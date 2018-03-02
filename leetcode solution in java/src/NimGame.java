public class NimGame {
	public boolean canWinNim(int n) {
		return n % 4 != 0; // or return (n & 3) != 0, it's more faster
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		NimGame ng = new NimGame();
		System.out.println(ng.canWinNim(12));
	}

}
