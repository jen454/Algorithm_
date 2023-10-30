#include <iostream>
#include <queue>
#define MAX 101

using namespace std;

int N, M;
string row;
int maze[MAX][MAX];
bool visited[MAX][MAX];
int dist[MAX][MAX];

int dir_x[4] = {-1, 1, 0, 0};
int dir_y[4] = {0, 0, -1, 1};

queue<pair<int,int>> q;

void solution(int start_x, int start_y);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> N >> M;

    for (int i=0; i<N; ++i){
        cin >> row;
        for (int j=0; j<M; ++j){
            maze[i][j] = row[j]-'0';
        }
    }

    solution(0,0);

    cout << dist[N-1][M-1] << "\n";
    return 0;
}

void solution(int start_x, int start_y){         

    visited[start_x][start_y] = true;
    q.push(make_pair(start_x,start_y));
    dist[start_x][start_y]++;

    while (!q.empty()){

        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i=0; i<4; ++i){
            int new_x = x + dir_x[i];
            int new_y = y + dir_y[i];

            if ( (0 <= new_x && new_x < N) && (0 <= new_y && new_y < M) && !visited[new_x][new_y] && maze[new_x][new_y] == 1 ) {
                visited[new_x][new_y] = true;
                q.push(make_pair(new_x, new_y));
                dist[new_x][new_y] = dist[x][y] + 1;
            }
        }
    }
}