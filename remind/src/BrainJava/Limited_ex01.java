package BrainJava;

public class Limited_ex01 {

	public static void main(String[] args) {
		LimitedValue v = new LimitedValue();
		v.setValue(200);
		System.out.println("v.value = " + v.value);
		System.out.println("상한값 = " + LimitedValue.Upper_Limit); //상수필드 사용
	}

}
