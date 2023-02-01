import java.util.*;
public class Solution{
    
    public static void main(String []argh)
    {
        Scanner sc = new Scanner(System.in);
        Stack<Character> Stacks = new Stack<>();
   
        while (sc.hasNext()) {
            String input=sc.next();
            //Complete the code
            for (int i =0; i< input.length(); i++){
                
                if (!Stacks.isEmpty()){
                    switch(input.charAt(i)){
                     case '}': if (Stacks.peek() == '{'){
                         Stacks.pop();
                     }break;
                     case ']': if (Stacks.peek() == '['){
                         Stacks.pop();
                     }break;
                     case ')': if (Stacks.peek() == '('){
                         Stacks.pop();
                     }break;                  
                    default: Stacks.push(input.charAt(i));    
                        
                    }
                }else{
                        Stacks.push(input.charAt(i));
                    }
               
            }
             System.out.println(Stacks.isEmpty());
             Stacks.clear();
        }
        
    }
}