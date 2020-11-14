package BrainJava;

public class PlainLabel implements Movable_ch8{
	int x, y;
	String str;
	PlainLabel(int x, int y, String str) {
		this.x = x;
		this.y = y;
		this.str = str;
	}
//	void moveTo(int x, int y) { //잘못된 메소드
	public void moveTo(int x, int y) {
		this.x = x;
		this.y = y;
	}

}
