/*UNIVERSIDAD DE LAS FUERZAS ARMADAS- ESPE
Autor:Pamela Jesabel Carriel Mier 
Ordenacion Burbuja
Fecha : 05 de junio del 2023*/
#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
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
