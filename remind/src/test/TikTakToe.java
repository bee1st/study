package test;


public class TikTakToe {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int count = 1;
		int x = 0;
		String[] board = {
				"[ ]","[ ]","[ ]",
				"[ ]","[ ]","[ ]",
				"[ ]","[ ]","[ ]",
				};
		
		while (x == 0) {
			if(count == 1) {
				System.out.print("1번 입력 (0~9) : ");
				int user1 = sc.nextInt();
				if(board[user1].equals("[ ]")) {
					board [user1] = "[O]";
					count = 2;
				}else {
					System.out.print("입력 불가");
				}
			}else if(count == 2) {
				System.out.print("2번 입력 (0~9) : ");
				int user2 = sc.nextInt();
				if(board[user2].equals("[ ]")) {
					board [user2] = "[X]";
					count = 1;
				}else {
					System.out.print("입력 불가");
				}
			}
				
			
			
			for (int i = 0; i < 9; i++) {
				System.out.println(board[i]);
				if(i % 3 == 2 && i != 0) {
					System.out.println("");
				}
			}
		}
		
	}
}
