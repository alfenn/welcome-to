import java.io.*;
import java.util.ArrayList;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;


public class Runner_2_2 {
    public static void run() throws Exception {
        // String json = readFileToString("input.txt");
        String json = readInputToString();
        String[] tokens_s = json.split("\\{");
        for (int i = 0; i < tokens_s.length; i++) {
            tokens_s[i] = "{" + tokens_s[i];
        }
        // Convert and dump the string tokens into a new array.
        JSONParser jsonParser = new JSONParser();
        ArrayList<JSONObject> tokens_o = new ArrayList<>();
        for (int i = 1; i < tokens_s.length; i++) {
            Object obj = jsonParser.parse(tokens_s[i]);
            tokens_o.add((JSONObject) obj);
        }
        sort(tokens_o);
        // Write JSON to stdout.
        ArrayList<String> tokens_o_strings = new ArrayList<>();
        for (int i = 0; i<tokens_o.size(); i++) {
            tokens_o_strings.add(tokens_o.get(i).toJSONString());
        }
        System.out.print(tokens_o_strings.toString());
    }

    // Read everything from a file into a string.
    public static String readFileToString(String p) throws IOException {
        File f = new File(p);
        BufferedReader br = new BufferedReader(new FileReader(f));
        String out = "";
        String reader;
        while ((reader = br.readLine()) != null) {
            out += reader;
        }
        return out;
    }

    public static String readInputToString() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String out = "";
        String reader;
        while ((reader = br.readLine()) != null) {
            out += reader;
        }
        return out;
    }

    // Implement bubble sort.
    public static void sort(ArrayList<JSONObject> tokens){
        int numIter = 0;
        boolean swapped = true;
        // for (JSONObject e : tokens) {
        //     if (e == null) {
        //         System.out.println("null");
        //     } else {
        //         System.out.println(e.toJSONString());
        //     }
        // }
        while (swapped) {
            swapped = false;
            for (int i = 0; i < tokens.size() - numIter - 1; i++) {
                if ((long) tokens.get(i).get("content") > (long) tokens.get(i + 1).get("content")) {
                    JSONObject temp = tokens.get(i);
                    tokens.set(i, tokens.get(i + 1));
                    tokens.set(i + 1, temp);
                    swapped = true;
//                    long[] testTokens = new long[tokens.length];
//                    for (int j = 0; j<testTokens.length; j++) {
//                        testTokens[j] = (long) tokens[j].get("content");
//                    }
//                    System.out.println(testTokens);
                }
            }
            numIter ++;
        }
    }

}
