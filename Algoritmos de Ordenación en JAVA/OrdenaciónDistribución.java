/*UNIVERSIDAD DE LAS FUERZAS ARMADAS- ESPE
Autor:Pamela Jesabel Carriel Mier 
Ordenacion Distribución
Fecha : 05 de junio del 2023*/
public class OrdenaciónDistribución {
    public static int[] countingSort(int[] arr) {
        // Encontrar el rango de valores en el arreglo
        int max_value = Integer.MIN_VALUE;
        int min_value = Integer.MAX_VALUE;
        for (int num : arr) {
            max_value = Math.max(max_value, num);
            min_value = Math.min(min_value, num);
        }
        int range_value = max_value - min_value + 1;

        // Inicializar el arreglo de conteo y el arreglo de salida
        int[] count = new int[range_value];
        int[] output = new int[arr.length];

        // Contar la frecuencia de cada elemento en el arreglo
        for (int num : arr) {
            count[num - min_value]++;
        }

        // Calcular las posiciones finales de los elementos en el arreglo ordenado
        for (int i = 1; i < range_value; i++) {
            count[i] += count[i - 1];
        }

        // Colocar los elementos en el arreglo de salida en orden
        for (int i = arr.length - 1; i >= 0; i--) {
            int num = arr[i];
            output[count[num - min_value] - 1] = num;
            count[num - min_value]--;
        }

        return output;
    }

    public static void main(String[] args) {
        int[] arr = {5, 2, 8, 12, 1, 6};
        System.out.println("Array original:");
        imprimirArray(arr);

        int[] arr_ordenado = countingSort(arr);

        System.out.println("Array ordenado:");
        imprimirArray(arr_ordenado);
    }

    public static void imprimirArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}
