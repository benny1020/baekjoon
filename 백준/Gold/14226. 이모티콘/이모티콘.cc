#include <bits/stdc++.h>
 
#define INF 0x3f3f3f3f
using namespace std;
 
int d[2222][2222];
int n;
 
// 1) clip 변경
// 2) 실제 개수를 하나 삭제
// 3) 실제 개수를 clip 만큼 증가
int go(int clip, int screen) {
    if (screen > 2 * n || clip > 2 * n) return INF;
    if (screen < 0) return INF;
    if (screen == n) return 0;
 
    int &ret = d[clip][screen];
    if (ret != -1) return ret;
    ret = INF;
    ret = min(ret, go(screen, screen) + 1);
    ret = min(ret, go(clip, screen - 1) + 1);
    ret = min(ret, go(clip, screen + clip) + 1);
    return ret;
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
 
    memset(d, -1, sizeof(d));
    cin >> n;
    cout << go(0, 1);
}