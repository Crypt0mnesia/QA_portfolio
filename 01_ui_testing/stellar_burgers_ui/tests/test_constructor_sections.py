import pytest
from selenium.webdriver.support import expected_conditions as EC

from data import TextMessages
from urls import MAIN
from locators import ConstructorLocators



class TestConstructorSections:
    """Тесты разделов конструктора"""

    @pytest.mark.parametrize("target_section,expected_text", [
        (ConstructorLocators.BUNS_SECTION, TextMessages.BUNS),
        (ConstructorLocators.SAUCES_SECTION, TextMessages.SAUCES),
        (ConstructorLocators.FILLINGS_SECTION, TextMessages.FILLINGS)
    ])

    def test_switch_to_section(self, driver, wait, target_section, expected_text):
        """Параметризованный тест перехода к разделам конструктора"""
        driver.get(MAIN)

        sauces_element = wait.until(EC.element_to_be_clickable(ConstructorLocators.SAUCES_SECTION))
        driver.execute_script("arguments[0].click();", sauces_element)

        target_element = wait.until(EC.element_to_be_clickable(target_section))
        driver.execute_script("arguments[0].click();", target_element)

        active_section = wait.until(EC.presence_of_element_located(ConstructorLocators.ACTIVE_SECTION))
        assert expected_text in active_section.text
