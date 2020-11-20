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
import string
#reporte simple python page3.py


#
#pytest -v -s --html=report.html --self-contained-html page3.py

#pytest page3.py  page3_2.py  page3_3.py  page3_4.py  page3_5.py  page3_6.py page3_7.py page3_8.py page3_9.py page3_10.py page3_11.py page3_12.py page3_13.py page3_14.py -n 14
#pytest page3.py  page3_2.py  page3_3.py  page3_4.py  page3_5.py -n 5

ren = 4
excel="C://ADEFOC//Documentos//EXCEL_PRUE.xlsx"
casos= 4
#pytest -v -s --alluredir="C:\SISIA\reportes_allure"  page3.py
#allure serve C:\SISIA\reportes_allure


ruta="http://10.16.3.29:8003/login"

#AB20200000044
#RAB20200000017


#cls
class Sisia(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(4)

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
        for r in range(ren, rows):
            user = fe.readData(path, hoja, r, 1)
            passw = fe.readData(path, hoja, r, 2)
            clave = fe.readData(path, hoja, r, 6)
            solicitud=fe.readData(path, hoja, r,8)
            especie=fe.readData(path, hoja, r,9)
            zoo=fe.readData(path, hoja, r,10)




            rf = random.randint(1, 5)
            fecha1 = datetime.now()+ + timedelta(days=rf)
            fecha1 = fecha1.strftime('%d/%m/%Y')

            # Login
            f.scrolling("100")
            f.tiempo(1)
            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary'][contains(.,'Acceder')]")
            f.tiempo(1)
            f.Click("//a[@href='consulta-unidad']")
            f.Click("//a[contains(@id,'unidad')][contains(.,'Registro de solicitud')]")
            f.limpiar("//input[contains(@id,'unidad')]")
            f.tiempo(.5)
            f.texto("//input[contains(@id,'unidad')]", clave)
            f.tiempo(1)
            f.Click("//button[contains(@id,'id_buscar_unidad')]")
            f.tiempo(3)
            f.scrolling(1000)
            f.combo_index("//select[contains(@id,'id_tipo_solicitud')]",solicitud)
            f.tiempo(1)
            f.combo_index("//select[contains(@id,'especie')]",especie)
            f.tiempo(1.5)
            f.combo_index("//select[contains(@id,'id_funcion_zootecnica')]",zoo)
            f.tiempo(1.5)
            f.texto("//input[contains(@id,'fechaInicio')]", fecha1)
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

            #Solicitud
            f.tiempo(2)
            f.Click("//*[@id='subenlaces']/ul/li[2]/a")
            f.Click("//*[@id='id_ir_consulta_solicitud']")
            f.scrolling(600)
            f.tiempo(2)
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
            f.tiempo(10)
            f.scrolling(1000)

            #Vacunación
            path = excel
            hoja = "vacunas"
            renv=1
            rows2 = fe.getRowCount(path, hoja)
            for r in range(renv, rows2 + 1):
                vacuna = fe.readData(path, hoja, r, 1)
                Labora = fe.readData(path, hoja, r, 2)
                lote = fe.readData(path, hoja, r, 3)
                f.tiempo(.3)
                f.combo_index("//select[contains(@id,'vacuna')]",vacuna)
                f.texto("//input[contains(@id,'laboratorio')]",Labora)
                f.texto("//input[contains(@id,'lote')]",lote)
                f.texto("//input[contains(@id,'caducidad')]",fecha1)
                f.Click("//*[@id='id_agregar_vacuna']")
                f.tiempo(.3)



            if(r == casos):
                break











    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Text Completado")



if  __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Resultados Test"))







