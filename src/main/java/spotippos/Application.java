package spotippos;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Created by drudi on 26/07/16.
 */
@SpringBootApplication
public class Application {

    public static void main(String[] args) {
        Properties props = Properties.getInstance();
        props.parseJson("properties.json");
        SpringApplication.run(Application.class, args);
    }
}
