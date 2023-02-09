def create(data, device = 1):
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '     <p {}>: {} </p>\n'\
        .format(style, data)
    html += '     </body>\n</html>'

    with open('phonebook.html', 'w', encoding='utf-8') as page:
        page.write(html)
    return data