package remind;

public class studyArray {
	public static void main(String[] args) {
		int [][] score = {
				{100, 100, 100},
				{20, 20, 30},
				{30, 30, 40},
				{50, 60, 30}
			};
		int sum = 0;
		for(int i = 0; i < score.length; i++) {
			for(int j = 0; j < score[i].length; j++) {
				System.out.println(score[i][j]);
			}
		}
		for (int[] a : score) {
			for (int i : a) {
				sum += i;
				
			}
			
		} System.out.println(sum);
	} 

}
