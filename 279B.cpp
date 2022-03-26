#include<bits/stdc++.h>
 
using namespace std;
 
int n, t, a[100005], ans, s, sum;
 
int main(){
	cin >> n >> t;
	s = 0;
	for (int i = 0; i < n; i++){
		cin >> a[i];
		sum += a[i];
		while (sum > t && s<=i){
			sum -= a[s++];
		}
		ans = max(ans, i - s + 1);
	}
	cout << ans;
}