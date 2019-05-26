import org.opencv.core.Mat;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;

import static org.opencv.highgui.HighGui.*;

public class Main {

    public static void main(String[] args) {

        //caminho da bibliotexa do OPENCV
        System.load("/home/ricardo/Documents/opencv/build/lib/libopencv_java410.so");
        System.out.println("Inicio");

        String window_name = "Lido em escala cinza";
        String window_name2 = "Apos Binzarisation";
        //caminho da imagem
        String imageName = "/home/ricardo/Downloads/img7.jpeg";
        Imgcodecs imageCodecs = new Imgcodecs();
        Mat img = new Mat();

        //define a imagem
        img.create(1024,512,0);
        //cria tipo scaner parea imagens
        img = imageCodecs.imread(imageName,0);

        //cria janela da imagem 1
        namedWindow(window_name, WINDOW_NORMAL);

        //mostra imagem 1 na janela criada
        imshow(window_name, img);

        System.out.println("Image Loaded");

        //chama função de binzarisar
        Mat result = binarize(img,Imgproc.THRESH_OTSU);


       // Imgproc.morphologyEx(result,result,Imgproc.MORPH_OPEN, kernel);

        //cria janela da imagem 2
        namedWindow(window_name2, WINDOW_NORMAL);
        //mostra imagem 2 na janela criada
        imshow(window_name2, result);

        //para ter tempo de aparecer as imagens
        waitKey(10);

    }

    //Diferentes tipos de binarisar
    public static Mat binarize(Mat img, int flag){
        Mat imB = new Mat();
        if(flag == Imgproc.THRESH_BINARY)
            Imgproc.threshold(img,imB,0,255,Imgproc.THRESH_BINARY);
        if(flag == Imgproc.THRESH_OTSU)
            Imgproc.threshold(img,imB,0,255,Imgproc.THRESH_BINARY+Imgproc.THRESH_OTSU);
        if(flag == Imgproc.ADAPTIVE_THRESH_GAUSSIAN_C)
            Imgproc.adaptiveThreshold(img,imB,255,Imgproc.ADAPTIVE_THRESH_GAUSSIAN_C,Imgproc.THRESH_BINARY,7,2);
        if(flag == Imgproc.ADAPTIVE_THRESH_MEAN_C)
            Imgproc.adaptiveThreshold(img,imB,255,Imgproc.ADAPTIVE_THRESH_MEAN_C,Imgproc.THRESH_BINARY,7,2);
        return imB;
    }
}
