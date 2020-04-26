//https://leetcode.com/problems/backspace-string-compare/
func backspaceCompare(S string, T string) bool {
    var i, j = dec_i(S, len(S)-1) , dec_i(T, len(T)-1)
    comp := true
    for i>=0 && j>=0 {
        if(S[i] != T[j]) {
            return false
        }
        i--
        j--
        i = dec_i(S, i)
        j = dec_i(T, j)
    }
    if(i != j) {
        comp = false  
    }
    
    return comp
}

func dec_i(S string, i int) int {
    h :=0
    for i>=0 && S[i] == '#' {
        h++
        i--
        //stack and unstack backspaces
        for h>0 && i>=0 {
            if S[i] == '#' {
                h++
            } else {
                h--
            }
            i--
        }
    }
    return i
}