import numpy as np
from PIL import Image as Img

class Image():
    def __init__(self, file_name):
        self.file_name = file_name
    
    def return_image_array(self):
        with open(self.file_name, 'r') as f:
            content = f.read()
            content_list = content.split('\n')
        
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
    
    def create_image_np_array(self):
        numpy_array = np.array(self.return_image_array())
        self.numpy_array = numpy_array
        return self.numpy_array
    
    def check_image_np_array_shape(self):
        if "numpy_array" not in self.__dict__:
            self.create_image_np_array()
            self.shape = self.numpy_array.shape
            return self.shape
        else:
            self.shape = self.numpy_array.shape
            return self.shape

    def save_image_file(self):

        file_path_parts = list(self.file_name.split("/"))
        last_item = file_path_parts.pop()
        file_path = ""
        for path in file_path_parts:
            file_path = file_path + path + "/"
            
        file_path = file_path + "image.sgi"
        
        if "numpy_array" not in self.__dict__:
            self.create_image_np_array()
            pil_image = Img.fromarray(self.numpy_array.astype(np.uint8))
            pil_image.save(file_path)
        else:
            pil_image =Img.fromarray(self.numpy_array.astype(np.uint8))
            pil_image.save(file_path)

    def create_upside_down_image_np_array(self):
        if "numpy_array" not in self.__dict__:
            self.create_image_np_array()
            self.upside_down_array = np.flip(self.numpy_array, axis = 0)
        else:
            self.upside_down_array = np.flip(self.numpy_array, axis = 0)

        return self.upside_down_array
    
    def save_upside_down_image_file(self):

        file_path_parts = list(self.file_name.split("/"))
        last_item = file_path_parts.pop()
        file_path = ""
        for path in file_path_parts:
            file_path = file_path + path + "/"
            
        file_path = file_path + "upside_down_image.sgi"

        if "upside_down_array" not in self.__dict__:
            self.create_upside_down_image_np_array()
            pil_image = Img.fromarray(self.upside_down_array.astype(np.uint8))
            pil_image.save(file_path)
        else :
            pil_image = Img.fromarray(self.upside_down_array.astype(np.uint8))
            pil_image.save(file_path)

    def create_xray_filter_np_array(self):
        if "numpy_array" not in self.__dict__:
            self.create_image_np_array()
    
        x_ray_image = list()

        for row in self.numpy_array:
            temp_list1 = list()
            for pixel in row:
                temp_list2 = list()
                for color in pixel:
                    new_color = 255 - color
                    temp_list2.append(new_color)
                temp_list1.append(temp_list2)
            x_ray_image.append(temp_list1)

        self.x_ray_numpy_array = np.array(x_ray_image)
    
        return self.x_ray_numpy_array
    
    def save_xray_filter_file(self):
        if "x_ray_numpy_array" not in self.__dict__:
            self.create_xray_filter_np_array()
        
        file_path_parts = list(self.file_name.split("/"))
        last_item = file_path_parts.pop()
        file_path = ""
        for path in file_path_parts:
            file_path = file_path + path + "/"
            
        file_path = file_path + "xray_filter_image.sgi"

        pil_image = Img.fromarray(self.x_ray_numpy_array.astype(np.uint8))
        pil_image.save(file_path)

    def create_border_np_array(self, r=0, g=0, b=0, pixel = 1):
        if "numpy_array" not in self.__dict__:
            self.create_image_np_array()
        
        self.r = r
        self.g = g
        self.b = b
        self.pixel = pixel

        border_pixel = [self.r, self.g, self.b]

        horizontol_border = list()

        array_list = self.numpy_array.tolist()

        for row in array_list:
            a=0
            while a < self.pixel:
                row.insert(0, border_pixel)
                row.append(border_pixel)
                a += 1

        for i in range(0, len(array_list[0])):
            horizontol_border.append(border_pixel)
            i+=1

        for i in range(0, self.pixel):
            array_list.insert(0, horizontol_border)

        for i in range(0, self.pixel):
            array_list.append(horizontol_border)
        
        self.numpy_array_border = np.array(array_list)

        return self.numpy_array_border

    def save_border_file(self):
        if "numpy_array_border" not in self.__dict__:
            self.create_border_numpy_array()
        
        file_path_parts = list(self.file_name.split("/"))
        last_item = file_path_parts.pop()
        file_path = ""
        for path in file_path_parts:
            file_path = file_path + path + "/"
            
        file_path = file_path + "border_image.sgi"

        pil_image = Img.fromarray(self.numpy_array_border.astype(np.uint8))
        pil_image.save(file_path)

    def create_r_g_b_np_array(self):
        
        if "numpy_array" not in self.__dict__:
            self.create_image_np_array()
        
        array_list = self.numpy_array.tolist()

        red_list = list()
        green_list = list()
        blue_list = list()

        for row in array_list:

            red_row = list()
            green_row = list()
            blue_row = list()

            for pixel in row:
        
                red = pixel[0]
                green = pixel[1]
                blue = pixel[2]

                temp_list_red = [red, 0, 0]
                temp_list_green = [0, green, 0]
                temp_list_blue = [0, 0, blue]

                red_row.append(temp_list_red)
                green_row.append(temp_list_green)
                blue_row.append(temp_list_blue)

            red_list.append(red_row)
            green_list.append(green_row)
            blue_list.append(blue_row)
        
        self.red_np_array= np.array(red_list)
        self.green_np_array = np.array(green_list)
        self.blue_np_array = np.array(blue_list)

        return (self.red_np_array, self.green_np_array, self.blue_np_array)

    def save_r_g_b_file(self):
        if "red_np_array" not in self.__dict__:
            self.create_r_g_b_np_array()
        elif "green_np_array" not in self.__dict__:
            self.create_r_g_b_np_array()
        elif "blue_np_array" not in self.__dict__:
            self.create_r_g_b_np_array()
        else:
            pass
        
        file_path_parts = list(self.file_name.split("/"))
        last_item = file_path_parts.pop()
        file_path = ""
        for path in file_path_parts:
            file_path = file_path + path + "/"
            
        file_path_red = file_path + "r_image.sgi"
        file_path_green = file_path + "g_image.sgi"
        file_path_blue = file_path + "b_image.sgi"

        red_img = Img.fromarray(self.red_np_array.astype(np.uint8))
        red_img.save(file_path_red)
        
        green_img = Img.fromarray(self.green_np_array.astype(np.uint8))
        green_img.save(file_path_green)

        blue_img = Img.fromarray(self.blue_np_array.astype(np.uint8))
        blue_img.save(file_path_blue)