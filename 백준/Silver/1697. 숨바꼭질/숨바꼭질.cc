#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// first : location, second : count
queue<pair<int,int> > q;
int visit[100001]={0,};

int n,k;
int minn=100001;

int main(void) {
    cin >> n >> k;
    q.push(make_pair(n,0));
    while(1) {
        if(q.empty())
            break;
        pair<int,int> p = q.front();
        q.pop();

        if(p.first<0 || p.first > 100001 || p.second >= minn)
            continue;
        if(p.first>=0 && p.first <100001) {
            if(visit[p.first]==1)
                continue;
        }
            
        if(minn > p.second && p.first == k)
            minn = p.second;

        visit[p.first]=1;

        q.push(make_pair(p.first+1,p.second+1));
        q.push(make_pair(p.first*2,p.second+1));
        q.push(make_pair(p.first-1,p.second+1));


            
    }
    cout << minn << endl;
    return 0;
}