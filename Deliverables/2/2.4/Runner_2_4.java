import java.io.*;
import java.util.ArrayList;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class Runner_2_4 {
    public static void run() throws IOException, ParseException {
        frontend();
    }

    public static void frontend() throws IOException, ParseException {
//        ArrayList<JSONObject> tokens = parseObjects(readFileToString("src/input.txt"));
        ArrayList<JSONObject> tokens = parseObjects(readInputToString());

        // Discard non-special JSON objects
        ArrayList<JSONObject> toRemove = new ArrayList<>();
        for (JSONObject t : tokens) {
            JSONParser jsonParser = new JSONParser();
//            if (t.keySet() != ((JSONObject) jsonParser.parse("{\"content\":1}")).keySet()
            if (t.keySet().size() != 1
                    || !t.containsKey("content")
                    || !(t.get("content") instanceof Long)
                    || !hasAllowedValue((Long)t.get("content"))) {
                toRemove.add(t);
            }
        }
        ArrayList<JSONObject> filteredTokens = new ArrayList<>();
        for (JSONObject t : tokens) {
            boolean bad = false;
            for (JSONObject tBad : toRemove) {
                if (t == tBad) {
                    bad = true;
                    break;
                }
            }
            if (!bad) filteredTokens.add(t);
        }

        // Discard extra elements.
        int numExtra = filteredTokens.size() % 10;
        for (int i = 0; i<numExtra; i++) {
            filteredTokens.remove(filteredTokens.size()/10);
        }

        // Group tokens into groups of 10.
        ArrayList<ArrayList<JSONObject>> groupedTokens = new ArrayList<>();
        for (int i = 0; i<filteredTokens.size()/10; i++) {
            ArrayList<JSONObject> temp = new ArrayList<>();
            for (int j = 0; j < 10; j++) {
                temp.add(filteredTokens.get(10 * i + j));
            }
            groupedTokens.add(temp);
        }

        // Sort each group of tokens in place using the backend.
        for (int i = 0; i<groupedTokens.size(); i++) {
            sort(groupedTokens.get(i));
        }

        // Write JSON to stdout.
        JSONParser jsonParser = new JSONParser();
        ArrayList<String> out = new ArrayList<>();
        for (int i = 0; i < groupedTokens.size(); i++) {
            ArrayList<String> temp = new ArrayList<>();
            for (int j = 0; j < 10; j++) {
                temp.add(groupedTokens.get(i).get(j).toJSONString());
            }
            out.add(temp.toString());
        }
        System.out.println(out.toString());
    }

    public static ArrayList<JSONObject> parseObjects(String in) throws ParseException {
        ArrayList<JSONObject> tokens = new ArrayList<>();
        boolean readingDict = false;
        String t = "";
        int numNestedBrackets = 0;
        boolean inStr = false;
        for (int i = 0; i<in.length(); i++) {
            char c = in.charAt(i);
            if (c == '{') {
                if (readingDict && !inStr) {
                    numNestedBrackets ++;
                }
                readingDict = true;
            }
            if (readingDict) {
                t += c;
            }
            if (c == '"') {
                if (!inStr) {
                    inStr = true;
                }
                else {
                    inStr = false;
                }
            }
            if (c == '}'){
                if (readingDict && !inStr && numNestedBrackets==0) {
                    JSONParser jsonParser = new JSONParser();
                    tokens.add((JSONObject) jsonParser.parse(t));
                    t = "";
                    readingDict = false;
                }
                else if (!inStr && readingDict) {
                    numNestedBrackets --;
                }
            }
        }
        return tokens;
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

    public static boolean hasAllowedValue(long l){
        long[] allowed = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24};
        for (long z : allowed) {
            if (z == l) return true;
        }
        return false;
    }

    // Implement bubble sort.
    public static void sort(ArrayList<JSONObject> tokens){
        int numIter = 0;
        boolean swapped = true;
        while (swapped) {
            swapped = false;
            for (int i = 0; i < tokens.size() - numIter - 1; i++) {
                if ((long) tokens.get(i).get("content") > (long) tokens.get(i + 1).get("content")) {
                    JSONObject temp = tokens.get(i);
                    tokens.set(i, tokens.get(i + 1));
                    tokens.set(i + 1, temp);
                    swapped = true;
                }
            }
            numIter ++;
        }
    }
}
