package spotippos;


import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.FileReader;
import java.util.List;
import java.util.ArrayList;
import java.util.Map.Entry;
import java.util.Iterator;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import spotippos.entity.Boundary;
import spotippos.entity.Province;
import spotippos.entity.GeoPoint;

/**
 * Created by drudi on 27/07/16.
 */
public class Provinces {
    private static Provinces ourInstance = new Provinces();
    private List<Province> provinces = new ArrayList<Province>();

    public static Provinces getInstance() {
        return ourInstance;
    }

    private Provinces() {
    }

    private String loadFile(String filename) {
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(new FileReader(filename));
        } catch (FileNotFoundException e) {
            System.out.println("Arquivos de dados nao encontrado: " + e.getMessage());

        }
        String line = null;
        StringBuilder builder = new StringBuilder();
        String lf = System.getProperty("line.separator");

        try {
            while ((line = reader.readLine()) != null) {
                builder.append(line);
                builder.append(lf);
            }

        } catch (IOException e) {
            System.out.println("Impossivel carregar o arquivo de Dados: " + e.getMessage());
            System.exit(2);
        }

        return builder.toString();
    }

    public void parseJson(String filename) {
        String dadosStr = loadFile(filename);
        ObjectMapper mapper = new ObjectMapper();
        JsonNode dados = null;
        try {
            dados  = mapper.readTree(dadosStr);
        } catch (IOException e) {
            e.printStackTrace();
            System.exit(2);
        }

        System.out.println(dados.getClass());

        Iterator<Entry<String, JsonNode>> nodeIter = dados.fields();
        while (nodeIter.hasNext()) {
            Entry<String, JsonNode> item = nodeIter.next();
            Province province = new Province();
            province.setName(item.getKey());
            Boundary boundaries = new Boundary();
            GeoPoint upperLeft = new GeoPoint(item.getValue().get("boundaries").get("upperLeft").get("x").asInt(),
                    item.getValue().get("boundaries").get("upperLeft").get("y").asInt());
            GeoPoint lowerRight = new GeoPoint(item.getValue().get("boundaries").get("bottomRight").get("x").asInt(),
                    item.getValue().get("boundaries").get("bottomRight").get("y").asInt());

            boundaries.setBottomRight(lowerRight);
            boundaries.setUpperLeft(upperLeft);
            province.setBoundaries(boundaries);

            this.provinces.add(province);
        }
    }

    public List<Province> getProvinces() {
        return provinces;
    }
}
