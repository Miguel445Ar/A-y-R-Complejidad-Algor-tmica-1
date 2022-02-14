#ifndef __HEAP_HPP__
#define __HEAP_HPP__
#include <iostream>
#include <functional>
#include <vector>
#include <windows.h>

using std::function;
using std::vector;


// left child -> 2 * i + 1
// right chuld -> 2 * i + 2
// parent of a node i -> (i - 1) / 2


namespace AStar {
    template<class T>
    class Heap {
        vector<T>* heap;
        function<bool(T,T)> comp;
    public:
        Heap(function<bool(T,T)> comp): comp(comp){ heap = new vector<T>; }
        ~Heap(){ 
            if (!heap->empty())
                heap->clear();
            delete heap;
        }
        void push(T value){
            heap->push_back(value);
            heapifyForInsertion();
        }
        T pop(){
            if(heap->size() == 0)
                return T();
            T value = (*heap)[0];
            (*heap)[0] = (*heap)[heap->size() - 1];
            heap->pop_back();
            heapyfyForElimination();
            return value;
        }
        size_t Size(){
            return heap->size();
        }
    private:
        void heapifyForInsertion() {
            if (heap->size() <= 1)
                return;
            size_t child = heap->size() - 1;
            size_t parent = (child - 1) / 2;
            while (comp((*heap)[child],(*heap)[parent])){
                swap((*heap)[child],(*heap)[parent]);
                if (parent == 0)
                    break;
                child = parent;
                parent = (child - 1) / 2;
            }
        }
        void heapyfyForElimination(){
            if(heap->size() <= 1)
                return;
            size_t parent = 0;
            while (true){
                size_t leftChild = 2 * parent + 1;
                size_t rightChild = 2 * parent + 2;
                if (leftChild >= heap->size() && rightChild >= heap->size())
                    break;
                size_t r;
                if(leftChild >= heap->size())
                    r = rightChild;
                else if (rightChild >= heap->size())
                    r = leftChild;
                else
                    r = (comp((*heap)[leftChild],(*heap)[rightChild]))? leftChild: rightChild;
                if(comp((*heap)[r],(*heap)[parent])){
                    swap((*heap)[r],(*heap)[parent]);
                    parent = r;
                    continue;
                }
                break;
            }
        }
        void swap(T& a, T& b){
            T c = a;
            a = b;
            b = c;
        }
    };
    //Función para colocar el cursor en cualquier posición
	void gotoxy(int x, int y){ HANDLE hcon; hcon=GetStdHandle(STD_OUTPUT_HANDLE); COORD dwPos; dwPos.X=x; dwPos.Y=y; SetConsoleCursorPosition(hcon, dwPos);}
	//Función para colorear un caracter en la pantalla
    void colorear(int c){ SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE),c);}
    //Función para ocultar el cursor en pantalla
    void ocultar_cursor(){ HANDLE hcon; hcon=GetStdHandle(STD_OUTPUT_HANDLE); CONSOLE_CURSOR_INFO cci; cci.dwSize=50; cci.bVisible=FALSE;
	SetConsoleCursorInfo(hcon,&cci);}
}
#endif