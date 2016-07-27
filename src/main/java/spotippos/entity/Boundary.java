package spotippos.entity;


/**
 * Created by drudi on 27/07/16.
 */
public class Boundary {
    private GeoPoint upperLeft;
    private GeoPoint bottomRight;

    public GeoPoint getUpperLeft() {
        return upperLeft;
    }

    public void setUpperLeft(GeoPoint upperLeft) {
        this.upperLeft = upperLeft;
    }

    public GeoPoint getBottomRight() {
        return bottomRight;
    }

    public void setBottomRight(GeoPoint bottomRight) {
        this.bottomRight = bottomRight;
    }
}
