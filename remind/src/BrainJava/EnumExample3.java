package BrainJava;

public class EnumExample3 {

	public static void main(String[] args) {
		printSeason(Season.SPRING);
		printSeason(Season.SUMMER);
		printSeason(Season.FALL);
		printSeason(Season.WINTER);
	}
	
	static void printSeason(Season season) {
		System.out.println(season.value());
	}

}
