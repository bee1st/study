package BrainJava;

public class AccessControlExample1 {

	public static void main(String[] args) {
		Fraction obj = new Fraction(100, 3);
		//System.out.println("100 / 3 = " + obj.getDouble()); //getDouble 은 private이기때문에
		System.out.println("100 / 3 = " + obj.getInt());

	}

}
