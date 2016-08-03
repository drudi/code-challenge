package spotippos.controller;

import com.fasterxml.jackson.databind.node.ObjectNode;
import spotippos.Properties;
import spotippos.Provinces;
import spotippos.entity.Province;
import spotippos.entity.Property;
import org.springframework.web.bind.annotation.*;
import spotippos.model.SpotipposSearch;

import javax.servlet.http.HttpServletResponse;
import java.util.List;
import java.util.Map;
import java.util.LinkedHashMap;

/**
 * Created by drudi on 26/07/16.
 */

@RestController
public class ApiController {

    @RequestMapping(value = "/properties/{id}", method = RequestMethod.GET)
    public Property property(@PathVariable("id") Long id) {
        SpotipposSearch spSearch = new SpotipposSearch();
        return spSearch.findPropertyById(id);
    }

    @RequestMapping(value = "/properties", method = RequestMethod.POST)
    public Property addProperty(@RequestBody Property body, HttpServletResponse response) {
        response.setStatus(201);
        return body;
    }

    @RequestMapping(value = "/all", method = RequestMethod.GET)
    public Map<String, Object> getAll() {
        List<Property> properties = Properties.getInstance().getProperties();
        Map<String, Object> rootNode = new LinkedHashMap<>();
        rootNode.put("totalProperties", properties.size());
        rootNode.put("properties", properties);
        return rootNode;
    }

    @RequestMapping(value = "/provinces", method = RequestMethod.GET)
    public List<Province> getProvinces() {
        List<Province> provs = Provinces.getInstance().getProvinces();

        return provs;
    }
}
