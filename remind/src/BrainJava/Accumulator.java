package BrainJava;

public class Accumulator {
	int total = 0;
	static int grandTotal = 0; //정적필드 선언
	void accumulate(int amount) {
		total += amount;
		grandTotal += amount; //정적필드 사용하는 명령문
	}

}
