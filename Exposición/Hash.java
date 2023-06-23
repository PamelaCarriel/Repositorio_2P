package Exposición;
import java.util.HashMap;

public class Hash {
    public static void main(String[] args) {
        HashMap<Integer, String> employees = new HashMap<>();
        employees.put(123, "Juan Pérez");
        employees.put(456, "María López");
        employees.put(789, "Pedro Gómez");
        employees.put(234, "Ana Rodríguez");

        int idNumber = 789;

        if (employees.containsKey(idNumber)) {
            String employeeName = employees.get(idNumber);
            System.out.println("El empleado con el número de identificación " + idNumber + " es " + employeeName);
        } else {
            System.out.println("No se encontró un empleado con el número de identificación " + idNumber);
        }
    }
}