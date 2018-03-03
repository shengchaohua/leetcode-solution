public class BestTimetoBuyandSellStockII {

	public static int maxProfit(int[] prices) {
		if (prices == null || 0 == prices.length) 
            return 0;  
        int minPrice  = prices[0];  
        int sumProfit = 0;  
        for(int i = 1; i < prices.length; i++){  
            if(minPrice < prices[i]){  
                sumProfit += prices[i] - minPrice;  
                minPrice = prices[i];  
            }else{  
                minPrice = prices[i];  
           }  
        }   
        return sumProfit;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] prices = {2,1,3,5};
		BestTimetoBuyandSellStockII stock = new BestTimetoBuyandSellStockII();
		System.out.println(stock.maxProfit(prices));
	}

}
