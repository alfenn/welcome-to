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
        // ArrayList<JSONObject> tokens = parseObjects(readFileToString("input.txt"));
        ArrayList<JSONObject> tokens = parseObjects(readInputToString());
        // TODO
        // testPrintTokens(tokens);
        // Discard non-special JSON objects
        ArrayList<JSONObject> toRemove = new ArrayList<>();
        for (JSONObject t : tokens) {
            JSONParser jsonParser = new JSONParser();
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
        // TODO: 
        // testPrintTokens(filteredTokens);

        // Discard extra elements.
        int numExtra = filteredTokens.size() % 10;
        for (int i = 0; i<numExtra; i++) {
            filteredTokens.remove(filteredTokens.size()-1);
        }
        // TODO:
        // testPrintTokens(filteredTokens);

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

    public static ArrayList<JSONObject> parseObjects(String jsonStr) throws ParseException {
        ArrayList<JSONObject> tokens = new ArrayList<>();
        boolean readingDict = false;
        String t = "";
        int numNestedBraces = 0;
        int numNestedBrackets = 0;
        boolean inStr = false;
        boolean inArr = false;
        for (int i = 0; i<jsonStr.length(); i++) {
            char c = jsonStr.charAt(i);
            // Set conditions for inStr.
            if (c == '"') {
                // To avoid out of bounds error for checking jsonStr[(i=0)-1], add edge case for when input starts with string.
                if (i == 0) {
                    inStr = true;
                } 
                else {
                    if (jsonStr.charAt(i-1) != '\\') {                        
                        if (!inStr) inStr = true;
                        else inStr = false;
                    }
                }                
            }
            // Split the nested braces operations from readingDict case below so we don't count first '{' as nested
            if (readingDict && !inStr) {
                if (c == '{') numNestedBraces ++;
            }

            // If not currently reading a top-level dictionary.
            if (!readingDict && !inStr) {
                if (c == '[') {
                    if (inArr) numNestedBraces ++;
                    else inArr = true;
                }
                if (c == '{' && !inArr) readingDict = true;
                if (c == ']') {
                    if (numNestedBrackets != 0) numNestedBraces --;
                    else inArr = false;
                }
            }

            // If currently reading a top-level dictionary.
            if (readingDict) {
                t += c;
                // Split this from the numNestBraces++ case above so we include the '}' in it.
                if (!inStr && c == '}') {
                    if (numNestedBraces == 0) {
                        JSONParser jsonParser = new JSONParser();
                        tokens.add((JSONObject) jsonParser.parse(t));
                        t = "";
                        readingDict = false;
                    }
                    // Check != 0 so we don't count actual closing '}' as nested.
                    // Put this under the previuos condition so { { {} } } doens't chop off the last '}'
                    if (numNestedBraces != 0) numNestedBraces --;
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

    public static void testPrintTokens (ArrayList<JSONObject> tokens) {
        ArrayList<String> ret = new ArrayList<>();
        for (JSONObject t : tokens) {
            ret.add(t.toJSONString());
        }
        System.out.println(ret);
    }
}
