def new_create(data, device = 1):
    xml = '<xml>\n'
    xml += '     <telephonebook> {} </phonenumber>\n'\
        .format(data)
    xml += '     </xml>'

    with open('new_data.xml', 'w', encoding='utf-8') as newxml:
        newxml.write(xml)
    return data