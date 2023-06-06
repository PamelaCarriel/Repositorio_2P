/*UNIVERSIDAD DE LAS FUERZAS ARMADAS- ESPE
Autor:Pamela Jesabel Carriel Mier 
Ordenacion Quicksort
Fecha : 05 de junio del 2023*/
public class Quicksort {
    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }

    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 8, 12, 1, 6};
        System.out.println("Array original:");
        imprimirArray(arr);

        quickSort(arr, 0, arr.length - 1);

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
