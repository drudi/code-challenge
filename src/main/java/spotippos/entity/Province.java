package spotippos.entity;


/**
 * Created by drudi on 27/07/16.
 */
public class Province {
    private String name;
    private Boundary boundaries;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Boundary getBoundaries() {
        return boundaries;
    }

    public void setBoundaries(Boundary boundaries) {
        this.boundaries = boundaries;
    }
}
