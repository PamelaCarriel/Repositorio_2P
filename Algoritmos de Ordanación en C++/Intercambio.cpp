/*UNIVERSIDAD DE LAS FUERZAS ARMADAS- ESPE
Autor:Pamela Jesabel Carriel Mier 
Ordenacion por intercambio 
Fecha : 05 de junio del 2023*/
#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n) {
    bool intercambio;
    
    for (int i = 0; i < n - 1; i++) {
        intercambio = false;
        
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                intercambio = true;
            }
        }
        
        if (!intercambio) {
            break;
        }
    }
}

int main() {
    int arr[] = {5, 2, 8, 12, 1, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cout << "Array original:" << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    bubbleSort(arr, n);
    
    cout << "Array ordenado:" << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
    
    return 0;
}
