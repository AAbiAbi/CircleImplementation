from PIL import Image, ImageDraw

## create a circle given radius and color
def create_circle_edge(img, center,radius, color):
    pixels = img.load();

    center_x = center[0]
    center_y = center[1]
    # Draw the circle
    x = 0;
    # 0
    y = radius;
    # R
#midpoint:
    ##noted : remember to transfer all pixels into actural location
    pixels[x + center_x ,y + center_y] = color #(0,R)

    pixels[x + center_x- radius ,y + center_y - radius] = color # (-R,0)

    pixels[x + center_x + radius,y + center_y - radius] = color # (R, 0)
    pixels[x + center_x,y + center_y - 2*radius] = color #(0, -R)
    

    fm = 1.25 - radius;#step 2

    
    while(x < y):
        #step3
        if(fm < 0):
            fm = fm + 2*x + 3;
            
        else: 
            fm = fm + 2*x -2*y + 5
            y = y - 1;
        
        x = x + 1
        #plot(x,y) and 7 other pixels
        pixels[x + center_x,y + center_y ] = color
        pixels[-x + center_x, y + center_y] = color
        pixels[x + center_x, -y + center_y] = color
        pixels[-x + center_x, -y + center_y] = color
        pixels[y + center_x, x + center_y] = color
        pixels[-y + center_x, x + center_y] = color
        pixels[y + center_x, -x + center_y] = color
        pixels[-y + center_x, -x + center_y] = color
        

    return img


def area_fill(img, color):
    # scan line moving from bottom to top
    for y in range(img.height):
        #for every pixel line, a unique intersection list
        intersection = []
        #due to convex character, no need to seperate intersection list and make pairs
    
        for x in range(img.width):
            #find all intersection points, added to intersection list
            if(img.getpixel((x,y)) == color):
                intersection.append(x)
        #sort in ascending order
        intersection.sort()

       
        if len(intersection) > 0 :
             #fulfill the interval line
            for i in range(intersection[0], intersection[len(intersection) - 1]):
                img.putpixel((i,y),color)
    
    return img


# calculate the area of the overlapped area of pixel with line
#Assuming the actual line has width of 1 pixel. Each pixel is a square
#The color value of the pixel will be proportional to the percentage of the overlap.
def anti_aliasing(img,center, radius,color):
    for y in range(img.height):
        for x in range(img.width):
            math_distance = ((x - center[0])**2 + (y - center[1])**2 ) ** 0.5

            overlap = radius - math_distance 

            if -1  < overlap < 1 :
                #get the boundary
                original_color = img.getpixel((x,y))

                blend_factor = max(0, 1 - abs(overlap))

                new_color = tuple(
                    int(c * blend_factor + original_c * (1 - blend_factor))
                    for c, original_c in zip(color, original_color)
                    #This loop iterates over each pair of color components.
                )
                img.putpixel((x,y), new_color)
    return img