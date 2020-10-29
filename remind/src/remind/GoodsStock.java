package remind;

public class GoodsStock {
	String goodsCode;
	int stockNum;
	
	
	void addStock(int goods) {
		stockNum += goods;
	}
	
	int minusStock(int goods) {
		if(stockNum < goods) 
			return 0;
		stockNum -= goods;
		return goods;
	}
}
