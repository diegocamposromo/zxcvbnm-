import cv2

# Ruta de la imagen
ruta_imagen = 'dtygghghu.jpg'

# Carga la imagen
imagen = cv2.imread(ruta_imagen)

# Verifica que la imagen se ha cargado correctamente
if imagen is not None:
    # Muestra la imagen
    cv2.imshow('Imagen', imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('No se pudo cargar la imagen')