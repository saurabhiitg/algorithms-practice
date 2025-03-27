//#include<bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        vector< int > d(10,0);
        //01.03.2025
        int total = 5;
        d[0] = 3;
        d[1] = 1;
        d[2] = 2;
        d[3] = 1;
        d[5] = 1;

        int x;
        int res = 0;
        for(int i = 0; i < n; i++){
            cin >> x;
            if(d[x] > 0){
                d[x]--;
                if(d[x] == 0){
                    total--;
                }
            }
            if(res==0 && total == 0){
                res = i+1;
            }
        }
        cout << res << endl;
    }
    return 0;
}