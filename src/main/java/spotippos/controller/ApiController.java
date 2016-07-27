package spotippos.controller;

import spotippos.Properties;
import spotippos.Provinces;
import spotippos.entity.Province;
import spotippos.entity.Property;
import org.springframework.web.bind.annotation.*;
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
    public String property(@PathVariable("id") Long id) {
        return String.format("ID: %d", id);
    }

    @RequestMapping(value = "/properties", method = RequestMethod.POST)
    public Property addProperty(@RequestBody Property body, HttpServletResponse response) {
        response.setStatus(201);
        return body;
    }

    @RequestMapping(value = "/all", method = RequestMethod.GET)
    public List<Property> getAll() {
        return Properties.getInstance().getProperties();
    }

    @RequestMapping(value = "/provinces", method = RequestMethod.GET)
    public List<Province> getProvinces() {
        List<Province> provs = Provinces.getInstance().getProvinces();

        return provs;
    }
}
