/*UNIVERSIDAD DE LAS FUERZAS ARMADAS- ESPE
Autor:Pamela Jesabel Carriel Mier 
Ordenacion Distribución
Fecha : 05 de junio del 2023*/
#include <iostream>
#include <algorithm>
using namespace std;

int* countingSort(int arr[], int n) {
    // Encontrar el rango de valores en el arreglo
    int max_value = *max_element(arr, arr + n);
    int min_value = *min_element(arr, arr + n);
    int range_value = max_value - min_value + 1;

    // Inicializar el arreglo de conteo y el arreglo de salida
    int* count = new int[range_value]();
    int* output = new int[n];

    // Contar la frecuencia de cada elemento en el arreglo
    for (int i = 0; i < n; i++) {
        count[arr[i] - min_value]++;
    }

    // Calcular las posiciones finales de los elementos en el arreglo ordenado
    for (int i = 1; i < range_value; i++) {
        count[i] += count[i - 1];
    }

    // Colocar los elementos en el arreglo de salida en orden
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i] - min_value] - 1] = arr[i];
        count[arr[i] - min_value]--;
    }

    delete[] count;
    return output;
}

int main() {
    int arr[] = {5, 2, 8, 12, 1, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    cout << "Array original:" << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    int* arr_ordenado = countingSort(arr, n);

    cout << "Array ordenado:" << endl;
    for (int i = 0; i < n; i++) {
        cout << arr_ordenado[i] << " ";
    }
    cout << endl;

    delete[] arr_ordenado;

    return 0;
}
