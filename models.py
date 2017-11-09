import requests as r

url = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'



while True:

    re = r.get(url)
    if re.text[:2] == 'We':
        print(re.text, url)
        break
    else:
        url = 'https://stepic.org/media/attachments/course67/3.6.3/' + re.text
        print(re.text)

