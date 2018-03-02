import com.sun.org.apache.bcel.internal.generic.LAND;

public class IslandPerimeter {
    public int calPerimeter(int[][] grid) {
    	int lineNum = grid.length;
    	int columnNum = grid[0].length;
    	int[][] perimeter = new int[lineNum][columnNum];
    	int perimeterSum = 0;
    	for (int i = 0; i < lineNum; i++) {
    		for (int j = 0; j < columnNum; j++) {
    			int length = 0;
    			if (grid[i][j] == 0) { // �ж���ˮ
    				length = j < columnNum - 1 && grid[i][j+1] == 1 ? length +1 : length; // �ұ���½�ؾͼ�һ
    				length = i < lineNum - 1 && grid[i+1][j] == 1 ? length +1: length;   // �±���½�ؾͼ�һ
    			} else { // �ж���½��
    				length = j == 0 ? length + 1 : length;
    				length = j == columnNum - 1 ? length + 1 :length;
    				length = i == 0 ? length + 1 :length;   // ½���ڱ߽������һ
    				length = i == lineNum - 1 ? length + 1 :length; 
    				length = j < columnNum - 1 && grid[i][j+1] == 0 ? length+1 : length;  // �ұ���ˮ��һ
    				length = i < lineNum - 1 && grid[i+1][j] == 0 ? length+1 : length;    // �±���ˮ��һ
    			}
    			perimeter[i][j] = length;
    		}
    	}
    	for ( int i = 0; i < perimeter.length; i++) {
    		for (int j = 0; j < perimeter[0].length; j++) {
    			perimeterSum += perimeter[i][j];
    		}
    	}
    	return perimeterSum;
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[][] grid1 = { 
				{0,1,0,0},
				{1,1,1,0},
				{0,1,0,0},
				{1,1,0,0}};
		int[][] grid2 = {{1,0}};
		IslandPerimeter land = new IslandPerimeter();
		System.out.println(land.calPerimeter(grid1));
		System.out.println(land.calPerimeter(grid2));
	}
}
