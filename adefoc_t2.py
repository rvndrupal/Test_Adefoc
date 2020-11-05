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

ren = 5
excel="C://ADEFOC//Documentos//EXCEL_PRUE.xlsx"
casos= 1
#pytest -v -s --alluredir="C:\SISIA\reportes_allure"  page3.py
#allure serve C:\SISIA\reportes_allure
nf=2
vacunas=10


ruta="http://10.16.3.29:8003/login"
ruta2="http://10.16.3.29:8003/consulta-solicitudes"
#AB20200000044
#RAB20200000017
#RAB20200000098
#RAB20200000013
#VBR202000000032
#VBR202000000044
#VBR20200000045
#VBR20200000050

#cls
class Sisia(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(8)

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
            fecha1 = datetime.now()
            fecha1 = fecha1.strftime('%d/%m/%Y')

            # Login
            f.scrolling("100")
            f.tiempo(1)
            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary'][contains(.,'Acceder')]")
            f.tiempo(2)



            f.Click("//a[@href='consulta-unidad']")
            f.Click("//a[contains(@id,'unidad')][contains(.,'Registro de solicitud')]")
            f.limpiar("//input[contains(@id,'unidad')]")
            f.tiempo(3)


            f.texto("//input[contains(@id,'unidad')]", clave)
            f.tiempo(1)
            f.Click("//button[contains(@id,'id_buscar_unidad')]")
            f.tiempo(3)
            f.scrolling(1400)
            f.tiempo(2)
            #vs=f.combo_index_existe("//select[contains(@id,'id_tipo_solicitud')]")
            #print(vs)
            f.combo_index("//select[contains(@id,'id_tipo_solicitud')]",solicitud)
            f.tiempo(2)
            f.combo_index("//select[contains(@id,'especie')]",especie)
            f.tiempo(65)
            driver.implicitly_wait(65)
            #f.combo_index("//select[contains(@id,'zootecnica')]",zoo)
            f.combo_index("//*[@id='id_funcion_zootecnica']",zoo)
            f.tiempo(1.5)
            f.texto("//input[contains(@id,'fechaInicio')]", fecha1)
            f.tiempo(1.5)

            driver.implicitly_wait(3)
            f.scrolling(100)
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
            f.tiempo(4)
            clave=f.obtenerTexto("/html/body/app-root/app-consulta-unidad/main/div/app-header/div[2]/div/app-global-alert/div")
            clave=clave[53:]
            print("Clave:"+ str(clave))
            f.tiempo(1)


            # Solicitud
            f.tiempo(1)
            f.Click("//*[@id='subenlaces']/ul/li[2]/a")
            f.Click("//*[@id='id_ir_consulta_solicitud']")
            f.scrolling(900)
            f.tiempo(1)
            f.texto("//input[contains(@id,'solicitud')]",clave)
            #f.texto("//input[contains(@id,'solicitud')]", "VBR20200000075")
            f.tiempo(3)
            f.Click("//span[@class='glyphicon glyphicon-search']")
            f.tiempo(2)

            #ir a detalle
            f.scrolling(100)
            #click detalle
            f.Click("//button[@id='id_detalle_solicitud']")
            f.scrolling(200)
            f.tiempo(2)



            # boton autorizar
            bt = f.existe_try("//*[@id='id_autorizar_solicitud']")
            if bt == "Existe":
                f.Click("//*[@id='id_autorizar_solicitud']")
                f.tiempo(1)
                f.scrolling(150)
                f.Click("//button[contains(@id,'id_ir_registro_solicitud')]")
                f.tiempo(6)
            elif bt == "Falso":
                f.Click("//button[contains(@id,'id_ir_registro_solicitud')]")
                f.tiempo(6)





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
                laboratorio = fe.readData(path, hoja, r, 4)

                f.tiempo(1)
                #f.combo_index("//select[contains(@id,'vacuna')]",vacuna)
                f.combo_index("//select[contains(@id,'vacuna')]",1)
                f.tiempo(1.5)
                f.combo_index("//select[contains(@id,'dosificacion')]",1)
                f.tiempo(.5)
                #f.texto("//input[contains(@id,'laboratorio')]",Labora)
                f.texto("//input[contains(@id,'id_laboratorio')]",laboratorio)
                #f.tiempo(.5)
                f.texto("//input[contains(@id,'lote')]",lote)
                #f.tiempo(.5)
                f.texto("//input[@id='fechaCaducidad']",fecha1)
                #f.tiempo(.5)
                f.Click("//*[@id='id_agregar_vacuna']")
                #f.tiempo(.5)
                if (r == casosv):
                    break



            # Tabla tablaVBrucelosis
            f.scrolling(750)
            f.tiempo(10)
            driver.implicitly_wait(10)
            tbl5 = f.existe_try_class_name("tablaVBrucelosis")
            Iden = f.localizar_elemento_css("tablaVBrucelosis")
            f.tiempo(2)
            print("Tabla Brucelosis" + str(tbl5))
            if tbl5 == "Existe":
                tbl5 = f.localizar_elemento("cantidadTable__animales")
                tbl5 = f.obtenerTexto_id("cantidadTable__animales")
                # print("Base tabla dos: " +str(tbl2))
                f.tiempo(2)
                tb5 = float(tbl5)
                ttb5 = tb5 / 15
                tb1_t5 = str(ttb5).split(".")
                tb5_entero = int(tb1_t5[0])
                print("Tabla Brucelosis: " + str(tb5_entero))

                # segunda tabla
                # for r in range(1, tb4_entero+1):
                for r in range(1, nf):
                    # f.Click("//span[@id='tablaAnimalExtra__1__paginador__span__']"+str(r)+"')]")
                    f.Click("//*[@id='tablaVBrucelosis__paginador__page"+str(r)+"']")
                    f.scrolling(-750)
                    f.tiempo(1)

                    # for ch in range(0,15):
                    Iden = f.localizar_elemento_css("tablaVBrucelosis")
                    print("identificado" + str(Iden))
                    for ch in range(0, 15):
                        raz = random.randint(1, 6)
                        vacc = random.randint(1, 8)
                        # print("chec: " + str(ch))
                        f.scrolling(30)
                        f.Click("//input[@id='tablaVBrucelosis__check__"+str(ch)+"']")
                        f.combo_index("//select[@id='tablaVBrucelosis__raza__"+str(ch)+"']", str(raz))
                        f.combo_index("//select[@id='tablaVBrucelosis__vacuna__"+str(ch)+"']", str(vacc))





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







