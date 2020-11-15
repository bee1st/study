package BrainJava;

public class NewExample2 {

	public static void main(String[] args) {
		ClothingInfo01 obj = new ClothingInfo01("105", "반팔", "면100%", ClothingInfo01.Season.SUMMER);
		System.out.println("상품코드 : " + obj.code);
		System.out.println("상품명 : " + obj.name);
		System.out.println("소재 : " + obj.material);
		System.out.println("계절구분 : " + obj.season);

	}

}
