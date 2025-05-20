import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def scrape_and_store():
    # Configurar Selenium para evitar detección
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # Inicializar navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', { get: () => undefined })"
    })

    try:
        url = "https://listado.mercadolibre.com.co/all-in-one#D[A:ALL%20IN%20ONE]"
        driver.get(url)
        time.sleep(6)  # Esperar que cargue

        # Conectar a la base de datos SQLite
        conn = sqlite3.connect("mercadolibre.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                precio TEXT,
                link TEXT
            )
        """)

        # Limpiar tabla antes de insertar
        cursor.execute("DELETE FROM productos")

        productos = driver.find_elements(By.CLASS_NAME, "ui-search-layout__item")
        contador = 0

        for producto in productos[:50]:
            try:
                enlace_elemento = producto.find_element(By.CLASS_NAME, "poly-component__title")
                nombre = enlace_elemento.text.strip()
                link = enlace_elemento.get_attribute("href")
            except:
                nombre = "No disponible"
                link = "No disponible"

            try:
                precio = producto.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text.strip()
            except:
                precio = "No disponible"

            cursor.execute("INSERT INTO productos (nombre, precio, link) VALUES (?, ?, ?)", (nombre, precio, link))
            contador += 1

        conn.commit()
    finally:
        conn.close()
        driver.quit()

    # Puedes dejar esto para debug local, pero en producción es mejor no imprimir
    print(f"✅ Se han almacenado {contador} productos correctamente.")

if __name__ == "__main__":
    scrape_and_store()
