# SpikeCV

## Results

1. ### Detect edges
    * Sobel:
        ![alt text](./imgs/results/Sobel.jpg "Logo Title Text 1")
    * Roberts:
        ![alt text](./imgs/results/Roberts.jpg "Logo Title Text 1")
    * Prewitt and Canny:
        ![alt text](./imgs/results/Prewit.jpg "Logo Title Text 1")

---

2. ### Histogram and Normalization:
        ![alt text](./imgs/results/Normalized.jpg "Logo Title Text 1")
3. ### Local and global thresholding:
        ![alt text](./imgs/results/Globalthresh.jpg "Logo Title Text 1")

---

4. ### Frequency domain filters
    * Low Pass: 
        ![alt text](./imgs/results/LowPass.jpg"Logo Title Text 1")
    * High Pass:
        ![alt text](./imgs/results/HighPass.jpg "Logo Title Text 1")
5. ### Hybrid images:
        ![alt text](./imgs/results/Hybrid.jpg "Logo Title Text 1")


---


6. ### Boundary detection
    * **Canny Superimposed:**
        ![alt text](./imgs/results/canny.png "Logo Title Text 1")
    * **Hough Lines:**
        ![alt text](./imgs/results/hough_lines.png "Logo Title Text 1")
    * **Hough Circles:**
        ![alt text](./imgs/results/circles.png "Logo Title Text 1")

---

7. ### Active Contour
    * **Object:** 
        ![alt text](./imgs/object.png "Logo Title Text 1")
    *  **initialize the contour:** 
        ![alt text](./imgs/results/Initial_setup.jpg "Logo Title Text 1")
    * **Evolved Contour:**
        ![alt text](./imgs/results/result.png "Logo Title Text 1")

---

8. ### Harris

   - _original image_:

   ![original](imgs/chess.png)

   - _output image_ :

   ![output](imgs/results/chessCorners.png)

---

9. ### SIFT

   - _original image_:

   ![original](imgs/lena.jpg)

   - _output image_ :

   ![output](imgs/results/lenaOut.png)

---

10. ### Template Matching

   - _result_:

   ![result](imgs/results/templateMatching.png)

---

11. ### Thresholding
      1. Optimal Otsu's bimodal thresholding
         * Global thresholding: 
            ![alt text](./imgs/results/optimalOtsu_global.png "Global thresholding")
         * Local thresolding: 
            ![alt text](./imgs/results/optimalOtsu_local.png "Local thresolding")
      2. Spectral thresholding (trimodal)
         * Global thresholding: 
            ![alt text](./imgs/results/spectral_global.png "Global thresholding")
         * Local thresolding: 
            ![alt text](./imgs/results/spectral_local.png  "Local thresolding")
      3. Optimal (iterative) thresholding (trimodal)
         * Global thresholding: 
            ![alt text](./imgs/results/optimal_global.png "Global thresholding")
         * Local thresolding: 
            ![alt text](./imgs/results/optimal_local.png "Local thresholding")
12. ### Segmentation
      1. K-means
         * Input:
         
            ![original](imgs/lena.jpg)
         * Output:
         
            ![original](imgs/kmeans_output.png)
      2. Region Growing
         * Input:
            
            ![original](imgs/mri.jpg)
         * Output:
         
            ![output](imgs/results/mri-out.jpg)
      3. _Agglomerative_ :
         * Input:
         
            ![original](imgs/lena.jpg)
         * Output:
         
            ![original](imgs/results/agglo_output.png)
      4. _Mean Shift_ :
         * Input:
         
            ![original](imgs/lena.jpg)
         * Output:
         
            ![original](imgs/results/meanShift_output.png)


---

13. ### Face Detection
   ![alt text](./UI/imgs/1_1.png "Face Detection")
14. ### Face Recognition
   ![alt text](./UI/imgs/2_1.png "Face Recognition")
   
