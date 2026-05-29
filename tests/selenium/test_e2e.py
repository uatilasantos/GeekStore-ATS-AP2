from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

from database import get_db_connection


def test_compra_e2e():

    # Garante estoque disponível
    conn = get_db_connection()

    conn.execute(
        """
        UPDATE produtos
        SET estoque = 10
        WHERE nome = 'teclado'
        """
    )

    conn.commit()
    conn.close()

    options = webdriver.ChromeOptions()

    # Executa sem abrir navegador
    options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:

        driver.get("http://127.0.0.1:8000")

        # Produto
        produto = driver.find_element(By.ID, "input-produto")
        produto.send_keys("teclado")

        # Cartão
        cartao = driver.find_element(By.ID, "input-cartao")
        cartao.send_keys("123456789")

        # Cupom
        cupom = driver.find_element(By.ID, "input-cupom")
        cupom.send_keys("GEEK20")

        # Botão
        botao = driver.find_element(By.ID, "btn-comprar")
        botao.click()

        # Aguarda mensagem final
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, "mensagem"),
                "Compra aprovada com sucesso!"
            )
        )

        mensagem = driver.find_element(By.ID, "mensagem")

        texto = mensagem.text

        assert "Compra aprovada com sucesso!" in texto

    finally:

        driver.quit()