import java.util.ArrayList;
import java.util.Collection;
//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
void main() {

    ArrayList<String> tasks = new ArrayList<>();
    tasks.add("Купить еду");
    tasks.add("Постирать вещи");
    tasks.add("Завести будильник");

    int raz = tasks.size();
    for (int i = 0;i<raz;i++){
        IO.println(String.format(tasks.get(i)));
    }

    IO.println(String.format("-----------------"));

    tasks.remove(1);

    raz = tasks.size();
    for (int i = 0;i<raz;i++){
        IO.println(String.format(tasks.get(i)));
    }

    IO.println(String.format("-----------------"));
    Collections.sort(tasks);
    for (int i = 0;i<raz;i++){
        IO.println(String.format(tasks.get(i)));
    }



}
