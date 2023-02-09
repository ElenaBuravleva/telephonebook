import xml_generator as xg
import html_creator as hc
import logger as lr

def search_contact(base, contact):
    base = base.split('\n')
    flag = True
    results = []
    for i in base:
        if contact in i:
            flag = False
            results.append(i)
    if flag:
        results.append(f'Контакт {contact} не найден')
    return results
xg.new_create(lr.get_base())
hc.create(lr.get_base())