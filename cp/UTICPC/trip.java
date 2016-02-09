import java.util.*;
import java.lang.Math;
public class scoreBoard{
    public static void main(String[]args){
	Scanner sc = new Scanner(System.in);
	int testCase = sc.nextInt();
	for(int i = 0; i < testCase; i++){
	    int number = sc.nextInt();
	    double sum = 0;
	    for(int j = 0 ; j < number; j++){
		sum += sc.nextDouble();		
	    }
	    System.out.println(sum);

	}
    }
}
