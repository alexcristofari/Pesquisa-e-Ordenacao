import java.util.ArrayList;

public class Principal {
    public static void main(String[] args) {
        ArrayList<Integer> listaNumeros = new ArrayList<>();
        ArrayList<String> listaPalavras = new ArrayList<>();

        Util.popularListaNumerosAleatorio(listaNumeros, 10, 50, 100);
        Util.exibirListaNumeros(listaNumeros);

        Util.popularListaPalavrasAleatorio(listaPalavras, 10, 10);
        Util.exibirListaPalavras(listaPalavras);
    }
}