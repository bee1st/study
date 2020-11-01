package remind;

public class Constructor {
	String goodsCode;
	int stockNum;
	
	public Constructor(String code, int num) {
		goodsCode = code;
		stockNum = num;
	}
	
	void addStock(int num) {
		stockNum += num;
	}
	int minusStock(int num) {
		if(stockNum < num)
			return 0;
		stockNum -= num;
		return num;
	}

}
