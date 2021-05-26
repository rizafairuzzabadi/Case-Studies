import requests
from bs4 import BeautifulSoup

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    URL = "https://www.bosch-home.com.tr/urun-listesi/buzdolaplari-derin-dondurucular/buzdolaplari/alttan-donduruculu-buzdolaplari"
    # Above does not work since the website disallows scraping. Error Message -> Dear
    # User, your request has been rated as suspicious by our firewall and therefore got blocked
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())

    # scrap product name, product code, and score of the refrigerator products
    pr_name = []
    pr_code = []
    pr_score = []

    product_div = soup.find_all('div', class_='item') 
    # iterate through every div container we stored in move_div
    for container in product_div:
        pr_series = container.find('div', class_='product-info js-product-info-wrapper').find('div', class_='m-producttitle').a.h2.find('span', class_='fragment normal std-header-1').text
        pr_tur = container.find('div', class_='product-info js-product-info-wrapper').find('div', class_='m-producttitle').a.h2.find('span', class_='fragment normal std-header-2').text
        pr_boy = container.find('div', class_='product-info js-product-info-wrapper').find('div', class_='m-producttitle').a.h2.find('span', class_='fragment normal std-header-3').text
        pr_tip = container.find('div', class_='product-info js-product-info-wrapper').find('div', class_='m-producttitle').a.h2.find('span', class_='fragment normal std-header-4').text
        product = pr_series + pr_tur + pr_boy + pr_tip
        pr_name.append(product)

        # code
        the_code = container.find('div', class_='product-info js-product-info-wrapper').find('div', class_='m-producttitle').h2.span.text
        pr_code.append(the_code)

        # score
        score_loc = container.find('div', class_='product-conversion').find('div', class_='m-productconversionarea').find('div', class_='js-conversion-wrapper').find('div', class_='a-rating rating').find('span', class_='text number').text
        pr_score.append(score_loc)

    print(pr_name)
    print(pr_code)
    print(pr_score)
