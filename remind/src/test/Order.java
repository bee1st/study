package test;

public class Order {
	private int currentOrder;
	
	public void initialize() {
		currentOrder = 1;
	}
	
	public void next() {
		if (currentOrder == 1) {
			currentOrder = 2;
		} else if (currentOrder == 2) {
			currentOrder = 1;
		}
	}
	
	public int getCurrentOrder() {
		return currentOrder;
	}
}
