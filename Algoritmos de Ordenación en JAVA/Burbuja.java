/*UNIVERSIDAD DE LAS FUERZAS ARMADAS- ESPE
Autor:Pamela Jesabel Carriel Mier 
Ordenacion Burbuja
Fecha : 05 de junio del 2023*/
public class Burbuja {
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
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

    public static void main(String[] args) {
        int[] arr = {5, 2, 8, 12, 1, 6};
        System.out.println("Array original:");
        imprimirArray(arr);
        
        bubbleSort(arr);
        
        System.out.println("Array ordenado:");
        imprimirArray(arr);
    }

    public static void imprimirArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
