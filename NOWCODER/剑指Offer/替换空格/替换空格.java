public class Solution {
    public String replaceSpace(StringBuffer str) {
    	int l = str.length();
    	int dz = 0;
    	for(int i=0; i<l+dz; i++){
    		if(str.charAt(i)==' '){
    			str.replace(i, i+1, "%20");
    			dz += 2;
    		}
    	}
		
		return str.toString();
    }
}