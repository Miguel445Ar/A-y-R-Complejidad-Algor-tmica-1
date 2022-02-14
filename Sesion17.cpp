#include "Heap.hpp"
#include <string>

using std::cout;
using std::cin;
using AStar::Heap;
using AStar::colorear;
using std::string;
using std::to_string;
using std::pair;


#define ROWS 10
#define COLS 10
#define PRINT(VALUE) cout << VALUE
#define INF 20000000
#define MIN -20000000

class Map {
    double map[ROWS][COLS] = {
           {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1},
           {-1,INF,INF,INF,INF,INF,INF,INF,INF,-1},
           {-1,INF,INF,-1,-1,-1,INF,INF,INF,-1},
           {-1,INF,INF,-1,INF,INF,INF,-1,-1,-1},
           {-1,INF,-1,-1,-1,INF,INF,-1,INF,-1},
           {-1,INF,INF,INF,-1,INF,INF,-1,INF,-1},
           {-1,INF,INF,INF,-1,INF,INF,-1,INF,-1},
           {-1,INF,INF,INF,-1,-1,-1,-1,INF,-1},
           {-1,INF,INF,INF,INF,INF,INF,INF,INF,-1},
           {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1}
    };
public:
    Map() {
    }
    void print() {
        for (size_t i = 0; i < ROWS; ++i) {
            for (size_t j = 0; j < COLS; ++j) {
               if (map[i][j] == -1) {
                    PRINT(char(219)); // WALL
                }
                else if (map[i][j] == -2){
                    PRINT("+"); // VISITED
                }
                else if (map[i][j] == MIN){
                    PRINT("*"); // Final Path
                }
                else if (map[i][j] == INF){
                    PRINT(" "); //  Not Explored
                }
                else {
                    PRINT("-"); //  Explored
                }
            }
             cout << "\n";
        }
        
    }
    bool exists(size_t x, size_t y) {
        return (y >= 0 && y < ROWS) && (x >= 0 && x < COLS);
    }
    bool isWall(size_t x, size_t y) {
        return (exists(x, y)) ? map[y][x] == -1 || map[y][x] == -2 : true;
    }
    bool isVisited(size_t x, size_t y) {
        return map[y][x] == -2;
    }
    void setVisited(size_t x, size_t y) {
        map[y][x] = -2;
    }
    void setweight(size_t x, size_t y, double value) {
        map[y][x] = value;
    }
    double getWeight(size_t x, size_t y) {
        return map[y][x];
    }
    double h(int x,int y, int xf, int yf) {
        return abs(x - xf) + abs(y - yf);
    }
};

struct Coord {
    int x,y;
    Coord* parent;
    Coord(int x = -1, int y = -1): x(x), y(y), parent(nullptr) {}
    string toString(){
        return "(" + to_string(x) + "," + to_string(y) + ")";
    }
};

#define PAIR pair<Coord*,double>

class As {
    Map* map;
    Heap<PAIR>* openList;
public:
    As(){
        map = new Map;
        auto comp = [](PAIR a, PAIR b) -> bool {
            return a.second < b.second;
        };
        openList = new Heap<PAIR>(comp);
    }
    ~As(){
        delete openList;
        delete map;
    }
    void Algorithm(int xi, int yi, int xf, int yf){
        Coord* parent = nullptr;
        Coord* current = nullptr;
        Coord* c = new Coord(xi,yi);
        map->setweight(xi,yi,0.0);
        openList->push(PAIR(c,0));
        while (openList->Size()){
            PAIR p = openList->pop();
            int x = p.first->x;
            int y = p.first->y;
            double cost = map->getWeight(x,y);
            if(map->isVisited(x,y) == false){
                map->setVisited(x,y);
                parent = p.first;
            }
            else 
                continue;
            if(x == xf && y == yf){
                current = p.first;
                break;
            }
            vector<Coord*> adj = {new Coord(x,y-1), new Coord(x,y+1), new Coord(x-1,y), new Coord(x+1,y)};
            for(auto& ad: adj){
                if(map->isWall(ad->x,ad->y))
                    continue;
                double g = cost + 1;
                double h = map->h(ad->x,ad->y,xf,yf);
                double f = g + h;
                if(g < map->getWeight(ad->x,ad->y)){
                    map->setweight(ad->x,ad->y,g);
                    ad->parent = parent;
                    openList->push(PAIR(ad,f));
                }
            }
        }
        while(current != nullptr){
            map->setweight(current->x, current->y,MIN);
            current = current->parent;
        }
        map->print();
    }
};

int main(){
    As a;
    a.Algorithm(1,1,6,4);
    return 0;
}
