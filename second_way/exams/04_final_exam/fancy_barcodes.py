import re

pattern = r"@#{1,}([A-Z][A-Za-z0-9]{4,}[A-Z])@#{1,}"

for _ in range(int(input())):
    text = input()
    matches = re.search(pattern, text)

    if matches:
        product_group = re.findall("[0-9]", matches.group())
        if product_group:
            print(f'Product group: {"".join(product_group)}')
        else:
            print('Product group: 00')

    else:
        print('Invalid barcode')