/*UNIVERSIDAD DE LAS FUERZAS ARMADAS- ESPE
Autor:Pamela Jesabel Carriel Mier 
Ordenacion por intercambio 
Fecha : 05 de junio del 2023*/
public class Intercambio{
    public static void bubbleSort(int[] array) {
        int n = array.length;
        boolean intercambio;
        
        for (int i = 0; i < n - 1; i++) {
            intercambio = false;
            
            for (int j = 0; j < n - 1 - i; j++) {
                if (array[j] > array[j + 1]) {
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                    intercambio = true;
                }
            }
            
            if (!intercambio) {
                break;
            }
        }
    }
    
    // Ejemplo de uso
    public static void main(String[] args) {
        int[] array = {5, 2, 8, 12, 1, 6};
        
        System.out.println("Lista original:");
        imprimirArray(array);
        
        bubbleSort(array);
        
        System.out.println("Lista ordenada:");
        imprimirArray(array);
    }
    
    public static void imprimirArray(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }
}
