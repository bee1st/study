package test;


/* 틱택토
 * 1. 이차원 배열을 이용
 * 2. 판 그리기
 * 3. x축 2개 같거나 y축 2개 같으면 2개 같은 축에 넣기 (0,0) (0,1) -> (0,2)에 넣게끔 if문
 * 
 */

import java.util.*;

public class TikTakToe {

	   public static void main(String[] args) {
	      Scanner sc = new Scanner(System.in);
	      int x, y;
	      char[][] board = new char[3][3];
	      
	      //보드판 초기화
	      for(int i = 0; i < 3; i++) {
	    	  for(int j = 0; j < 3; j++) {
	    		  board[i][j] = ' ';
	    	  }
	    		  
	      }

	      
	      for(int i = 0; i < 3; i++) {
	         System.out.println(" " + board[i][0] + " | " + board[i][1] + " | " + board[i][2]);
	         if (i != 2) {
	            System.out.println("---|---|---");
	         }
	      }

	   }
	}