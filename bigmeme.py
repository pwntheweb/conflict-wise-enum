import requests

pagenav_url = "https://courses.3rdmil.com/pagenavigation.php"
view_url = "https://courses.3rdmil.com/mod/surveymil/view.php?id="
viewkey = your_beginner_view_key

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'cookie': 'your_cookie_string',
    'Origin': 'https://courses.3rdmil.com',
    'Referer': str(viewkey)
}

data = {
    'sesskey': 'your_sess_key',
    'rightnav': 'true'
    }

for i in range(100):
    viewkey = viewkey + 1
    print(str(viewkey))
    req = requests.post(pagenav_url,data=data,headers=headers)
    req = requests.get(view_url+str(viewkey),headers=headers)
    input_lines = []
    memes = req.text.splitlines()
    dank = {}
    for line in memes:
        if "<input" in line:
            input_lines.append(line)
    for line in input_lines:
        try:
            line_name = line.split('name="')[1].split('"')[0]
            dank[line_name] = "0x000000"
        except:
            "do nothing"
    req = requests.post(view_url+str(viewkey),headers=headers,data=dank)
