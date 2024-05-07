import java.util.Scanner;

public class xx{

    static Scanner sc = new Scanner(System.in);

    public static void selection_sort(int arr[]){
        for(int i=0;i<arr.length;i++){
            int min_index = i;
            for(int j=i;j<arr.length;j++){
                if(arr[j] < arr[min_index]){
                    min_index = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[min_index];
            arr[min_index] = temp;
        }
    }

    public static void selection_sort_desc(int arr[]){
        for(int i=0;i<arr.length;i++){
            int max_index = i;
            for(int j=i;j<arr.length;j++){
                if(arr[j] > arr[max_index]){
                    max_index = j;
                }
            }
            int temp = arr[i];
            arr[i] = arr[max_index];
            arr[max_index] = temp;
        }
    }

    public static int[] accept(int n){
        int arr[] = new int[n];
        System.out.println("Enter elements: ");
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        return arr;
    }

    public static void display(int arr[], int n){
        for(int i=0;i<n;i++){
            System.out.print(arr[i]+"  ");
        }
    }
    
    public static void main(String[] args) {
        
        System.out.println("\nEnter total number of elements: ");
        int n = sc.nextInt();
        int arr[] = accept(n);
        selection_sort(arr);
        display(arr,n);
        System.out.println("\nDescending: ");
        selection_sort_desc(arr);
        display(arr, n);
    }
}
