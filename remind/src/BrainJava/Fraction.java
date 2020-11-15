package BrainJava;

public class Fraction {
	private int numerator;
	private int denominator;
	Fraction(int numerator, int denominator) {
		this.numerator = numerator;
		this.denominator = denominator;
		
	}
	private double getDouble() {
		return (double) numerator / denominator;
	}
	int getInt() {
		return (int) getDouble();
	}


}
