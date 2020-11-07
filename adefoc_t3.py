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

ren = 17
excel="C://ADEFOC//Documentos//EXCEL_PRUE.xlsx"
casos= 18
#pytest -v -s --alluredir="C:\SISIA\reportes_allure"  page3.py
#allure serve C:\SISIA\reportes_allure
nf=2
vacunas=10


ruta="http://10.16.3.29:8003/login"
ruta2="http://10.16.3.29:8003/consulta-solicitudes"
#TB20200000025

#cls
class Sisia(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(8)

    # @unittest.skip("Para pruebas de datos")
    # Primero
    def test01_garra(self):
        driver = self.driver
        f = Funciones(driver)
        fe = Funexcel(driver)
        f.tiempo(2)
        driver.get(ruta)

        path = excel
        hoja = "garra"
        rows = fe.getRowCount(path, hoja)
        for r in range(ren, rows):
            user = fe.readData(path, hoja, r, 1)
            passw = fe.readData(path, hoja, r, 2)
            folio = fe.readData(path, hoja, r, 3)
            estado = fe.readData(path, hoja, r, 4)
            municipio = fe.readData(path, hoja, r, 5)
            localidad = fe.readData(path, hoja, r, 6)
            Observacion = fe.readData(path, hoja, r, 7)
            Carro = fe.readData(path, hoja, r, 8)
            Marca = fe.readData(path, hoja, r, 9)
            Placas = fe.readData(path, hoja, r, 10)
            Capacidad = fe.readData(path, hoja, r, 11)
            Flejado = fe.readData(path, hoja, r, 12)
            Producto = fe.readData(path, hoja, r, 13)



            rf = random.randint(1, 5)
            fecha1 = datetime.now()
            fecha1 = datetime.now() + timedelta(days=+2)
            fecha1 = fecha1.strftime('%d/%m/%Y')

            fecha2 = datetime.now()
            fecha2 = datetime.now() + timedelta(days=10)
            fecha2 = fecha2.strftime('%d/%m/%Y')

            # Login
            f.scrolling("100")
            f.tiempo(1)
            f.texto("//input[contains(@id,'username')]", user)
            f.texto("//input[contains(@id,'password')]", passw)
            f.Click("//button[@class='btn btn-primary'][contains(.,'Acceder')]")
            f.tiempo(2)

            #Cargar folio
            f.Click("//a[@href='consulta-unidad']")
            f.tiempo(1)
            f.Click("//a[contains(@id,'solicitud')]")
            f.tiempo(1)
            f.scrolling(200)
            f.limpiar("//input[contains(@id,'id_folio_solicitud')]")
            f.tiempo(1)
            f.texto("//input[contains(@id,'id_folio_solicitud')]",folio)
            f.tiempo(2)
            f.Click("//button[contains(@id,'id_buscar_solicitud')]")
            f.scrolling(300)
            f.tiempo(1.5)
            #Valor de la fecha
            fa=f.obtenerTexto("//*[@id='Registros']/div[1]/div/table/tbody/tr/td[6]")
            fa=fa[:10]
            print(fa)

            f.Click("//button[contains(@id,'id_detalle_solicitud')]")
            f.tiempo(2)
            f.scrolling(500)
            bt=f.existe_try("//button[contains(@id,'id_reactivar_solicitud')]")
            if bt=="Existe":
                #Reactivar boton
                f.Click("//button[contains(@id,'id_reactivar_solicitud')]")
                f.Click("//a[@aria-expanded='false'][contains(.,'Programación de actividades')]")
                f.tiempo(1)
                f.Click("//a[contains(@id,'solicitud')]")
                f.tiempo(1)
                f.scrolling(200)
                f.limpiar("//input[contains(@id,'id_folio_solicitud')]")
                f.tiempo(1)
                f.texto("//input[contains(@id,'id_folio_solicitud')]", folio)
                f.tiempo(2)
                f.Click("//button[contains(@id,'id_buscar_solicitud')]")
                f.scrolling(300)
                f.tiempo(1)
                f.Click("//button[contains(@id,'id_detalle_solicitud')]")
                f.tiempo(2)
                f.scrolling(300)
                #Registrar solicitud
                f.Click("//button[contains(@id,'id_ir_registro_solicitud')]")
                f.tiempo(25)
                driver.implicitly_wait(30)

            elif bt=="Falso":
                f.tiempo(2)
                f.scrolling(300)
                # Registrar solicitud
                f.Click("//button[contains(@id,'id_ir_registro_solicitud')]")
                f.tiempo(25)
                driver.implicitly_wait(30)


            f.scrolling(600)
            f.combo_index("//select[contains(@id,'id_tratamiento')]",1)
            f.tiempo(1.5)
            f.limpiar("//input[contains(@id,'id_estado')]")
            f.texto("//input[contains(@id,'id_estado')]",estado)
            f.limpiar("//input[contains(@id,'id_municipio')]")
            f.texto("//input[contains(@id,'id_municipio')]",municipio)
            f.limpiar("//input[contains(@id,'id_localidad')]")
            f.texto("//input[contains(@id,'id_localidad')]",localidad)
            f.texto("//input[contains(@id,'fechaInicio2')]",fa)
            f.texto("//input[@id='id_observaciones']",Observacion)
            est = random.randint(1, 8)
            f.tiempo(6)
            f.combo_index("//select[contains(@id,'id_estado_destino')]",est)
            f.tiempo(3)
            f.combo_index("//select[contains(@id,'id_municipio_destino')]",est)
            f.tiempo(3)

            #Medio de tranporte
            f.texto("//input[contains(@id,'transporte')]",Carro)
            f.texto("//input[contains(@id,'id_marca')]",Marca)
            f.texto("//input[contains(@id,'id_placas')]",Placas)
            f.texto("//input[contains(@id,'id_capacidad')]",Capacidad)
            f.texto("//input[contains(@id,'id_flejado')]",Flejado)

            #Ruta
            f.combo_index("//select[contains(@id,'id_estado_ruta')]",est)
            f.tiempo(1.5)
            f.combo_index("//select[contains(@id,'id_municipio_ruta')]",est)
            f.texto("//input[contains(@id,'id_detalle_ruta')]",Observacion)
            f.Click("//button[contains(@id,'id_agregar_ruta')]")
            f.tiempo(2)
            f.scrolling(200)

            #Producto Tratamiento
            f.combo_index("//select[contains(@id,'id_familia_producto')]",1)
            f.tiempo(1.5)
            f.texto("//input[contains(@id,'id_nombre_producto')]",Producto)
            f.texto("//input[contains(@id,'id_fecha_caducidad')]",fecha2)
            f.Click("//button[contains(@id,'id_agregar_producto')]")
            f.tiempo(2)
            f.scrolling(350)





            # Tabla tablaGarrapata
            f.tiempo(3)
            driver.implicitly_wait(5)
            tbl5 = f.existe_try_class_name("tablaGarrapata")
            Iden = f.localizar_elemento_css("tablaGarrapata")
            f.tiempo(2)
            print("Tabla tablaGarrapata" + str(tbl5))
            if tbl5 == "Existe":
                tbl5 = f.localizar_elemento("cantidadTable__animales")
                f.scrolling(20)
                tbl5 = f.obtenerTexto_id("cantidadTable__animales")
                # print("Base tabla dos: " +str(tbl2))
                f.tiempo(2)
                tb5 = float(tbl5)
                ttb5 = tb5 / 15
                tb1_t5 = str(ttb5).split(".")
                tb5_entero = int(tb1_t5[0])
                print("Tabla tablaGarrapata: " + str(tb5_entero))

                # segunda tabla
                #for r in range(1, tb5_entero+1):
                for r in range(1, nf):
                    # f.Click("//span[@id='tablaAnimalExtra__1__paginador__span__']"+str(r)+"')]")
                    f.Click("//li[contains(@id,'tablaGarrapata__paginador__page"+str(r)+"')]")
                    f.scrolling(-750)
                    f.tiempo(1)

                    # for ch in range(0,15):
                    Iden = f.localizar_elemento_css("tablaGarrapata")
                    print("identificado" + str(Iden))
                    for ch in range(0, 15):
                        raz = random.randint(1, 6)
                        vacc = random.randint(1, 3)
                        # print("chec: " + str(ch))
                        f.scrolling(50)
                        f.Click("//input[contains(@id,'id_check_tablaGarrapata__"+str(ch)+"')]")
                        f.combo_index("//select[@id='id_raza_tablaGarrapata__"+str(ch)+"']", str(raz))
                        f.combo_index("//select[@id='id_producto_tablaGarrapata__"+str(ch)+"']", 1)



            #Firma
            f.tiempo(2)
            f.Click("//span[contains(.,'Firmar')]")
            f.tiempo(2)
            f.Click("//button[@type='button'][contains(.,'Aceptar')]")
            f.tiempo(2)
            f.Click("//button[@type='button'][contains(.,'Aceptar')]")
            f.tiempo(2)
            f.Click("//a[contains(@id,'dictamen')]")
            f.tiempo(2)
            f.scrolling(200)
            f.texto("//input[contains(@id,'solicitud')]",folio)
            f.tiempo(1)
            f.Click("//button[contains(@id,'dictamen')]")
            f.tiempo(1)
            f.scrolling(200)
            #detalle
            f.Click("//button[@id='id_detalle_dictamen']")
            f.tiempo(3)
            f.scrolling(1200)
            f.Click("//button[contains(@id,'id_descargar_dictamen')]")
            f.tiempo(7)


            #salir
            f.scrolling(-1700)
            f.localizar_elemento_xpath("//a[contains(.,'Salir')]")
            f.tiempo(2)
            f.Click("//a[contains(.,'Salir')]")
            f.tiempo(2)



                #final
                #if (r == casos):
                 #   break



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Text Completado")



if  __name__ == '__main__':
    unittest.main()
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Resultados Test"))







