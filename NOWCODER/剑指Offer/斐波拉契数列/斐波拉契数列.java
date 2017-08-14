public class Main {
	
	public int Fibonacci(int n) {
		if(n==0){
			return 0;
		} else if(n==1 || n==2){
			return 1;
		}
		int[] fi = new int[n];
		fi[0] = 1;
		fi[1] = 1;
		int i = 2;
		while(fi[n-1]==0){
			fi[i] = fi[i-1] + fi[i-2];
			i++;
		}
		return fi[n-1];
    }
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}