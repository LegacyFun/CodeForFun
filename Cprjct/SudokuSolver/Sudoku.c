#include <stdio.h>
#include <stdbool.h>
#define N 9
int tb[N][N];

typedef struct{
    int x;
    int y;
} pair;

void input();

bool isOK(int x ,int y ,int num);

bool Solve();

pair issd(); //Find the nearest non-set element

void output(){
    for(int i = 0; i < N; i++){
            !(i % 3) ? printf("\n-----------------------") : 1;
        printf("\n");
        for(int j = 0; j < N; j++){
                
            !(j % 3) ? printf("| ") : 1;
             printf("%d ",tb[i][j]);
        }
    }
}

int main(){
    input();  

    if(Solve())
        output();

    return 0;
}

void input(){
    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++)
            scanf("%d", &tb[i][j]); 
    
}
bool isOK(int x, int y, int num){
    // Check Column and Row 
    for(int i = 0; i < N; i++)
        if( (tb[i][y] == num && i != x) || (tb[x][i] == num && i != y) )
            return false;

    // Check 3*3 Box

        for (int i = 0; i < 3; i++) 
            for (int j = 0; j < 3; j++) 
                if (tb[i + (x - x%3)][j + (y - y%3)] == num) 
                    return false;

        return true;
}
pair issd(){
    pair pos;

    pos.x = -1; pos.y = -1;// Initialize pair

    for(int i = 0; i < N; i++)
       for(int j=0; j < N; j++)
               if(tb[i][j] == 0){
                   pos.x = i ,pos.y = j;
                   return pos;
               }
    return pos;
    
}
bool Solve(){
    int x,y;
    pair pos;
    pos = issd();
    
    if(pos.x == -1 && pos.y == -1) // Check if there's any empty element 
        return  true;
    
    x = pos.x;
    y = pos.y;

    for(int n = 1; n < 10; n++){

        if(isOK(x,y,n)){
            
            tb[x][y] = n;
                
            if(Solve())
                return true;

            tb[x][y] = 0;
        }
    }
    return false;
}
