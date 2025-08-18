# DO NOT ADD ANY OTHER PACKAGES AND LIBRARIES

def create_image_array(file_name):

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

    reversed_array = list()

    for row in reversed(numbers):
        reversed_array.append(row)

    return reversed_array

def vertical_flip(numbers):

    flipped_array = list()

    for row in numbers:
        new_row = list(reversed(row))
        flipped_array.append(new_row)

    return flipped_array

def create_border(**kwargs):
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


