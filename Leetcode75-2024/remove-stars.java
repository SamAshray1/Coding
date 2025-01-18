import java.util.*;

class Solution {
    public String removeStars(String s) {
        
        Stack<Character> stack = new Stack<>();
        int index = 0;
        int lengthS = s.length();
        for(index=0; index < lengthS ; index++){
            char str = s.charAt(index);

            stack.push(str);

            if(str == '*'){
                stack.pop();
                stack.pop();
            }
        }

        StringBuilder finalStr = new StringBuilder();
        for (char c : stack) {
            finalStr.append(c);
        }
        
        return finalStr.toString();
    }
}

    