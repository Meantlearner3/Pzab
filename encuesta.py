import sys #cerrar cuando acaba programa
import cv2 #imagen
import playsound as ps #audio 

pregunta_1 = int (input ("\nTe caigo bien? \n 1- Si \n 2- No\n\n"))

if pregunta_1 == 1:
    print("\nVa, tengo otra pregunta que hacerte...") #si

elif pregunta_1 == 2:
    print("Ok, gracias por tu tiempo :)")#No

    sys.exit() # acabar programa


pregunta_2 = int (input ("\nQué tanto? \n 1- Como amigo \n 2- Más que un amigo\n\n"))
if pregunta_2 == 1: #Friendzoneado
    print("Ta bien, gracias por tu tiempo :)") #Finges no estar aguitado

    sys.exit() #acabar programa


elif pregunta_2 == 2: #sin miedo al exito

    #audio

    ps.playsound("D:\\bryan\\Documents\\Python (Programas)\\Quieres ser mi novia\\mi mayor anhelo.mp3")

#foto
    imagen = cv2.imread("quieres ser mi novia meme.jpg") #buscar direccion del archivo de video

    cv2.imshow("imagen", imagen) #mostrar imagen

    

    cv2.waitKey(0)
    cv2.destroyAllWindows()









    

    
    





