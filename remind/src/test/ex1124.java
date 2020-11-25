package test;

import java.util.Scanner;

public class ex1124 {

	private static int tttGame(String[][] board, int a, int b) {
		boolean check = false;
		if (board[a][0] == board[a][1] && board[a][0] == board[a][2]) {
			check = true;
		} else if (board[0][b] == board[1][b] && board[0][b] == board[2][b]) {
			check = true;
		}
		if(Math.abs(a - b) == 0 || Math.abs(a - b) == 2) {
			if(board[0][0] == board[1][1] && board[0][0] == board[2][2]) {
				check = true;
			} else if(board[2][0] == board[1][1] && board[0][2] == board[1][1]) {
				check = true;
			}
		}
		if (check == true) {
			return board[a][b].equals("[O]") ? 1 : 2;
		}
		return 0;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int count = 1;
		int x = 0;
		String[][] board = {
				{"[ ]","[ ]","[ ]"},
				{"[ ]","[ ]","[ ]"},
				{"[ ]","[ ]","[ ]"}
		};

		while(x == 0) {
			if(count == 1) {
				System.out.print("1번 선수 입력 : ");
				int a = sc.nextInt();
				int b = sc.nextInt();
				if(board[a][b].equals("[ ]")) {
					board[a][b] = "[O]";
					if(tttGame(board, a, b) != 0) {
						System.out.println("1번 승리");
						break;
					}
					count = 2;
				}else {
					System.out.println("입력 불가");
				}
			} else if(count == 2) {
				System.out.print("2번 선수 입력 : ");
				int a = sc.nextInt();
				int b = sc.nextInt();
				if(board[a][b].equals("[ ]")) {
					board[a][b] = "[X]";
					if(tttGame(board, a, b) != 0) {
						System.out.println("2번 승리");
						break;
					}
					count = 1;
				}else {
					System.out.println("입력 불가");
				}

			}
			for (int a = 0; a < 3; a++) {
				for(int b = 0; b < 3; b++) {
					System.out.print(board[a][b]);
				}
				System.out.println("");
			}
		}
	}
}
