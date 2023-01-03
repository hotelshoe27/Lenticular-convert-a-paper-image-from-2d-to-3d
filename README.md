# Lenticular-convert-a-paper-image-from-2d-to-3d
**This simple project makes lenticular image**  
- We can feel three-dimensional in 2D lenticular image by Binocular parallax. (skip the detailed theory😅)  
- So this project makes lenticular image for feeling three-dimensional in 2D image, also make a 'Simple lenticular image' that looks different depending on the direction you see it.
- **'Simple lenticular image'** can be printed and used immediately, but **'Real lenticular image'** requires the actual lenticular lens.
- Only two images can be used for this version, so you have to use only two images👀

---

### 1_resized images  

In order to make a 'lenticular image', the two images must be the same size.  
So check each two image's size(pixel) and Make both images the same size using 'img_resize.py'.

---

### 2_divide image  
![123](https://user-images.githubusercontent.com/120359150/209760591-a6efdcbc-6114-48c5-b334-0658f625c3d9.PNG)  
1. Select two images for making lenticular  
2. (Option)Select save path. The default save path is specified as the 'complete' folder, but you can replace it if you want.  
3. Insert number of piece for dividing. If you want to make a 'simple lenticular image', Number of piece is between 5 and 10 seems reasonable.  
But If you want to make 'Real lenticular image', you have to check your lenticular lenses Lpi(Lens per inch) and calculate lenses array interval(See this picture  below).  
![1111](https://user-images.githubusercontent.com/120359150/209764567-84377226-acb4-41a8-8602-c0a2452f6218.jpg)  

And divide the images according to array interval size calculated. In my case, I used lens of 40Lpi and used 'img_0.jpg' divided 512 pieces.

---

### 3_Print lenticular image  
#### a. Simple lenticular image  
1) Use 'sample_0.jpg' and 'sample_1.jpg' in 'data' folder. Before work this task, you have to fit two images size.  
![resized_img_0](https://user-images.githubusercontent.com/120359150/209765313-541c5003-cc0b-4176-bc92-0cacbf798f85.png) ![sample_1](https://user-images.githubusercontent.com/120359150/209765320-e63af89e-0ebd-4195-8c9b-45102cbc0111.jpg)  
2) Check the result in 'complete' folder  
![lenticularImg_sample](https://user-images.githubusercontent.com/120359150/209764460-878743d3-4077-45c7-a651-42f31413b924.png)  

3) Print the result and fold the paper along the divided lines.  
![resized_1_0](https://user-images.githubusercontent.com/120359150/209764052-26ceb943-e675-4bb8-8ca1-de9fa1fb2b17.png) ![resized_2_0](https://user-images.githubusercontent.com/120359150/209764083-4a7519eb-a63b-4061-906e-81e5b4aca4f9.png)  
Enjoy this show🤣🤣  

#### b. Real lenticular image  
1) Use 'img_0.jpg' and 'img_1.jpg' in 'data' folder.  
![img_0](https://user-images.githubusercontent.com/120359150/209765572-1c5756e5-9821-4658-85ea-87946bb58a73.jpg) ![img_1](https://user-images.githubusercontent.com/120359150/209765576-71c5dd5c-6bb8-4870-82b1-aacbed4f6626.jpg)  

2) Check the result in 'complete' folder  
![lenticularImg](https://user-images.githubusercontent.com/120359150/209764868-26cc0d7c-e22f-4f97-a173-6836db6e1613.png)  

3) Print the result and Please put a lenticular lens over the result image. In my case, I used lens of 40Lpi and used 'img_0.jpg' divided 512 pieces.  
![다운로드](https://user-images.githubusercontent.com/120359150/209765820-2863a9f9-0d6c-445d-ad85-356f7cbf6fb9.jpg)  

Enjoy feeling 3-D👀👀
