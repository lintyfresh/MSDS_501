# DO NOT ADD ANY OTHER PACKAGES AND LIBRARIES

def create_image_array(file_name):
    """
    Create a function called create_image_array() which takes
    file_name as an input variable and returns a list
    with the given width and height.
    """

    try: 
        with open(file_name, 'r') as f:
            content = f.read()
            content_list = content.split('\n')

    except FileNotFoundError:
        print("file not found")

    width = int(content_list[0])
    height = int(content_list[1])

    new_content = content_list[2:]
    last_item = new_content.pop()

    new_content_int = list()

    for line in new_content:
        temp_list = list()
        first_int = int(line.split(",")[0])
        second_int = int(line.split(",")[1])
        third_int = int(line.split(",")[2])
        temp_list.append(first_int)
        temp_list.append(second_int)
        temp_list.append(third_int)
        new_content_int.append(temp_list)

    len_list = len(new_content_int) - 1

    image_array = list()

    i = 0
    k = 0

    while i < len_list:
        while k < height:
            j = 0
            temp_list = list()
            while j < width:
                temp_list.append(new_content_int[i])
                i += 1
                j += 1
            image_array.append(temp_list) 
            k += 1

    return image_array

def xray_filter(numbers): 
    """
    Create xray_filter() that takes a list and returns a new list.
    This new list includes updated r,g,b values that
    r_value = 255 - r_value
    g_value = 255 - g_value
    and b_value = 255 – b_value.
    """

    x_ray_image = list()

    for row in numbers:
        temp_list1 = list()
        for pixel in row:
            temp_list2 = list()
            for color in pixel:
                new_color = 255 - color
                temp_list2.append(new_color)
            temp_list1.append(temp_list2)
        x_ray_image.append(temp_list1) 
    return x_ray_image


def adjust_r_g_b(numbers, r_ratio, g_ratio, b_ratio):
    
    """
    Create a function called adjust_r_g_b() that takes the image array and
    three float values that are multiplied to r,g, and b values accordingly.
    The adjusted value should be rounded to an integer.
    """

    red_adjustment = r_ratio
    green_adjustment = g_ratio
    blue_adjustment = b_ratio

    adjusted_image = list()

    for row in numbers:
        temp_list1 = list()
        for pixel in row:
            temp_list2 = list()
            color1 = round(pixel[0] * red_adjustment)
            color2 = round(pixel[1] * green_adjustment)
            color3 = round(pixel[2] * blue_adjustment)
            temp_list2 = [color1, color2, color3]
            temp_list1.append(temp_list2)
        adjusted_image.append(temp_list1)

    return adjusted_image

def upside_down(numbers):

    """
    Create a function called upside_down() that takes a list and
    reverses the list.
    """

    reversed_array = list()

    for row in reversed(numbers):
        reversed_array.append(row)

    return reversed_array

def vertical_flip(numbers):

    """
    Create a function called vertical_flip() that
    takes a list and returns a list
    where values in each row are vertically flipped.
    """

    flipped_array = list()

    for row in numbers:
        new_row = list(reversed(row))
        flipped_array.append(new_row)

    return flipped_array

def create_border(**kwargs):
    """
    Add a border around the images with given
    red, green, blue and pixel values.
    Input parameters are given as arbitary keyword arguments
    including numbers, red, green, blue and pixel.
    "numbers" is a list of pixel values of the input image created
    by create_image_array().
    "red", "green", "blue" are indicating values for rgb values.
    The "pixel" number of [red, green, blue] value should be added
    at the beginning and end of each row.
    In addition, the returned list should have
    the "pixel" number of rows only consists
    with the given red, green, blue at the beginning and end of "numbers".
    """
    array3 = kwargs['numbers']

    border = kwargs['pixel']

    red_value = kwargs['red']
    green_value = kwargs['green']
    blue_value = kwargs['blue']

    border_pixel = [red_value, green_value, blue_value]

    horizontol_border = list()

    for row in array3:
        a=0
        while a < border:
            row.insert(0, border_pixel)
            row.append(border_pixel)
            a += 1

    for i in range(0, len(array3[0])):
        horizontol_border.append(border_pixel)
        i+=1

    #print(horizontol_border)

    for i in range(0, border):
        array3.insert(0, horizontol_border)

    for i in range(0, border):
        array3.append(horizontol_border)

    return array3


