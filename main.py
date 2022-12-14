import requests

respons = requests.get('https://en.wikipedia.org/wiki/Khabib_Nurmagomedov')
print(respons.status_code)
print(respons.text)

with open('khabib_2.html', 'w', encoding='utf-8') as f:
    f.write(respons.text)
   


# with open('khabib.html', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(content)