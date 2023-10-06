

class Solution {
public:
    string colName(long long int n) {
        string result = "";

        while (n > 0) {
            // Subtract 1 to handle 1-based indexing (A=1, B=2, ..., Z=26)
            n--;
            
            // Get the remainder when divided by 26
            int remainder = n % 26;
            
            // Convert the remainder to the corresponding letter
            char letter = 'A' + remainder;
            
            // Append the letter to the result
            result = letter + result;

            // Divide the number by 26 to move to the next position
            n /= 26;
        }

        return result;
    }
};
