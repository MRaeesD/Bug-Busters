class Main{ //bug
	public static void main (String args){
    	Scanner sc = new Scanner(System.in);
      	int n = sc.nextInt();
      	String s = sc.nextString();
      	int countGood = 0;
      	int countPoor = 0;
      	for(int i=0; i<n; i++){
        	if(s.charAt(i) == 'o'){
            	countGood++;
            }
          	else if(s.charAt(i) == 'x'){
            	countPoor++;
            }
        }
      	if(countGood > 0 && countPoor == 0){
        	System.out.println("Yes");
        }
      	else{
        	System.out.println("No");
        }
    }
}

