package BrainJava;

public class ch5_test1 {
	int goodsCode;
	String brand;
	String origin;
	String maker;
	int dan;
	int sale;
	
	ch5_test1(int goodsCode, String brand, String origin, String maker, int dan){
		this.goodsCode = goodsCode;
		this.brand = brand;
		this.origin = origin;
		this.maker = maker;
		this.dan = dan;
	}
	
	ch5_test1(int goodsCode, String brand, String origin, String maker, int dan, int sale){
		this.goodsCode = goodsCode;
		this.brand = brand;
		this.origin = origin;
		this.maker = maker;
		this.dan = dan;
		this.sale = sale;
	}
	
	
	void UpdateChageSale(int sale) {
		this.sale = sale;
	}
	
	int getCount(int dan, int sale) {
		this.dan = dan;
		this.sale = sale;
		return dan * (sale /100);
	}

}
