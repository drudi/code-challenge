package spotippos.entity;

/**
 * Created by drudi on 27/07/16.
 */
public class GeoPoint {
    private int x;
    private int y;

    public GeoPoint(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
}
