package remind;

public class arr1 {
	public static void main(String[] args) {
		int[][] score = { 
				{100, 100, 100},
				{80, 70, 60},
				{60, 80, 90},
				{90, 50, 60},
				{80, 40, 60} };
		int kor = 0;
		int eng = 0;
		int math = 0;
		
		System.out.println("----------------------------");
		
		for(int i = 0; i < score.length; i++) {
			int sum = 0;
			float avg = 0.0f;
			kor += score[i][0];
			eng += score[i][1];
			math += score[i][2];
			System.out.printf("%3d",i + 1);
			
			for(int j = 0; j < score[i].length; j++) {
				sum += score[i][j];
				System.out.printf("%5d",score[i][j]);
			}
			avg = sum/(float)score[i].length;
			System.out.printf("%5d %5.1f%n",  sum , avg);
		}
		

		System.out.println("-------------------------------");

	}

}
