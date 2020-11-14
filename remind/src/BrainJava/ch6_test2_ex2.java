package BrainJava;

public class ch6_test2_ex2 extends ch6_test2{
	
	ch6_test2_ex2 (int sideLength) {
		super(sideLength, sideLength);
	}
	
	int getSideLength() {
		return getWidth();
	}
}
