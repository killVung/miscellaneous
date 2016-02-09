import java.util.Scanner;

public class Continents{
    public static void main(String[]args){
	Scanner sc = new Scanner(System.in);
	int testCase = sc.nextInt();
	for(int i = 0; i < testCase; i++){   
	    int row = sc.nextInt();
	    int col = sc.nextInt();
	    int[][] board = new int[row][col];
	    
	    //row
	    for(int x = 0; x < board.length; x++){
		for(int y = 0; y < board[0].length; y++){
		    board[x][y] = sc.nextInt(); 
		}
	    }
	    //testBoard(board);
	    for(int y = 0; y < board.length; y++){
		for(int x = 0; x < board[0].length; x++){
		    if(){
			
		    }
		}
	    }
	    
	}
    }
    
    public static void testBoard(int[][] board){
	for(int i = 0; i < board.length; i++){
	    for(int j = 0; j < board[0].length; j++){
		System.out.print(board[i][j] + " ");
	    }
	    System.out.println();
	}
	System.out.println();

    }
}
