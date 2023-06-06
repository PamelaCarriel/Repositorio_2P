/*UNIVERSIDAD DE LAS FUERZAS ARMADAS- ESPE
Autor:Pamela Jesabel Carriel Mier 
Ordenacion Radix
Fecha : 05 de junio del 2023*/
public class OrdenaciónRadix{
    public static void countingSort(int[] arr, int exp) {
        int n = arr.length;
        int[] output = new int[n];
        int[] count = new int[10];

        for (int i = 0; i < n; i++) {
            int index = arr[i] / exp;
            count[index % 10]++;
        }

        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }

        for (int i = n - 1; i >= 0; i--) {
            int index = arr[i] / exp;
            output[count[index % 10] - 1] = arr[i];
            count[index % 10]--;
        }

        System.arraycopy(output, 0, arr, 0, n);
    }

    public static void radixSort(int[] arr) {
        int max_value = Integer.MIN_VALUE;

        for (int num : arr) {
            if (num > max_value) {
                max_value = num;
            }
        }

        int exp = 1;
        while (max_value / exp > 0) {
            countingSort(arr, exp);
            exp *= 10;
        }
    }

    public static void main(String[] args) {
        int[] arr = {170, 45, 75, 90, 802, 24, 2, 66};
        System.out.println("Array original:");
        imprimirArray(arr);

        radixSort(arr);

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
