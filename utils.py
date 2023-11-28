def get_data(pixels):
    
    import os
    from PIL import Image
    import numpy as np

    x_train = []
    y_train = []
    path_data = 'data224/train'
    names_files = os.listdir(path_data)
    print('----------Train----------')
    for i,file in enumerate(names_files):
        print(file)
        path_images = 'data224/train/'+file
        names_images = os.listdir(path_images)
        for name in names_images:
            path_image = os.path.join(path_images, name)
            image = Image.open(path_image)
            image = image.resize((pixels,pixels))
            image = image.convert("L")
            x_train.append(np.array(image))
            y_train.append(i)
            
    x_test = []
    y_test = []
    path_data = 'data224/test'
    names_files = os.listdir(path_data)
    print('----------Test----------')
    for i,file in enumerate(names_files):
        print(file)
        path_images = 'data224/test/'+file
        names_images = os.listdir(path_images)
        for name in names_images:
            path_image = os.path.join(path_images, name)
            image = Image.open(path_image)
            image = image.resize((pixels,pixels))
            image = image.convert("L")
            x_test.append(np.array(image))
            y_test.append(int(i))
            
    x_train = np.array(x_train)
    y_train = np.array(y_train)
    x_test = np.array(x_test)
    y_test = np.array(y_test)
    
    return x_train, y_train, x_test, y_test