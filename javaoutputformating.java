import java.util.Scanner;

public class Solution{
    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++){
                String s1=sc.next();
                int x=sc.nextInt();
                //Complete this line
                String s = String.valueOf(x);
        
                int len=s1.length();
                
                if (len <15){
                    System.out.print(s1);
                    for(int j = 0; j<(15-len); j++){
                        System.out.print(" ");
                        
                    }
                    String s2 = String.valueOf(x);
                    int le=s2.length();
                    if(le < 3){
                        for(int k=0; k<3-le; k++){
                            System.out.print("0");         
                        }
                        System.out.print(s2);
                       
                    }
                    else{
                        System.out.print(s2);
                    }
                }
                else{
                    System.out.print(s1+s);
                }
                System.out.println();
            }
            
        
            System.out.println("================================");

    }
}
