from requests import get

product_code = input("Enter product code: ")
print(product_code)

url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
print(url)

response = get(url)
print(response.status_code)