package BrainJava;

public class ClothingInfo01 {
	enum Season {
		SPRING, SUMMER, FALL, WINTER
	}
	String code;
	String name;
	String material;
	Season season;
	ClothingInfo01(String code, String name, String material, Season season) {
		this.code = code;
		this.name = name;
		this.material = material;
		this.season = season;
	}

	

}
