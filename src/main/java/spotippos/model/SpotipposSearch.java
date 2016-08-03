package spotippos.model;

import spotippos.Properties;
import spotippos.entity.Property;

import java.util.List;

/**
 * Created by drudi on 02/08/16.
 */
public class SpotipposSearch {
    public Property findPropertyById(Long id) {
        List<Property> props = Properties.getInstance().getProperties();

        for (Property prop : props) {
            if (prop.getId() == id) {
                return prop;
            }
        }

        return null;
    }
}
