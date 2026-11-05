from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Firefox()

try:

    driver.get("https://fundacion-instituto-profesional-duoc-uc.github.io/ATY1102-MantenedorUsuarios/index.html")

    usuario = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"username"))
    )
    
    usuario.send_keys("duoc")

    mensaje = driver.find_element(By.ID, "errorMsg").text or "No encontrado"

    driver.find_element(By.ID,"password").send_keys("duoc123")

    driver.find_element(By.ID,"loginForm").submit()

    try:
        nombre = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID,"username"))
        )
        print("Ingreso correcto")

        nombre.send_keys("Juan")

        driver.find_element(By.ID, "nombre").send_keys("Juan")
        driver.find_element(By.ID, "email").send_keys("Juan@prueba.cl")
        driver.find_element(By.ID, "ciudad").send_keys("Valparaiso")

        driver.find_element(By.ID, "dataForm").submit()

        time.sleep(5)
        
    except Exception:
        print("Usuario incorrecto o error al cargar la siguiente página.")
        time.sleep(3)
        input("Presione ENTER para cerrar...")

except NoSuchElementException:   
    print("Elemento no encontrado")
    input("Presione ENTER para cerrar...")

except Exception as e:
    print("Error:", e)
    input("Presione ENTER para cerrar...")
finally:
    driver.quit()
