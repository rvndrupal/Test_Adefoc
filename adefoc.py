#import HtmlTestRunner
#from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from funciones import *
from excel import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from datetime import timedelta
from selenium.webdriver.common.action_chains import ActionChains
import string
#reporte simple python page3.py


#
#pytest -v -s --html=report.html --self-contained-html adefoc.py

#pytest page3.py  page3_2.py  page3_3.py  page3_4.py  page3_5.py  page3_6.py page3_7.py page3_8.py page3_9.py page3_10.py page3_11.py page3_12.py page3_13.py page3_14.py -n 14
#pytest page3.py  page3_2.py  page3_3.py  page3_4.py  page3_5.py -n 5

ren = 4
excel="C://ADEFOC//Documentos//EXCEL_PRUE.xlsx"
casos= 1
#pytest -v -s --alluredir="C:\SISIA\reportes_allure"  page3.py
#allure serve C:\SISIA\reportes_allure
nf=3
vacunas=25


ruta="http://10.16.3.29:8003/login"

#AB20200000044
#RAB20200000017
#RAB20200000098
#RAB20200000013
#RAB20200000039


#cls
class Sisia(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(40)

    # @unittest.skip("Para pruebas de datos")
    # Primero
    def test01_registro(self):
        driver = self.driver
        f = Funciones(driver)
        fe = Funexcel(driver)
        f.tiempo(2)
        driver.get(ruta)

        path = excel
        hoja = "registro"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows + 1):
            user = fe.readData(path, hoja, r, 1)
            passw = fe.readData(path, hoja, r, 2)
            clave = fe.readData(path, hoja, r, 6)
            solicitud=fe.readData(path, hoja, r,8)
            especie=fe.readData(path, hoja, r,9)
            zoo=fe.readData(path, hoja, r,10)




            rf = random.randint(1, 5)
            fecha1 = datetime.now()+timedelta(days=rf)
            fecha1 = fecha1.strftime('%d/%m/%Y')

            # Login
            f.scrolling("100")
            f.tiempo(1)
            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary'][contains(.,'Acceder')]")
            f.tiempo(4)

            f.Click("//a[@href='consulta-unidad']")
            f.Click("//a[contains(@id,'unidad')][contains(.,'Registro de solicitud')]")
            f.limpiar("//input[contains(@id,'unidad')]")
            f.tiempo(3)




            #seleccionar clase de vacuna

            f.texto("//input[contains(@id,'unidad')]", clave)
            f.tiempo(1)
            f.Click("//button[contains(@id,'id_buscar_unidad')]")
            f.tiempo(3)
            f.scrolling(1400)
            f.tiempo(2)
            #vs=f.combo_index_existe("//select[contains(@id,'id_tipo_solicitud')]")
            #print(vs)
            f.combo_index("//select[contains(@id,'id_tipo_solicitud')]",solicitud)
            f.tiempo(6)
            f.combo_index("//select[contains(@id,'especie')]",especie)
            f.tiempo(4)
            driver.implicitly_wait(10)
            f.combo_index("//select[contains(@id,'zootecnica')]",zoo)
            f.tiempo(1.5)
            f.texto("//input[contains(@id,'fechaInicio')]", fecha1)
            f.tiempo(1.5)

            numa = f.obtenerTexto("//label[contains(@class,'control-label numero')]")
            numa=numa[3:]
            print("Numero de  animales"+ str(numa))
            f.limpiar("//input[contains(@id,'id_numero_animales')]")
            f.tiempo(.5)
            f.texto("//input[contains(@id,'id_numero_animales')]",numa)
            f.tiempo(1)
            f.Click("//input[@id='id_datos_correctos']")
            f.tiempo(.5)
            f.Click("//button[contains(@id,'solicitud')]")
            f.tiempo(1)
            f.Click("//button[@type='button'][contains(.,'Aceptar')]")
            f.scrolling(-1200)
            f.tiempo(2)
            clave=f.obtenerTexto("/html/body/app-root/app-consulta-unidad/main/div/app-header/div[2]/div/app-global-alert/div")
            clave=clave[53:]
            print("Clave:"+ str(clave))
            f.tiempo(5)
            





            #Solicitud
            f.Click("//*[@id='subenlaces']/ul/li[2]/a")      #se activa para directo programacion de actividades
            f.tiempo(5)
            f.Click("//a[contains(@id,'solicitud')][contains(.,'Mis solicitudes')]")
            f.scrolling(600)
            f.tiempo(2)
            #f.texto("//input[contains(@id,'solicitud')]",clave)
            f.texto("//input[contains(@id,'solicitud')]",clave)
            f.tiempo(2)
            f.scrolling(130)
            f.Click("//button[@id='id_buscar_solicitud']")
            f.tiempo(2)
            f.scrolling(190)
            f.tiempo(2)
            f.Click("//*[@id='id_detalle_solicitud']")
            f.scrolling(450)
            f.tiempo(2)
            f.Click("//button[contains(@id,'id_ir_registro_solicitud')]")
            driver.implicitly_wait(20)
            f.scrolling(1000)
            f.tiempo(5)

            #Vacunación
            path = excel
            hoja = "vacunas"
            renv=1
            casosv=vacunas
            rows2 = fe.getRowCount(path, hoja)
            for r in range(renv, rows2 + 1):
                vacuna = fe.readData(path, hoja, r, 1)
                Labora = fe.readData(path, hoja, r, 2)
                lote = fe.readData(path, hoja, r, 3)
                f.tiempo(.1)
                f.combo_index("//select[contains(@id,'vacuna')]",vacuna)
                f.texto("//input[contains(@id,'laboratorio')]",Labora)
                f.texto("//input[contains(@id,'lote')]",lote)
                f.texto("//input[contains(@id,'caducidad')]",fecha1)
                f.Click("//*[@id='id_agregar_vacuna']")
                f.tiempo(.1)
                if (r == casosv):
                    break
            f.scrolling(450)
            f.tiempo(2)
            #Alta de las Especies
            ves=f.combo_index_Ok("//select[contains(@id,'especie')]")
            print("Especies Registradas: " +str(ves))
            for esp  in range(1,ves):
                print("Veces: "+ str(esp))
                if esp == 1:
                    f.combo_index("//select[contains(@id,'especie')]",1)
                    f.tiempo(.5)
                    f.Click("//*[@id='id_agregar_especie']")
                    driver.implicitly_wait(11)
                    f.tiempo(11)
                elif esp == 2:
                    f.combo_index("//select[contains(@id,'especie')]", 1)
                    f.tiempo(.5)
                    f.Click("//*[@id='id_agregar_especie']")
                    driver.implicitly_wait(25)
                    f.tiempo(25)
                else:
                    f.combo_index("//select[contains(@id,'especie')]", 1)
                    f.tiempo(.5)
                    f.Click("//*[@id='id_agregar_especie']")
                    driver.implicitly_wait(25)
                    f.tiempo(25)


            #Tablas
            tbl2=f.existe_try_class_name("tablaAntirrabica")
            tbl1 =f.localizar_elemento("cantidadTable__animales")
            f.tiempo(1)
            tb1=f.obtenerTexto_id("cantidadTable__animales")
            tb1=float(tb1)
            ttb1=tb1/15
            tb1_t=str(ttb1).split(".")
            tb1_entero=int(tb1_t[0])
            #print("Entero: "+ str(tb1_entero))
            #print("Tabla: "+ str(tb1))

            #for r in range(1, tb1_entero+1):
            for r in range(1, nf):
                f.Click("//span[@id='tablaAntirrabica__paginador__span__"+str(r)+"']")
                f.scrolling(-410)
                f.tiempo(1)

                #for ch in range(0,15):
                Iden = f.localizar_elemento_css("tablaAntirrabica")
                for ch in range(0, 15):
                    raz = random.randint(1, 6)
                    vacc = random.randint(1, 8)
                    #print("chec: "+str(ch))
                    f.scrolling(30)
                    f.Click("//input[@id='id_check_tablaAntirrabica__"+str(ch)+"']")
                    f.combo_index("//select[@id='id_raza_tablaAntirrabica__"+str(ch)+"']",str(raz))
                    f.combo_index("//select[@id='id_vacuna_tablaAntirrabica__"+str(ch)+"']",str(vacc))




            #Tabla 2
            f.scrolling(750)
            tbl2=f.existe_try_class_name("tabla_BOVINO")
            if tbl2 == "Existe":
                tbl2 = f.localizar_elemento("cantidadTable__BOVINO")
                tbl2 = f.obtenerTexto_id("cantidadTable__BOVINO")
                #print("Base tabla dos: " +str(tbl2))
                f.tiempo(2)
                tb2 = float(tbl2)
                ttb2 = tb2 / 15
                tb1_t2 = str(ttb2).split(".")
                tb2_entero = int(tb1_t2[0])
                #print("Tabla dos entero: " +str(tb2_entero))

                #segunda tabla
                #for r in range(1, tb2_entero+1):
                for r in range(1, nf):
                    f.Click("//span[contains(@id,'tablaAnimalExtra__0__paginador__span__" + str(r) + "')]")
                    f.scrolling(-420)
                    f.tiempo(1)

                    # for ch in range(0,15):
                    Iden = f.localizar_elemento_css("tabla_BOVINO")
                    for ch in range(0, 15):
                        raz = random.randint(1, 6)
                        vacc = random.randint(1, 8)
                        #print("chec: " + str(ch))
                        f.scrolling(30)
                        f.Click("//input[@id='id_check_BOVINO__"+str(ch)+"']")
                        f.combo_index("//select[@id='id_raza_BOVINO__"+ str(ch) +"']", str(raz))
                        f.combo_index("//select[@id='id_vacuna_BOVINO__"+str(ch)+"']", str(vacc))




            # Tabla 3
            f.scrolling(750)
            tbl3 = f.existe_try_class_name("tabla_OVINO")
            if tbl3 == "Existe":
                tbl3 = f.localizar_elemento("cantidadTable__OVINO")
                tbl3 = f.obtenerTexto_id("cantidadTable__OVINO")
                #print("Base tabla tres: " + str(tbl3))
                f.tiempo(2)
                tb3 = float(tbl3)
                ttb3 = tb3 / 15
                tb1_t3 = str(ttb3).split(".")
                tb3_entero = int(tb1_t3[0])
                #print("Tabla tres entero: " + str(tb3_entero))

                # Tercera tabla
                # for r in range(1, tb3_entero+1):
                for r in range(1, nf):
                    f.Click("//span[contains(@id,'tablaAnimalExtra__1__paginador__span__" + str(r) + "')]")
                    f.scrolling(-500)
                    f.tiempo(1)

                    # for ch in range(0,15):
                    Iden = f.localizar_elemento_css("tabla_OVINO")
                    for ch in range(0, 15):
                        raz = random.randint(1, 6)
                        vacc = random.randint(1, 8)
                        #print("chec: " + str(ch))
                        f.Click("//input[@id='id_check_OVINO__"+str(ch)+"']")
                        f.scrolling(30)
                        f.combo_index("//select[@id='id_raza_OVINO__" + str(ch) + "']", str(raz))
                        f.combo_index("//select[@id='id_vacuna_OVINO__" + str(ch) + "']", str(vacc))


            '''
            # Tabla tablaCAPRINO
            f.scrolling(750)
            f.tiempo(1)
            tbl4 = f.existe_try_class_name("tablaCAPRINO")

            f.tiempo(2)
            print("Tabla caprino" +str(tbl4))
            if tbl4 == "Existe":
                tbl4 = f.localizar_elemento("cantidadTable__CAPRINO")
                tbl4 = f.obtenerTexto_id("cantidadTable__CAPRINO")
                #Iden = f.localizar_elemento_css("tablaCAPRINO")
                # print("Base tabla dos: " +str(tbl2))
                f.tiempo(2)
                tb4 = float(tbl4)
                ttb4 = tb4 / 15
                tb1_t4 = str(ttb4).split(".")
                tb4_entero = int(tb1_t4[0])
                print("Tabla dos entero: " +str(tb4_entero))

                # TABLA CAPRINO
                # for r in range(1, tb4_entero+1):
                for r in range(1, nf):
                    #f.Click("//span[@id='tablaAnimalExtra__1__paginador__span__']"+ str(r)+"')]")
                    f.Click(" // *[ @ id = 'tablaAnimalExtra__1__paginador__span__"+ str(r)+"']")
                    f.scrolling(-800)
                    f.tiempo(1)

                    # for ch in range(0,15):
                    #Iden = f.localizar_elemento_css("tablaCAPRINO")
                    #tbl4 = f.localizar_elemento_css("tablaCAPRINO")
                    #print("identificado"+ str(tbl4))
                    for ch in range(0, 15):
                        raz = random.randint(1, 6)
                        vacc = random.randint(1, 8)
                        # print("chec: " + str(ch))
                        f.scrolling(30)
                        f.tiempo(10)
                        f.Click("//input[contains(@id,'tablaAnimalExtra__0__check__"+str(ch)+"')]")
                        f.combo_index("//select[@id='id_raza_CAPRINO__"+str(ch)+"']", str(raz))
                        f.combo_index("//select[@id='id_vacuna_CAPRINO__"+str(ch)+"']", str(vacc))
            '''



            #Nuevos Registros
            reg=f.localizar_elemento_xpath("//label[contains(.,'Registrar animales adicionales')]")
            f.scrolling(30)
            f.tiempo(2)
            f.Click("//label[contains(.,'Registrar animales adicionales')]")
            f.scrolling(150)
            f.texto("//input[@id='id_adefoc_animal_nuevo']","Nuevo uno")
            f.tiempo(.6)
            f.combo_index("//select[@id='id_especie_animal_nuevo']",1)
            f.tiempo(.6)
            f.texto("//input[@id='id_edad_animal_nuevo']",3)
            f.tiempo(.6)
            f.combo_index("//select[@id='id_raza_animal_nuevo']",3)
            f.tiempo(.6)
            f.combo_index("//select[@id='id_sexo_animal_nuevo']",1)
            f.tiempo(.6)
            f.texto("//input[contains(@id,'patente')]","Patenete nueva")
            f.tiempo(.6)
            f.Click("//button[contains(.,'Agregar datos')]")
            f.scrolling(-150)
            f.tiempo(1)
            f.texto("//input[@id='id_adefoc_animal_nuevo']", "Nuevo dos")
            f.tiempo(.6)
            f.combo_index("//select[@id='id_especie_animal_nuevo']", 1)
            f.tiempo(.6)
            f.texto("//input[@id='id_edad_animal_nuevo']", 4)
            f.tiempo(.6)
            f.combo_index("//select[@id='id_raza_animal_nuevo']", 2)
            f.tiempo(.6)
            f.combo_index("//select[@id='id_sexo_animal_nuevo']", 2)
            f.tiempo(.6)
            f.texto("//input[contains(@id,'patente')]", "Patenete nueva dos")
            f.tiempo(.6)
            f.Click("//button[contains(.,'Agregar datos')]")
            f.tiempo(1)
            f.scrolling(300)
            f.tiempo(1)
            f.combo_index("//select[@id='id_vacuna_animalExtra_0']",1)
            f.tiempo(.6)
            f.combo_index("//select[@id='id_vacuna_animalExtra_1']",2)
            f.tiempo(4)

            #final
            if (r == casos):
                break



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Text Completado")



if  __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Resultados Test"))







