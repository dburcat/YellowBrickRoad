package rocks.zipcode.dreamhouse;


import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;


/**
 * The test class PictureTest.
 *
 * @author  (your name)
 * @version (a version number or a date)
 */
public class PictureTest
{
    /**
     * Default constructor for test class PictureTest
     */
    public PictureTest()
    {
    }


    @Test
    public void DrawTest()
    {
        Picture picture1 = new Picture();
        picture1.draw();
    }
}

