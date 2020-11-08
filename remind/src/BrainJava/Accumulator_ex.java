package BrainJava;

public class Accumulator_ex {

	public static void main(String[] args) {
		Accumulator_class acc1 = new Accumulator_class();
		Accumulator_class acc2 = new Accumulator_class();
		
		acc1.accumulate(10);
		acc2.accumulate(20);
		
		int grandTotal = Accumulator_class.getGrandTotal();
		
		System.out.println("acc1.total = " + acc1.total);
		System.out.println("acc2.total = " + acc2.total);
		System.out.println("총계 = " + grandTotal);

	}

}
