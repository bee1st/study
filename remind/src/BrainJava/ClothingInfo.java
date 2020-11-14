package BrainJava;

public class ClothingInfo {
	String code;
	String name;
	String material;
//	int season;
//	static final int SPING = 1;
//	static final int SUMMER = 2;
//	static final int FALL = 3;
//	static final int WINTER = 4;
	Season season;
	
	ClothingInfo (String code, String name, String material, Season season) {
		this.code = code;
		this.name = name;
		this.material = material;
		this.season = season;
	}


}
