package test;


public class Board {
	
	private static final String EMPTY = "[ ]";
	String[][] board = {
			{"", "", ""},
			{"", "", ""},
			{"", "", ""}
	};
	
	public void initialize() {
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				board[i][j] = EMPTY;
			}
		}
	}
	
	public void setPoint(int a, int b, String point) {
		board[a][b] = point;
	}
	
	public boolean isEmpty(int a, int b) {
		return board[a][b].equals(EMPTY);
	}
	
	public void print() {
		for (int a = 0; a < 3; a++) {
			for (int b = 0; b < 3; b++) {
				System.out.print(board[a][b]);	
			}
			System.out.println("");			
		}
	}
	
	/***
	 * 
	 * @param a
	 * @param b
	 * @return if user1 won return 1, else user2 won return 2, else return 0.
	 */
	public int checkWinningGame(int a, int b) {
		// 0, 0
		// [ ] [ ] [ ]
		// [ ] [O] [ ]
		// [ ] [ ] [ ]
				
		boolean check = false;
		// a 줄이 완성됬는지
		if (board[a][0] == board[a][1] && board[a][0] == board[a][2]) {
			check = true;
		} else if (board[0][b] == board[1][b] && board[0][b] == board[2][b]) {
			// b 줄이 완성됬는지
			check = true;
		}
		if (Math.abs(a - b) == 0 || Math.abs(a- b) == 2 ) {
			if (board[0][0] == board[1][1] && board[0][0] == board[2][2]) {
				check = true;
			} else if (board[2][0] == board[1][1] && board[0][2] == board[1][1]) {
				check = true;
			}
		}
		// a,b로 대각선이 완료됬는지
		if (check == true) {
			return board[a][b].equals("[O]") ? 1 : 2;
		}
		return 0;
	}
}
