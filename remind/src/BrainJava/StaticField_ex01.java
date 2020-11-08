package BrainJava;

public class StaticField_ex01 {

	public static void main(String[] args) {
		Accumulator acc1 = new Accumulator();
		Accumulator acc2 = new Accumulator();
		acc1.accumulate(10);
		acc2.accumulate(20);
		System.out.println("acc1.total = " + acc1.total);
		System.out.println("acc2.total = " + acc2.total);
		System.out.println();
		System.out.println("acc1.grandtotal = " + acc1.grandTotal);
		System.out.println("acc2.grandtotal = " + acc2.grandTotal);
		System.out.println();
		System.out.println("총계 : " + Accumulator.grandTotal);

	}

}
