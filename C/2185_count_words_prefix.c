int prefixCount(char** words, int wordsSize, char* pref) {
    double n = strlen(pref), res = 0;

    for (int i=0; i<wordsSize; i++) {
        bool vp = true;
        if (strlen(words[i])<n) continue;

        for (int j=0; j<n; j++) {
            if (words[i][j] != pref[j]) vp=false;
        }

        if (vp==true) {res++;}
    }

    return res;
}