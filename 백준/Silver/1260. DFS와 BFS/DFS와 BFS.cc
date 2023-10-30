#include <iostream>
#include <queue>
using namespace std;
#define MAX 1001
 
int N, M, V;
int arr[MAX][MAX];
bool visited[MAX];
queue<int> q;

void dfs(int v);

void bfs(int v);
 
int main() {
    cin >> N >> M >> V;
 
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        arr[a][b] = 1;
        arr[b][a] = 1;
    }
 
    for (int i = 1; i < N+1; i++) {
        visited[i] = false;
    }
    dfs(V);
    
    cout << '\n';
    
    for (int i = 1; i < N+1; i++) {
        visited[i] = false;
    }
    bfs(V);
 
    return 0;
}

void dfs(int v) {
    visited[v] = true;
    cout << v << " ";
    
    for (int i = 1; i < N+1; i++) {
        if (arr[v][i] == 1 && visited[i] == false) {
            dfs(i);
        }
    }
}
 
void bfs(int v) {
    q.push(v);
    visited[v] = true;
    cout << v << " ";
 
    while (!q.empty()) {
        v = q.front();
        q.pop();
        
        for (int i = 1; i < N+1; i++) {
            if (arr[v][i] == 1 && visited[i] == false) {
                q.push(i);
                visited[i] = true;
                cout << i << " ";
            }
        }
    }
}