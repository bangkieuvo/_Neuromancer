#include <iostream>
using namespace std;
#define ll long long
ll GCD(ll a, ll b){
    if (b == 0)
        return a;
    while(b!=0){
        ll tam = a;
        a = b;
        b = tam%a;
    }
    return a;
}

ll ETF(ll n){
    ll res = n;
    if(n%2 == 0){
        res = res/2;
        while(n%2 == 0)
            n = n/2;
    }
    ll p = 3;
    while(n != 1){
        if(n%p == 0){
            res = (res/p)*(p-1);
            while(n%p == 0)
                n = n/p;
        }
        if (res == n && p*p >= n){
            return res - 1;
        }
        p = p + 2;
    }
    return res;
}
