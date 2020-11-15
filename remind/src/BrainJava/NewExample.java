package BrainJava;

public class NewExample {

	public static void main(String[] args) {
		ClothingInfo obj = new ClothingInfo("33", "반바지", "스판", Season.SUMMER);
		System.out.println("상품코드 : " + obj.code);
		System.out.println("상품명 : " + obj.name);
		System.out.println("소재 : " + obj.material);
		System.out.println("계절구분 : " + obj.season);

	}

}
