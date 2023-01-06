)

# photos = driver.find_elements(By.CLASS_NAME, '_aagw')
# videos = driver.find_elements(By.CLASS_NAME, '_aak1')

like_buttons = []
i = 0
like_button = driver.find_elements(By.CSS_SELECTOR, 'div._ab1_')
like_buttons.append(like_button)