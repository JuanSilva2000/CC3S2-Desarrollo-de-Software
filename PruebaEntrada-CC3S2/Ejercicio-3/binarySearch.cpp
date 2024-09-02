#include<iostream>
using namespace std;

int main() {
    int array[7] = {2,5,7,10,13,15,19};
    int n = 7;
    int numero; 

    cout<<"Ingrese el numero a buscar: ";cin>>numero;

    int primero = 0; 
    int ultimo = n-1;
    int medio = (ultimo + primero)/2;

    while(primero<=ultimo){
        if(array[medio] < numero) {
            primero = medio+1;
        }else if (array[medio] > numero) {
            ultimo = medio -1;
        }else {
            cout<<"Se encontro el numero "<<numero<<endl;
            cout<<"Posición: "<<medio+1;
            break;
        }

        medio = (primero + ultimo)/2;
    }

    return 0;
}






