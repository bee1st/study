package remind;

public class Number {
	int num[];
	Number(int num[]) {
		this.num = num;
	}
	int getTotal() {
		int total = 0;
		for(int i = 0; i < num.length; i++) 
			total += num[i];
			return total;
	}
	int getAverage() {
		int total = 0;
		total = getTotal();
		int avg = total / num.length;
		return avg;
	}
}
