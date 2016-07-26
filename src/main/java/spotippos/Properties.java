package spotippos;

import spotippos.entity.Property;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.FileReader;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.LinkedHashMap;

import org.springframework.boot.json.JacksonJsonParser;

/**
 * Created by drudi on 26/07/16.
 */
public class Properties {
    private static Properties ourInstance = new Properties();
    private Long totalProperties;
    private List<Property> properties = new ArrayList<Property>();

    public static Properties getInstance() {
        return ourInstance;
    }

    private Properties() {

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
        JacksonJsonParser parser = new JacksonJsonParser();
        String dadosStr = loadFile(filename);
        Map<String, Object> dados = parser.parseMap(dadosStr);
        totalProperties = (Long)dados.get("totalItems");

        for (LinkedHashMap<String, Object> item : (List<LinkedHashMap<String, Object>>)dados.get("properties")) {
            Property property = new Property();
            property.setId((int)item.get("id"));
            property.setX((int) item.get("x"));
            property.setY((int) item.get("y"));
            property.setBaths((int) item.get("baths"));
            property.setBeds((int) item.get("beds"));
            property.setSquareMeters((int) item.get("squareMeters"));

            if (item.containsKey("description")) {
                property.setDescription((String) item.get("description"));
            }
            if (item.containsKey("title")) {
                property.setTitle((String) item.get("title"));
            }
            if (item.containsKey("price")) {
                property.setPrice((double) item.get("price"));
            }
            if (item.containsKey("provinces")) {
                property.setProvinces((List<String>) item.get("provinces"));
            }

            properties.add(property);
        }

    }

    public Long getTotalProperties() {
        return totalProperties;
    }

    public List<Property> getProperties() {
        return properties;
    }
}
