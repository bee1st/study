package remind;

public class GoodsStock_ex {

	public static void main(String[] args) {
		GoodsStock obj = new GoodsStock();
		obj.goodsCode = "45327";
		obj.stockNum = 200;
		
		System.out.println("상품코드 : " + obj.goodsCode);
		System.out.println("상품재고 : " + obj.stockNum);
		
		obj.addStock(1000);
		System.out.println("상품코드 : " + obj.goodsCode);
		System.out.println("상품재고 : " + obj.stockNum);
		
		obj.minusStock(1);
		System.out.println("상품코드 : " + obj.goodsCode);
		System.out.println("상품재고 : " + obj.stockNum);

	}

}
