package BrainJava;

public enum Color {
	YELLOW("노랑"), RED("빨강"), BLUE("파랑");
	final private String color;
	Color(String color) {
		this.color = color;
	}
	String value() {
		return color;
	}
	
}
