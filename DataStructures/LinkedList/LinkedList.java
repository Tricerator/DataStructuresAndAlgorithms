public class LinkedList<T> {

    private Node root;

    public LinkedList(T value ){
        root = new Node(value);
    }

    public LinkedList(){
        root = null;
    }


    public LinkedList(T[] arrayO){
     if(arrayO.length == 0){
         root = null;
     }
     else{
         root = new Node(arrayO[0]);
         for(int i = 1; i < arrayO.length; i++){
             AddValue(arrayO[i]);
         }
     }
    }

    public boolean removeValue(T value){
        if (root == null) return false;

        if(root.value == value){
            root = root.descendant;
            return true;
        }
        else{
            Node previousNode = root;
            Node node = root.descendant;
            while(node != null){
                if (node.value == value){
                    previousNode.descendant = node.descendant;
                    return true;
                }
                previousNode = node;
                node = node.descendant;
            }
            return false;
        }


    }
    public void addToBeginning(T value){
        Node node = new Node(value);
        node.descendant = root;
        root = node;
    }

    public void removeAllOccurencies(T value){
        while(removeValue(value)){

        }
    }


    public void printValues(){
        Node node = root;
        while(node != null){
            System.out.print(node.value + " ");
            node = node.descendant;
        }
        System.out.println();
    }

    public void AddValue(T value){
        if (root == null){
            root = new Node(value);
            return;
        }
        Node n = root;
        while(n.descendant != null){
            n = n.descendant;
        }
        n.descendant = new Node(value);
    }
    public boolean Search(T value){
        Node node = root;
        while(node != null){
            if(node.value.equals(value)){
                return true;
            }
            node = node.descendant;
        }
        return false;
    }

}


class Node<T> {

    T value;
    Node descendant;

    public Node(T value){

        this.value = value;
    }
}