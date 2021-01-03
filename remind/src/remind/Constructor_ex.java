package remind;

public class Constructor_ex {

	public static void main(String[] args) {
		Constructor obj = new Constructor("19845", 200);
		System.out.println("상품코드 : " + obj.goodsCode);
		System.out.println("상품재고 : " + obj.stockNum);
		
		obj.addStock(350);
		System.out.println("상품코드 : " + obj.goodsCode);
		System.out.println("상품재고 : " + obj.stockNum);
		
		obj.minusStock(55);
		System.out.println("상품코드 : " + obj.goodsCode);
		System.out.println("상품재고 : " + obj.stockNum);
	}

}
